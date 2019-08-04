

def MSNSADM1():
    T = int(input())
    for _ in range(T):
        N = int(input())
        goals = [int(x) for x in input().split()]
        fouls = [int(x) for x in input().split()]
        max = 0
        for i in range(N):
            score = (goals[i] * 20) - (fouls[i] * 10)
            if score > max:
                max = score
        print(max)


# MSNSADM1()

def DSTAPLS():
    T = int(input())
    for _ in range(T):
        N, K = [int(x) for x in input().split()]
        rem = N // K
        if rem < K:
            print("YES")
        else:
            if rem % K == 0:
                print('NO')
            else:
                print('YES')


# DSTAPLS()


def CHEFDIL():
    T = int(input())
    for _ in range(T):
        S = input()
        one_count = S.count("1")
        print("WIN" if one_count%2!=0 else "LOSE")


CHEFDIL()