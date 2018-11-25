from math import sqrt
from itertools import count
from collections import defaultdict


def prime_candidates(begin=5, end=1000000):

    cur = begin
    if cur % 2 == 0:
        if cur == 2:
            yield 2
        cur += 1
    if cur % 6 == 3:
        if cur == 3:
            yield 3
        cur += 2
    elif cur % 6 == 1:
        yield cur
        cur += 4
    gen = count(cur, step=6) if not end else range(cur, end, 6)

    for n in gen:
        yield n
        yield n + 2


for q in prime_candidates():
    print(q)
def gen_primes(mx):

    mx_sqrt = int(sqrt(mx)) + 1
    D = {}
    yield 2
    yield 3
    for q in prime_candidates():
        if q >= mx:
            return
        if q not in D:
            yield q
            if q < mx_sqrt:
                D[q * q] = [q]
        else:
            for p in D[q]:
                qp = q + p
                while qp % 6 not in [1, 5]:
                    qp += p
                if qp < mx:
                    D.setdefault(qp, []).append(p)
            del D[q]


def factorize(n):

    res = defaultdict(lambda: 0)
    for p in gen_primes(n):
        while n % p == 0:
            n = n // p
            res[p] += 1
        if n == 1:
            return dict(res)


N = int(input())
s = input()

count = 0

for j in range(N):
    if s[j] == 'b':

        sq = (j+1)**2

        d = factorize(sq)

        for key in d.keys():
            pw = d[key]
            for i in range(1,pw+1):
                fac = key ** i
                div = sq//fac
                if fac < N and div < N:
                    if s[fac-1] == 'a' and s[div-1] == 'c':
                        # print(fac,end=" ")
                        # print(div)
                        count += 1
                    if s[fac-1] =='c' and s[div-1] =='a':
                        # print(fac, end=" ")
                        # print(div)
                        count += 1



print(count)