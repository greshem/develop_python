def sortByBasename(files):
    def __sort(x1, x2):
        f1 = x1.split('\\')[-1]
        f2 = x2.split('\\')[-1]
        if f1 == f2: return 0
        elif f1 < f2: return -1
        else: return 1
    files.sort(__sort)
