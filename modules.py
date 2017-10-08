#!/usr/bin/python
#2011_01_12_12:51:10 add by greshem
import sys
forceload=1;
path='a';
#if forceload and path in sys.modules:
if 1:
	if path not in sys.builtin_module_names:
		# Avoid simply calling reload() because it leaves names in
		# the currently loaded module lying around if they're not
		# defined in the new source file.  Instead, remove the
		# module from sys.modules and re-import.  Also remove any
		# submodules because they won't appear in the newly loaded
		# module's namespace if they're already in sys.modules.
		subs = [m for m in sys.modules if m.startswith(path + '.')]
		for key in [path] + subs:
			# Prevent garbage collection.
			cache[key] = sys.modules[key]
			del sys.modules[key]

