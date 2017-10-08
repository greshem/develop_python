import sys, traceback

def mock():
    lumberjack()

def lumberjack():
    bright_side_of_death()

def bright_side_of_death():
    return tuple()[1]

try:
    mock()
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print "*** print sys.exc_info:"
    print 'exc_type is: %s, exc_value is: %s, exc_traceback is: %s' % (exc_type, exc_value, exc_traceback)
    print "-" *  100

    print "*** print_tb:"
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
    print "-" *  100

    print "*** print_exception:"
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stdout)
    print "-" *  100

    print "*** print_exc:"
    traceback.print_exc()
    print "-" *  100

    print "*** format_exc, first and last line:"
    formatted_lines = traceback.format_exc().splitlines()
    print formatted_lines[0]
    print formatted_lines[-1]
    print "-" *  100

    print "*** format_exception:"
    print repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print "-" *  100

    print "*** extract_tb:"
    print repr(traceback.extract_tb(exc_traceback))
    print "-" *  100

    print "*** extract_stack:"
    print traceback.extract_stack()
    print "-" *  100

    print "*** format_tb:"
    print repr(traceback.format_tb(exc_traceback))
    print "-" *  100

    print "*** tb_lineno:", exc_traceback.tb_lineno

    print traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'), ('eggs.py', 42, 'eggs', 'return "bacon"')])


