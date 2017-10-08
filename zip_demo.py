
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
L3 = [9, 10, 11, 12]
zip(L1, L2, L3)
list(zip(L1, L2, L3))
for (x, y, z) in zip(L1, L2, L3):
    print(x, '+', y, '+', z, '=', x + y + z)
