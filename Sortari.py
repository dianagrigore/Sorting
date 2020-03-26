import time
import random

f = open("fisier.in")
g = open("fisier.out", 'w')

v = []
inp = f.readlines()  # Citirea din fisier a datelor
t = int(inp[0][0])
f.close()


def mediana_din_3(L, p, q):
    mij = (p + q - 1) // 2
    a = L[p]
    b = L[mij]
    c = L[q]
    if a <= b <= c:
        return b
    if c <= b <= a:
        return b
    if a <= c <= b:
        return c
    if b <= c <= a:
        return c
    return a


def pivot_mediana(A):
    if len(A) < 5:
        return sorted(A)[len(A) // 2]
    subliste = [sorted(A[i:i + 5]) for i in range(0, len(A), 5)]
    mediane = [sl[len(sl) // 2] for sl in subliste]
    return pivot_mediana(mediane)


def quickSort(v, tip):
    L = []
    E = []
    G = []

    if len(v) <= 1:
        return v
    else:
        if tip == 1:
            pivot = mediana_din_3(v, 0, len(v) - 1)
        else:
            pivot = pivot_mediana(v)
        for i in v:
            if i < pivot:
                L.append(i)
            elif i > pivot:
                G.append(i)
            else:
                E.append(i)
        L = quickSort(L, tip)
        G = quickSort(G, tip)
        return L + E + G


def radix_sort(l, z):  # z e puterea lui 2 in care fac sortarea
    maximum = max(l)
    biti = 0
    while (maximum):
        biti += 1
        maximum = maximum >> 1

    if biti % z == 0:
        bit_maxim = biti // z
    else:
        bit_maxim = (biti // z) + 1
    x = l
    for i in range(bit_maxim):
        x = radixsort_offset(x, i, z)
    return x


def radixsort_offset(x, y, z):
    bit = ((2 ** z) - 1) << y * z
    buckets = [[] for a in range(2 ** z)]
    for num in x:
        bit_offset = (num & bit) >> y * z
        buckets[bit_offset].append(num)
    lista=[]
    for x in buckets:
        for y in x:
            lista.append(y)
    return lista


def countsort(v):  # CountSort
    m = max(v)
    fr = [0 for i in range(10 ** 6)]
    for x in v:
        fr[x] += 1

    rez = []
    for i in range(10 ** 6):
        while fr[i] > 0:
            rez.append(i)
            fr[i] -= 1

    return rez


def bubblesort(l):  # BubbleSort
    p = 0
    while p == 0:
        p = 1
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                a = l[i]
                l[i] = l[i + 1]
                l[i + 1] = a
                p = 0
    return l


def interclasare(lst, ldr):  # Interclasare mergesort
    i = j = 0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] < ldr[j]:
            rez.append(lst[i])
            i = i + 1
        else:
            rez.append(ldr[j])
            j = j + 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez


def mergesort(lista):  # Mergesort
    if len(lista) <= 1:
        return lista
    else:
        mij = len(lista) // 2
        lst = mergesort(lista[:mij])
        ldr = mergesort(lista[mij:])
        return interclasare(lst, ldr)


def genereaza(n, maxim):
    lis = []
    for x in range(n):
        nr = random.randint(0, maxim + 1)
        lis.append(nr)
    return lis


def testare(l):  # Functie care testeaza daca vectorul este intr-adevar sortat
    ok = 1
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            ok = 0
    if ok == 0:
        g.write(" nu e sortat")
    else:
        g.write(" e sortat")


for teste in range(0, t):
    intrare = inp[teste + 1].split()
    n = int(intrare[0])
    maxim = int(intrare[1])
    lista = genereaza(n, maxim)

    g.write('Testul ' + str(teste + 1) + ':\n')
    g.write('valoare maxima este ' + str(maxim) + ' nr. maxim de elemente este ' + str(n) + '\n')
    if maxim < 10 ** 6:
        start_time = time.time()
        sol = countsort(lista)
        g.write('Countsort ')
        testare(sol)
    else:
        start_time = time.time()
        g.write('Countsort: ')
        g.write('Nu se poate sorta')
    g.write("  %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    if n <= 3000:
        sol = bubblesort(lista)
        g.write('Bubble Sort: ')
        testare(sol)
    else:
        g.write('Bubble Sort: ')
        g.write("Nu se poate sorta")
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = radix_sort(lista, 8)
    g.write('Radixsort in baza 256: ')
    testare(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = radix_sort(lista, 1)
    g.write('Radixsort in baza 2: ')
    testare(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = mergesort(lista)
    g.write('Mergesort: ')
    testare(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = quickSort(lista, 1)
    g.write('Quicksort cu mediana din 3: ')
    testare(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol = quickSort(lista, 2)
    g.write('Quicksort cu mediana medianelor: ')
    testare(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')

    start_time = time.time()
    sol.sort()
    g.write("Sortare implicita Python: ")
    testare(sol)
    g.write(" %s secunde " % str(round((time.time() - start_time), 3)))
    g.write('\n')
    g.write('\n')
    g.write('\n')
