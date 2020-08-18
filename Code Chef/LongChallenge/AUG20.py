# cook your dish here
from collections import Counter


def SKMP():
    tc = int(input())
    for _ in range(tc):
        S = input().strip()
        P = input().strip()
        charMap = Counter(S)
        print(charMap)
        charMap.subtract(Counter(P))

        print("".join(sorted([P] + [key * charMap[key] for key in charMap.keys()])))


# SKMP()


def CHEFWARS():
    tc = int(input())
    for _ in range(tc):
        H, P = [int(x) for x in input().strip().split(' ')]
        flag = 0
        while P > 0:
            H -= P
            if H <= 0:
                flag = 1
            P //= 2

        if flag == 0:
            print(0)
        else:
            print(1)

# CHEFWARS()


def calc_cost(index, chosen, cost, arr, k):
    if index == len(arr):
        return cost + find_fight_cost(chosen) + k

    chosen.append(arr[index])
    p_1 = calc_cost(index + 1, chosen, cost, arr, k)
    chosen.pop()
    p_2 = calc_cost(index + 1, [arr[index]], cost, arr, k)
    p_2 += find_fight_cost(chosen) + k

    return min(p_1, p_2)


def find_fight_cost(chosen):
    return sum([0] + [c for c in Counter(chosen).values() if c > 1])


def solve(k, fam):
    print(calc_cost(0, [], 0, fam, k))


def CHEFWED():
    tc = int(input())
    for _ in range(tc):
        N, K = [int(x) for x in input().strip().split(' ')]
        arr = [int(x) for x in input().strip().split(' ')]
        solve(K, arr)


CHEFWED()
