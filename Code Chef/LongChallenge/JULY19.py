import sys


def CHFM():
    T = int(input())
    for i in range(T):
        N = int(input())
        A = [int(x) for x in input().split()]
        original_sum = sum(A)
        original_mean = original_sum / N

        count = 0
        index = -1
        for j in range(N):
            coin = A[j]
            affected_mean = (original_sum - coin) / ( N -1)
            if affected_mean == original_mean:
                count += 1
                if count > 1:
                    break
                index = j+ 1

        if index != -1:
            print(index)
        else:
            print("Impossible")


# CHFM()


def MMAX():
    T = int(input())

    for i in range(T):
        N = int(input())
        K = int(input())

        ans = 0
        if N != K:
            if K > N:
                if K % N != 0:
                    div = K // N
                    extra = K - (N * div)
                    bigger_num_count = extra
                    smaller_num_count = N - extra

                    if bigger_num_count <= smaller_num_count:
                        ans = bigger_num_count * 2
                        if bigger_num_count == smaller_num_count:
                            ans -= 1
                    else:
                        ans = smaller_num_count * 2
            else:
                bigger_num_count = K
                smaller_num_count = N - bigger_num_count
                if bigger_num_count <= smaller_num_count:
                    ans = bigger_num_count * 2
                    if bigger_num_count == smaller_num_count:
                        ans -= 1
                else:
                    ans = smaller_num_count * 2

        print(ans)


# MMAX()
"""
5
10
19
2
4
7
2
35
7
13
7
35
0
10
21
2
"""


def count_set_bits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_set_bits(n & (n - 1))

    # Algo to Ans
    # if item is not in the set, then evencount = (prevevencount * 2 + 1), oddcount = (prevoddcount) * 2
    # if item is in the set then print prevevencount and prevoddcount

    # 101001101
    #    10110
    # --------- xor
    # 101011011


def PRTAGN():
    T = int(input())

    for t in range(T):
        S1 = set()
        S2 = set()
        Q = int(input())
        even_count = 0

        for q in range(Q):
            x = int(input())

            if x not in S1:
                S1.add(x)
                if count_set_bits(x) % 2 == 0:
                    even_count += 1

                for element in S1:
                    if element != x:
                        y = x ^ element
                        if y not in S1:
                            if count_set_bits(y) % 2 == 0:
                                even_count += 1
                            S2.add(y)

                for j in S2:
                    if j not in S1:
                        S1.add(j)

                S1_len = len(S1)
                S2 = set()

                print(even_count, S1_len - even_count)
            else:
                print(even_count, len(S1) - even_count)


# PRTAGN()

# brute force way first
def CIRMERGE():

    max_size = 9223372036854775807
    T = int(input())

    for t in range(T):

        N = int(input())
        A = [int(x) for x in input().split()]
        ANS = 0

        while len(A) > 1:
            min_sum = max_size
            j = 0

            l = []
            for i in range(len(A)):
                if A[i] + A[(i + 1) % len(A)] <= min_sum:
                    min_sum = A[i] + A[(i + 1) % len(A)]
                    j = i

            A.insert(j, min_sum)
            # A.remove(A[j + 1]) # remove left
            del A[j+1]
            # A.remove(A[(j + 1) % len(A)]) # remove right adjacent to left
            del A[(j+1) % len(A)]

            ANS += min_sum

        print(ANS)


# CIRMERGE()