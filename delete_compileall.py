"""Module/script to "compile" all .py files to .pyc (or .pyo) file.

When called as a script with arguments, this compiles the directories
given as arguments recursively; the -l option prevents it from
recursing into directories.

Without arguments, if compiles all modules on sys.path, without
recursing into subdirectories.  (Even though it should do so for
packages -- for now, you'll have to deal with packages separately.)

See module py_compile for details of the actual byte-compilation.

"""

import os
import sys
import py_compile

__all__ = ["compile_dir","compile_path"]

def compile_dir(dir, maxlevels=10, ddir=None,
                force=0, rx=None, quiet=0):
    """Byte-compile all modules in the given directory tree.

    Arguments (only dir is required):

    dir:       the directory to byte-compile
    maxlevels: maximum recursion level (default 10)
    ddir:      if given, purported directory name (this is the
               directory name that will show up in error messages)
    force:     if 1, force compilation, even if timestamps are up-to-date
    quiet:     if 1, be quiet during compilation

    """
    if not quiet:
        print 'Listing', dir, '...'
    try:
        names = os.listdir(dir)
    except os.error:
        print "Can't list", dir
        names = []
    names.sort()
    success = 1
    for name in names:
        fullname = os.path.join(dir, name)
        if ddir is not None:
            dfile = os.path.join(ddir, name)
        else:
            dfile = None
        if rx is not None:
            mo = rx.search(fullname)
            if mo:
                continue
        if os.path.isfile(fullname):
            head, tail = name[:-3], name[-3:]
            if tail == '.py':
                cfile = fullname + (__debug__ and 'c' or 'o')
                ftime = os.stat(fullname).st_mtime
                try: ctime = os.stat(cfile).st_mtime
                except os.error: ctime = 0
                if (ctime > ftime) and not force: 
				except o00644          llname +nam(u5t   is is the
     umbers)hats.

Y)o_thenr�ʼ8turn 1;

Efpt   if (ctime ��ʼ     ee mod        h import�ʼ  ime �ges)nt -on if �     Is is the
  fullname = os.path.jo            # Minor cards
            iMvrmon( 5̼on/n9e given directo    nme on if �3ven directo    'pt o006446if � 5on/ngiven e3en  timesta't list", dime llname   �          (i)
            n += 1

    def telf......n  tim     devei+= 1

    de= self.get_act      =�lop_python/array_for_match.py                                                                   0000644 ��:���a=R3* tree
        tdire    1

    de= %s"_        3 1

    # [IP][0x01][���Һ͵������ not force: 
				except [IP][     3 1

    # [IP][0x01][���Һ͵������ not force: 
				except [IP][     3 1

    # [IP][0x01][���Һ͵������ not force: 
				except [IP][     3 1

    #ot force: 
				except [IP][d [IP][ce: 
		p�u 
			' o00644t	except [IP]�r_pythotT      1de5i2n	ykģ��
stctimgexcept [ 
	#EEEEEEn u'pt o   P][d [IP][ce: 
port py_c
			      [IP][py__mtime
    h4$ethon/g                                                                                 develop_python/time_str.py                                                                          0000644��Ԫ��5f,ce:  �f  # Minor ca     apit,evel_ om
except:
isnd(      [IP][p"urint joiM[ (     1on/tnd(    autf                R'3o� progra  t(26):(26o 1de5i2n	ykģ��
stctimgexcept [ 
	#EEEEEEn u'pt o   P][d [IP][ce: 
port py_c
			      [IP][py__mtime
    h4$ethon/g                                                                                 develop_python/time_str.py                                      
>('  r1  QQWry.Datʹ��				except [IP][     3 1

    #ot force: 
				except [IP][d [I2     s           
                  
>('  r1,}./time_str.py                  2Apif tail == '.py':
              R       %[        Ef>� 
			        2A' )
  r��� star   roo[      y�7mr�ַ���ʹ��strptime()����һ��ʱ��Ԫ�ع��ɵ�Ԫ��
print string;
string[0:3]                      #�ѵõ���ʱ��Ԫ��ǰ����Ԫ�ظ�ֵ����������(Ҳ����������)
#string = datetime.datetime(y, m, d)        #���ʹ��datetime�Ѹղŵõ���ʱ�����תΪ��ʽ��ʱ���ʽ����
					�vpywi�][0x02][��7exit()�ny  except getopt.GetoptError:
        # print help information and exit:
 ][0x02][��7exit()�ny  except getopt.GetoptError:
        # print help information and exit:
 ][0x02][��7e      [y  e�7e      [y  e�7e      [y  e�7e      [y  e�7e      [y  e�7e    9�7pu�#age()
n sys.p   r����ʱ�[y  e�7eur optiIs is the�7e      [y  Founظ�ֵ����������(Ҳ����������)
#string = datetime.datetime(y, m, d)        #���ʹ��datetime�Ѹղŵõ���ʱ�����תΪ��ʽ��ʱ���ʽ����
					�vpywi�][0x02][��7exit()�ny  except getopt.GetoptError:
        # print help information and exit:
 ][0x02][��7exi-     roo[  ywi�]the�7e      [y  FouS6dm���7  root"��		      [m2(�e൸����x02usr/bine�����x0Asr/b      # print help informat_mtime
    pand  infor L               deve     #�,)[IP][p"u:���datga0Asr/gcv
     'Asrmt jgetime.datetime(y                                                                                                                                                                                    athe G             S= Norror        -+

        S= Norror        -+

        S= Norror        -+

        S= Norror        -+

        S  0000644 0000 S= Nacept ge4       S=ram; if not, write             ibute it and root"��		      = write  a� =n ��'seve )l      S=ra Norr_rite   