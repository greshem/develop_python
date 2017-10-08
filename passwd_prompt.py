import sys;
import getpass


def _prompt_password( verify=True):
    pw = None
    if hasattr(sys.stdin, 'isatty') and sys.stdin.isatty():
        # Check for Ctl-D
        try:
            while True:
                pw1 = getpass.getpass('OS Password: ')
                if verify:
                    pw2 = getpass.getpass('Please verify: ')
                else:
                    pw2 = pw1
                if pw1 == pw2:
                    pw = pw1
                    break
        except EOFError:
            pass
    return pw

_prompt_password();
