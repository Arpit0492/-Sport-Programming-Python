
import math
import random
from itertools import product, permutations


def super_balanced_bracket():

    T = int(input())
    for _ in range(T):
        s = input()
        left = 0
        right = len(s) - 1
        balance_count = 0
        while left < right:
            if s[left] == '(' and s[right] == ')':
                balance_count += 1
                left += 1
                right -= 1
            else:
                if s[left] != '(' and s[right] == ")":
                    left += 1
                elif s[left] == '(' and s[right] != ")":
                    right -= 1
                else:
                    left += 1
                    right -= 1
        print(balance_count * 2)


# super_balanced_bracket()


def special_binary_tree():
    T = int(input())
    mod = int(1e9+7)
    for _ in range(T):
        N = int(input())
        # print(pow(N, N-2, mod))
        s = str()
        for i in range(2, N+1):
            s += str(i)

        permList = permutations(s)
        ii = 0
        for perm in permList:
            ii += 1
            print(perm)
        print(ii)


special_binary_tree()


"""
2,[3 - 2o, 1e] -> 2
6,[7 - 4o, 3e] -> 144
8 -> 4608
9 -> 
14,[15 - 8o, 7e] -> 203212800
30,[31 - 16o,15e]
62,[63 - 32o,31e]
126,[127 - 64o,63e]
    

"""


def tiredness():
    n, d = [int(x) for x in input().split()]
    loww = int(1e7)
    maxx = 0
    for _ in range(n):
        l = [int(x) for x in input().split()]
        m = max(l)
        if m > maxx:
            maxx = m
        lo = min(l)
        if lo < loww:
            loww = lo
    m = random.randrange(1, n)
    xxi = 1
    yyi = 1
    print(m)
    for i in range(m):
        xi = xxi
        yi = yyi
        xxi = random.randint(loww, maxx)
        yyi = random.randint(loww, maxx)
        d = random.randint(0, 10)

        print(xi, yi, xxi, yyi, d)

# tiredness()


def strength_of_game():
    n, m = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    combs = []
    for skill_level in S:
        combs.append([j for j in range(0, skill_level + 1)])

    tuples_arr = product(*combs)
    xor_list = []

    for i in tuples_arr:
        xor = 0
        for j in i:
            xor ^= j
        xor_list.append(xor)

    mod = int(1e9+7)
    for i in range(m + 1):
        print(xor_list.count(i) % mod, end=' ')


# strength_of_game()
