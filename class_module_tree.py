import inspect
import os;
import sys

from oslo_utils import importutils


package="vzhucloud.api"

def _is_correct_class(obj):
    """Return whether an object is a class of the correct type and
    is not prefixed with an underscore.
    """
    return (inspect.isclass(obj) and
            (not obj.__name__.startswith('_')) )

            #issubclass(obj, self.loadable_cls_type))




def _get_classes_from_module( module_name):
    """Get the classes from a module that match the type we want."""
    classes = []
    module = importutils.import_module(module_name)
    for obj_name in dir(module):
        # Skip objects that are meant to be private.
        if obj_name.startswith('_'):
            continue
        itm = getattr(module, obj_name)
        if _is_correct_class(itm):
            classes.append(itm)
        else:
            classes.append(itm)
    return classes

def get_all_classes(path="vzhucloud/api/"):
        """Get the classes of the type we want from all modules found
        in the directory that defines this class.
        """
        classes = []
        for dirpath, dirnames, filenames in os.walk(path):
            relpath = os.path.relpath(dirpath, path)
            if relpath == '.':
                relpkg = ''
            else:
                relpkg = '.%s' % '.'.join(relpath.split(os.sep))
            for fname in filenames:
                root, ext = os.path.splitext(fname)
                if ext != '.py' or root == '__init__':
                    continue
                module_name = "%s%s.%s" % (package, relpkg, root)
                #print "%s"%module_name;
                mod_classes = _get_classes_from_module(module_name)
                #print type(mod_classes);
                for each in mod_classes:
                    if inspect.isclass(each): 
                        print "CLASS:\t %s -->   %s"%(module_name, each.__name__);
                    elif inspect.isfunction(each): 
                        print "FUN:\t %s -->   %s"%(module_name, each.__name__);
                    elif inspect.ismodule(each): 
                        print "MOD:\t %s -->   %s"%(module_name, each.__name__);

 
                #classes.extend(mod_classes)
        return classes





import sys
import os
reload(sys)
sys.setdefaultencoding('utf8') 
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'vzhucloud.settings'
import django
django.setup()

get_all_classes();
