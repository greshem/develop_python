from itertools import chain, imap
def flatmap(f, items):
        return chain.from_iterable(imap(f, items))
