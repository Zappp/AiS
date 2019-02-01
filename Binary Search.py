import random


def SzukBin(A, x):
    l = 0
    p = len(A) - 1
    i = 0

    while l <= p:
        i += 1
        k = (int)((l + p) / 2)
        if x > A[k]:
            l = k + 1
        elif x < A[k]:
            p = k - 1
        else:
            break

    print("Ilość sondowań: ", i)

    if A[k] == x:
        return k
    else:
        return 0


n = int(input('Podaj długość listy: '))
x = int(input('Podaj szukaną wartość: '))

A = random.sample(range(1, 2 * n), n)
A.sort()
z = SzukBin(A, x)
print(A)
if z == 1:
    print('SzukBin: 0')
else:
    print('SzukBin: ', z, )
