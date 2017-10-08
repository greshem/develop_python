
import random
import string
VALIDSET=frozenset(set(string.ascii_letters) | set(string.digits) | set('-_.~'))
VALIDSTR=''.join(c for c in VALIDSET)
VALIDSET_DESC='alphanumeric and -_.~'

def generate_password():
    ''' Very dumb 20-character password generation '''
    random.seed()
    return ''.join(random.choice(VALIDSTR) for _ in xrange(20))


print generate_password();
