
"""
    This file is part of Web Portage.

    Web Portage is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Web Portage is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Web Portage; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
    
    Portions of the code in Web Portage are derivative works based in whole
    or part on source code supplied as part of the "Portage" package in the
    Gentoo GNU/Linux distribution (http://www.gentoo.org)
"""

import portage
import string
import re
import os
import sys

from depgraph import *

VERSION_SHORT=1
VERSION_RELEASE=2

spinpos=0
spinner="\|/-\|/-"

def update_spinner():
	global spinner, spinpos
	if sys.stdout.isatty():
		sys.stdout.write("\b"+spinner[spinpos])
		spinpos=(spinpos+1)%8
		sys.stdout.flush()

def getInstallationStatus(package):
	installed_package = portage.db["/"]["vartree"].dep_bestmatch(package)
	result = ""
	version = getVersion(installed_package,VERSION_RELEASE)
	if len(version) > 0:
		result = version
	else:
		result = "Not Installed"
	return result

def getVersion(full_package,detail):
	if len(full_package) > 1:
		package_parts = portage.catpkgsplit(full_package)
		if detail == VERSION_RELEASE and package_parts[3] != 'r0':
			result = package_parts[2]+ "-" + package_parts[3]
		else:
			result = package_parts[2]
	else:
		result = ""
	return result

# search functionality
class websearch:
	#
	# public interface
	#
	def __init__(self):
		"""Searches the available and installed packages for the supplied search key.
		The list of available and installed packages is created at object instantiation.
		This makes successive searches faster."""
		self.installcache = portage.db["/"]["vartree"]

	def execute(self,searchkey, searchdesc=None):
		"""Performs the search for the supplied search key"""

		self.searchkey=searchkey
		self.packagematches = []


		if searchdesc == 1:
			self.matches = {"pkg":[], "desc":[]}
		else:
			self.matches = {"pkg":[]}
		if self.searchkey=="*":
			#hack for people who aren't regular expression gurus
			self.searchkey==".*"
		for package in portage.portdb.cp_all():
			package_parts=package.split("/")
			masked=0
			if re.search(self.searchkey.lower(), package_parts[1].lower()):
				if not portage.portdb.xmatch("match-visible",package):
					masked=1
				self.matches["pkg"].append([package,masked])
			elif searchdesc: # DESCRIPTION searching
				full_package = portage.portdb.xmatch("bestmatch-visible",package)
				if not full_package:
					#no match found; we don't want to query description
					full_package=portage.best(portage.portdb.xmatch("match-all",package))
					if not full_package:
						continue
					else:
						masked=1
				try:
					full_desc, homepage = portage.portdb.aux_get(full_package,["DESCRIPTION"] ["HOMEPAGE"])
				except KeyError:
					print "emerge: search: aux_get() failed, skipping"
					continue
				if re.search(self.searchkey.lower(), full_desc.lower()):
					self.matches["desc"].append([full_package,masked])
		self.mlen=0
		for mtype in self.matches.keys():
			self.matches[mtype].sort()
			self.mlen += len(self.matches[mtype])

	def output(self):
		"""Outputs the results of the search."""
		output = "\b\b	\n[ Results for search key : "+ self.searchkey +" ]"
		output += "[ Applications found : "+ str(self.mlen) +" ]"
		output += " "
		result = []
		for mtype in self.matches.keys():
			for match,masked in self.matches[mtype]:
				if mtype=="pkg":
					catpack=match
					full_package = portage.portdb.xmatch("bestmatch-visible",match)
					if not full_package:
						#no match found; we don't want to query description
						masked=1
						full_package=portage.best(portage.portdb.xmatch("match-all",match))
				else:
					full_package=match
					catpack=portage.pkgsplit(match)[0]
				if full_package:
					try:
						desc, homepage = portage.portdb.aux_get(full_package,["DESCRIPTION","HOMEPAGE"])
					except KeyError:
						output += "emerge: search: aux_get() failed, skipping"
						continue
					if masked:
						output += "*" + "	" + match +" "+ "[ Masked ]"
					else:
						output +=  "*" + "	" + match
					myversion = getVersion(full_package, VERSION_RELEASE)

					mysum = [0,0]
					mycat = match.split("/")[0]
					mypkg = match.split("/")[1] + "-" + myversion

					mydigest = portage.config()["PORTDIR"] + "/"  + match + "/files/digest-" + mypkg

					try:
						myfile = open(mydigest,"r")
						for line in myfile.readlines():
							mysum[0] += int(line.split(" ")[3])
						myfile.close()
						mystr = str(mysum[0]/1024)
						mycount=len(mystr)
						while (mycount > 3):
							mycount-=3
							mystr=mystr[:mycount]+","+mystr[mycount:]
						mysum[0]=mystr+" kB"
					except Exception, e:
						mysum[0]=" [no/bad digest]"

					result.append({ "Name": match,
							"Available": myversion,
							"Status": getInstallationStatus(catpack),
							"Size": mysum[0],
							"Homepage": homepage,
							"Description": desc,
							"Masked": masked})
		return result
