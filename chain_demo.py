
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


for each in  chain(range(1,10), range(22,33)):
    print each;
