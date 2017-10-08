# -*- coding: utf-8 -*-
#    Copyright (C) 2007 Stewart Adam
#    This file is part of audio-convert-mod.

#    audio-convert-mod is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    audio-convert-mod is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with audio-convert-mod; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
The various formats audio-convert-mod supports.

Each format is a class:
  __encode = bool
  __decode = bool
  extension = ['ext1', 'ext2'] /* ALL IN lowercase */
  __qualities = [['quality#','desc'], ['quality#','desc']]
  check(self): Checks for any required programs
  decode(file): (decode file into WAV)
  encode(wavfile): (encode WAV into format)

To add support for new formats, add a entry under checkFormat() and create
the new format functions.

** Remember when making new formats that Windows cannot handle single-quotes,
   only double quotes.
"""

import os
import subprocess
from audio_convert_mod.i18n import _
from audio_convert_mod.const import *

environ = {'PATH': str(os.getenv('PATH'))}

def getNewExt(ext, filename):
    return '%s.%s' % ('.'.join(filename.split('.')[:-1]), ext)

def which(program):
  """ Emulates unix `which` command """
  for path in os.getenv('PATH').split(os.pathsep):
    programPath = os.path.join(path, program)
    if os.path.exists(programPath) and os.path.isfile(programPath):
      return programPath
    if os.path.exists(programPath+'.exe') and os.path.isfile(programPath+'.exe'):
      return programPath
  return False

""" Check if the required programs exist """
class wav:
  """ ?wav >> ?wav  """
  def __init__(self):
    """ Initialize """
    self.__encode = True
    self.__decode = True
    self.extensions = ['wav']
    self.check()
    self.__qualities = [
    ['0', _('(Based on original file)')]
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    pass

  def decode(self, filename):
    command = "echo .5"
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    command = "echo 1"
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class mp3:
  """ Lame >> MP3 """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['mp3']
    self.check()
    self.__qualities = [
    ['56', '56 kbps'],
    ['96', '96 kbps'],
    ['128', '128 kbps'],
    ['160', '160 kbps'],
    ['192', '192 kbps'],
    ['256', '256 kbps'],
    ['320', '320 kbps'],
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('lame'):
      self.__encode, self.__decode = True, True
    else:
      self.__encode, self.__decode = False, False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def decode(self, filename):
    """ Decodes a MP3 file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'lame.exe --decode --mp3input "%(a)s" "%(b)s" -- 2>&1 | awk.exe -vRS="\\r" -F"[ /]+" "(NR>2){print $2/$3;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "lame --decode --mp3input '%(a)s' '%(b)s' -- 2>&1 | awk -vRS='\\r' -F'[ /]+' '(NR>2){print $2/$3;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    """ Encodes a new MP3 file """
    if MSWINDOWS:
      command = 'lame.exe -m auto --preset cbr %(a)i "%(b)s" "%(c)s" 2>&1 | awk.exe -vRS="\\r" "(NR>3){gsub(/[()%%|]/,\\" \\");if($1 != \\"\\") print $2/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "lame -m auto --preset cbr %(a)i '%(b)s' '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>3){gsub(/[()%%|]/,\" \");if($1 != \"\") print $2/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    if MSWINDOWS:
      return None
    command = "id3info '%(a)s' | awk" % {'a': filename}
    tags = []
    for i in [
              "'/TIT2/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/TPE1/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/TALB/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/TYER/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/TRCK/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/TCON/ { print substr($0, match($0, /:/) + 2 )}'",
              "'/COMM (Comments)/ { print substr($0, match($0, /:/) + 24)}'",
             ]:
      sub = subprocess.Popen('%s %s' % (command, i), shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      sub.wait()
      tags.append('\n'.join(sub.stdout.read().split('\n')[:-1]))
    return tags

  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    command = "id3tag '%(a)s' --song='%(b)s' --artist='%(c)s' --album='%(d)s' --year='%(e)s' --track='%(f)s' --genre='%(g)s' --comment='%(h)s' " % {'a': filename, 'b': tags[0], 'c': tags[1], 'd': tags[2], 'e': tags[3], 'f': tags[4], 'g': tags[5], 'h': tags[6]}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    sub.wait()

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class flac:
  """ flac >> flac """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['flac']
    self.check()
    self.__qualities = [
    ['0', _('Lossless, fastest compression (0)')],
    ['2', _('Lossless, fast compression (2)')],
    ['4', _('Lossless, moderate compression (4)')],
    ['6', _('Lossless, high compression (6)')],
    ['8', _('Lossless, highest compression (8)')],
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('flac'):
      self.__encode, self.__decode = True, True
    else:
      self.__encode, self.__decode = False, False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]
    
  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    if MSWINDOWS:
      return None
    tags = []
    command = "metaflac --no-filename '%(a)s' " % {'a': filename}
    for i in [
             '--show-tag=title',
             '--show-tag=artist',
             '--show-tag=album',
             '--show-tag=date',
             '--show-tag=tracknumber',
             '--show-tag=genre',
             '--show-tag=description',
             ]:  
      sub = subprocess.Popen('%s %s' % (command, i), shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      sub.wait()
      tag = '\n'.join(sub.stdout.read().split('\n')[:-1])
      if len(tag.split('=')[0]) >= 2:
        tags.append('='.join(tag.split('=')[1:]))
      else:
        tags.append(tag)
    return tags

  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    command = "metaflac '%(a)s' --set-tag title='%(b)s' --set-tag artist='%(c)s' --set-tag album='%(d)s' --set-tag date='%(e)s' --set-tag tracknumber='%(f)s' --set-tag genre='%(g)s' --set-tag description='%(h)s'" % {'a': filename, 'b': tags[0], 'c': tags[1], 'd': tags[2], 'e': tags[3], 'f': tags[4], 'g': tags[5], 'h': tags[6]}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    sub.wait()
    
  def decode(self, filename):
    """ Decodes a FLAC file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'flac.exe -d -f "%(a)s" -o "%(b)s" 2>&1 | awk.exe -vRS="\\r" -F":" "!/done/{gsub(/ /,\\"\\");gsub(/%% complete/,\\"\\");;gsub(/%%complete/,\\"\\");if(NR>1) print $2/100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "flac -d -f '%(a)s' -o '%(b)s' 2>&1 | awk -vRS='\\r' -F':' '!/done/{gsub(/ /,\"\");gsub(/%% complete/,\"\");;gsub(/%%complete/,\"\");if(NR>1) print $2/100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    """ Encodes a new FLAC file """
    if MSWINDOWS:
      command = 'flac.exe -f --compression-level-%(a)i "%(b)s" -o "%(c)s" 2>&1 | awk.exe -vRS="\\r" -F":" "!/wrote/{gsub(/ /,\\"\\");if(NR>1)print $2/100;fflush();}" | awk.exe -F"%%" "{printf $1\\"\\n\\";fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "flac -f --compression-level-%(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' -F':' '!/wrote/{gsub(/ /,\"\");if(NR>1)print $2/100;fflush();}' | awk -F'%%' '{printf $1\"\\n\";fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class ogg:
  """ oggenc >> OGG (vorbis-tools) """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.check()
    self.extensions = ['ogg']
    self.__qualities = [
    ['-1', '~40 kbps'],
    ['0', '~64 kbps'],
    ['1', '~80 kbps'],
    ['2', '~100 kbps'],
    ['3', '~110 kbps'],
    ['4', '~120 kbps'],
    ['5', '~130 kbps'],
    ['6', '~170 kbps'],
    ['7', '~200 kbps'],
    ['8', '~230 kbps'],
    ['9', '~280 kbps'],
    ['10', '400+ kbps'],
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('oggdec'):
      self.__decode = True
    else:
      self.__decode = False
    if which('oggenc'):
      self.__encode = True
    else:
      self.__encode = False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    if MSWINDOWS:
      return None
    command = "ogginfo '%(a)s' | awk '/title=/ { print substr($0, match($0, /=/) + 1 ) } /artist=/ { print substr($0, match($0, /=/) + 1 ) } /album=/ { print substr($0, match($0, /=/) + 1 ) } /date=/ { print substr($0, match($0, /=/) + 1 ) } /tracknumber=/ { print substr($0, match($0, /=/) + 1 ) } /genre=/ { print substr($0, match($0, /=/) + 1 ) }'" % {'a': filename}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    sub.wait()
    tags = []
    out = sub.stdout.read().split('\n')
    tags.append(out[0]) #title
    tags.append(out[1]) #artist
    tags.append(out[3]) #album
    tags.append(out[3]) #date
    tags.append(out[5]) #track number
    tags.append(out[2]) #genre
    tags.append('') #description/comments
    return tags
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    command = "vorbiscomment -a '%(a)s' -t 'TITLE=%(b)s' -t 'ARTIST=%(c)s' -t 'ALBUMB=%(d)s' -t 'DATE=%(e)s' -t 'TRACKNUMBER=%(f)s' -t 'GENRE=%(g)s' -t 'DESCRIPTION=%(h)s'" % {'a': filename, 'b': tags[0], 'c': tags[1], 'd': tags[2], 'e': tags[3], 'f': tags[4], 'g': tags[5], 'h': tags[6]}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    sub.wait()
    
  def decode(self, filename):
    """ Decodes a OGG file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'oggdec.exe "%(a)s" -o "%(b)s" 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $2/100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "oggdec '%(a)s' -o '%(b)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $2/100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality, tags=None):
    """ Encodes a new OGG file """
    if tags and MSWINDOWS:
      command = 'oggenc.exe --title "%(d)s" --artist "%(e)s" --album "%(f)s" --date "%(g)s" --tracknum "%(h)s" --genre "%(i)s" --comment "%(j)s" -q %(a)i "%(b)s" -o "%(c)s" 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $2/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname, 'd': tags[0], 'e': tags[1], 'f': tags[2], 'g': tags[3], 'h': tags[4], 'i': tags[5], 'j': tags[6]}
    elif tags and not MSWINDOWS:
      command = "oggenc --title '%(d)s' --artist '%(e)s' --album '%(f)s' --date '%(g)s' --tracknum '%(h)s' --genre '%(i)s' --comment '%(j)s' -q %(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $2/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname, 'd': tags[0], 'e': tags[1], 'f': tags[2], 'g': tags[3], 'h': tags[4], 'i': tags[5], 'j': tags[6]}
    elif not tags and MSWINDOWS:
      command = 'oggenc.exe -q %(a)i "%(b)s" -o "%(c)s" 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $2/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    elif not tags and not MSWINDOWS:
      command = "oggenc -q %(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $2/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    else: # just incase.
      command = "oggenc -q %(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $2/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class mpc:
  """ mppdec >> MPC (musepack-tools) """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['mpc']
    self.check()
    self.__qualities = [
    ['1','~35 kbps'],
    ['2','~64 kbps'],
    ['3','~90 kbps'],
    ['4','~130 kbps'],
    ['5','~170 kbps'],
    ['6','~200 kbps'],
    ['7','~210 kbps'],
    ['8','~240 kbps'],
    ['9','~260 kbps'],
    ['10','~280 kbps'],
                      ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('mppdec'):
      self.__decode = True
    else:
      self.__decode = False
    if which('mppenc'):
      self.__encode = True
    else:
      self.__encode = False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    return None
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    return

  def decode(self, filename):
    """ Decodes a MPC file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'mppdec.exe "%(a)s" "%(b)s" 2>&1 | awk.exe -vRS="\\r" -F"[ (]+" "!/s/{gsub(/(%%)/,\\" \\");if(NR>5)print $5/100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "mppdec '%(a)s' '%(b)s' 2>&1 | awk -vRS='\\r' -F'[ (]+' '!/s/{gsub(/(%%)/,\" \");if(NR>5)print $5/100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    """ Encodes a new MPC file """
    if MSWINDOWS:
      command = 'mppenc.exe --quality %(a)i --overwrite "%(b)s" "%(c)s" 2>&1 | awk.exe -vRS="\\r" "!/^$/{if (NR>5) print $1/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "mppenc --quality %(a)i --overwrite '%(b)s' '%(c)s' 2>&1 | awk -vRS='\\r' '!/^$/{if (NR>5) print $1/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class ape:
  """ mac >> ape """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.check()
    self.extensions = ['ape']
    self.__qualities = [
    ['1000','1000'],
    ['2000','2000'],
    ['3000','3000'],
    ['4000','4000'],
    ['5000','5000'],
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('mac'):
      self.__decode, self.__encode = True, True
    else:
      self.__decode, self.__encode = False, False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    return None
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    return

  def decode(self, filename):
    """ Decodes a MAC file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'mac.exe "%(a)s" "%(b)s" -d 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $2/100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "mac '%(a)s' '%(b)s' -d 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $2/100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    """ Encodes a new MAC file """
    if MSWINDOWS:
      command = 'mac.exe "%(b)s" "%(c)s" -c%(a)i 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $2/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "mac '%(b)s' '%(c)s' -c%(a)i 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $2/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class aac:
  """ faad >> AAC """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['m4a', 'aac', 'mp4']
    self.check()
    self.__qualities = [
    ['100','50%'],
    ['100','100%'],
    ['200','200%'],
    ['30','300%'],
    ['400','400%'],
    ['500','500%'],
                      ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('faad'):
      self.__decode = True
    else:
      self.__decode = False
    if which('faac'):
      self.__encode = True
    else:
      self.__encode = False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    if MSWINDOWS:
      return None
    command = 'faad -i "%(a)s" 2>&1 | awk' % {'a': filename}
    tags = []
    for i in [
              "'/title/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/artist/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/album/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/date/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/track/ { print substr($0, match($0, /:/) + 2 ) }'",
              "'/genre/ { print substr($0, match($0, /:/) + 2 )}'",
              "'/comment/ { print substr($0, match($0, /:/) + 2)}'",
             ]:
      sub = subprocess.Popen('%s %s' % (command, i), shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
      sub.wait()
      tags.append('\n'.join(sub.stdout.read().split('\n')[:-1]))
    return tags
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    return

  def decode(self, filename):
    """ Decodes a AAC file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'faad.exe "%(a)s" -o "%(b)s" 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $1/100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "faad '%(a)s' -o '%(b)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $1/100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality, tags=None):
    """ Encodes a new AAC file """
    if tags and MSWINDOWS:
      command = 'faac.exe -w --title "%(d)s" --artist "%(e)s" --album "%(f)s" --year "%(g)s" --track "%(h)s" --genre "%(i)s" --comment "%(j)s" -q %(a)i "%(b)s" -o "%(c)s" 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $3/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname, 'd': tags[0], 'e': tags[1], 'f': tags[2], 'g': tags[3], 'h': tags[4], 'i': tags[5], 'j': tags[6]}
    if tags and not MSWINDOWS:
      command = "faac -w --title '%(d)s' --artist '%(e)s' --album '%(f)s' --year '%(g)s' --track '%(h)s' --genre '%(i)s' --comment '%(j)s' -q %(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $3/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname, 'd': tags[0], 'e': tags[1], 'f': tags[2], 'g': tags[3], 'h': tags[4], 'i': tags[5], 'j': tags[6]}
    if not tags and MSWINDOWS:
      command = 'faac.exe -w -q %(a)i "%(b)s" -o "%(c)s" 2>&1 | awk.exe -vRS="\\r" "(NR>1){gsub(/%%/,\\" \\");print $3/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    if not tags and not MSWINDOWS:
      command = "faac -w -q %(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $3/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "faac -w -q %(a)i '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\\r' '(NR>1){gsub(/%%/,\" \");print $3/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class mplayer:
  """ mplayer >> WMA, SHN """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['wma', 'shn']
    self.check()
    self.__qualities = [
    ['-', _('(Based on original file)')]
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('mplayer'):
      self.__decode = True
    else:
      self.__decode = False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    return None
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    return
  
  # FIXME: Finish this
  def decode(self, filename):
    """ Decodes a mplayer-playable file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'mplayer.exe -quiet -vo null -vc dummy -ao pcm:waveheader:file="%(b)s" "%(a)s" 2>&1 | awk.exe -vRS="\\r" "($2~/^[-+]?[0-9]/ && $5~/^[-+]?[0-9]/){print $2/$5*100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "mplayer -quiet -vo null -vc dummy -ao pcm:waveheader:file='%(b)s' '%(a)s' 2>&1 | awk -vRS='\\r' '($2~/^[-+]?[0-9]/ && $5~/^[-+]?[0-9]/){print $2/$5*100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class ac3:
  """ a52dec >> AC3 """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['ac3']
    self.check()
    self.__qualities = [
    ['56', '56 kbps'],
    ['96', '96 kbps'],
    ['128', '128 kbps'],
    ['160', '160 kbps'],
    ['192', '192 kbps'],
    ['256', '256 kbps'],
    ['320', '320 kbps'],
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('a52dec'):
      self.__decode = True
    else:
      self.__decode = False
    if which('ffmpeg'):
      self.__encode = True
    else:
      self.__encode = False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    return None
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    return

  def decode(self, filename):
    """ Decodes a AC3 file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'echo 0;a52dec.exe -o wav "%(a)s" > "%(b)s"' % {'a': filename, 'b': newname}
    else:
      command = "echo 0;a52dec -o wav '%(a)s' > '%(b)s'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    """ Encodes a new AC3 file """
    if MSWINDOWS:
      command = 'echo 0;ffmpeg.exe -i "%(b)s" -ab %(a)ik "%(c)s" 2>&1 | awk.exe -vRS="\10\10\10\10\10\10" "(NR>1){gsub(/%%/,\\" \\");if($1 != \\"\\") print $1;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "echo 0;ffmpeg -i '%(b)s' -ab %(a)ik '%(c)s' 2>&1 | awk -vRS='\10\10\10\10\10\10' '(NR>1){gsub(/%%/,\" \");if($1 != \"\") print $1;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

class wv:
  """ wavpack >> WVPK """
  def __init__(self):
    """ Initialize """
    self.__encode = False
    self.__decode = False
    self.extensions = ['wv', 'wvc']
    self.check()
    self.__qualities = [
    ['0', _('Low compression')],
    ['1', _('High compression')],
    ['2', _('Very high compression')],
                       ]

  def check(self):
    """ Check if the required program(s) exist """
    if which('wvunpack'):
      self.__decode = True
    else:
      self.__decode = False
    if which('wavpack'):
      self.__encode = True
    else:
      self.__encode = False

  def get(self):
    """ Return all information on the format """
    return [self.__encode, self.__decode, self.__qualities]

  def getTags(self, filename):
    """ Retrieves the metadata from filename """
    return None
    
  def setTags(self, filename, tags):
    """ Sets the metadata on filename """
    if MSWINDOWS:
      return
    return

  # -c || -i for lossless||lossy.... I smell workarounds :/
  def decode(self, filename):
    """ Decodes a WVPk file """
    newname = getNewExt('wav', filename)
    if MSWINDOWS:
      command = 'wvunpack.exe "%(a)s" -o "%(b)s" 2>&1 | awk.exe -vRS="\10\10\10\10\10\10" "(NR>1){gsub(/%%/,\\" \\");if($1 != \\"\\") print $1/100;fflush();}"' % {'a': filename, 'b': newname}
    else:
      command = "wvunpack '%(a)s' -o '%(b)s' 2>&1 | awk -vRS='\10\10\10\10\10\10' '(NR>1){gsub(/%%/,\" \");if($1 != \"\") print $1/100;fflush();}'" % {'a': filename, 'b': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

  def encode(self, filename, newname, quality):
    """ Encodes a new WVPK file """
    if quality == 0:
      quality = '-f'
    elif quality == 1:
      quality = '-h'
    elif quality == 2:
      quality = '-hh'
    if MSWINDOWS:
      command = 'wavpack.exe -y %(a)s "%(b)s" -o "%(c)s" 2>&1 | awk.exe -vRS="\10\10\10\10\10\10" "(NR>1){gsub(/%%/,\\" \\");if($1 != \\"\\") print $1/100;fflush();}"' % {'a': quality, 'b': filename, 'c': newname}
    else:
      command = "wavpack -y %(a)s '%(b)s' -o '%(c)s' 2>&1 | awk -vRS='\10\10\10\10\10\10' '(NR>1){gsub(/%%/,\" \");if($1 != \"\") print $1/100;fflush();}'" % {'a': quality, 'b': filename, 'c': newname}
    sub = subprocess.Popen(command, shell=True, env=environ, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return sub, command

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
MP3 = mp3()
OGG = ogg()
MPC = mpc()
APE = ape()
AAC = aac()
AC3 = ac3()
WV = wv()
WAV = wav()
FLAC = flac()

FORMATS = [MP3, OGG, MPC, APE, AAC, AC3, WV, WAV, FLAC]

def recheck():
  """ Recheck all formats """
  for format in FORMATS:
    format.check()

def getFileType(path):
  """ Return the file type based on extension """
  fileExtension = path.split('.')[-1].lower()
  for format in FORMATS:
    for extension in format.extensions:
      if fileExtension == extension:
        return format
  # unknown filetype!
  return False

def decodable(path):
  """ Checks if a given file is currently decodable """
  fileType = getFileType(path)
  if fileType == False:
    # unknown filetype!
    return False
  return fileType.get()[0]

