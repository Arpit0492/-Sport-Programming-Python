

import math

"""
7
aaxaabc
aabcaax


7
eefhijk
ijkgggg


4
abbb
bbcc
"""


def rotation():
    N = int(input())
    S = input()
    T = input()

    if S == T:
        print(0)
    else:
        ans = N
        for i in range(N-1, -1, -1):
            # print(S[i:N])
            if T.startswith(S[i:N]):
                # print(i)
                ans = i
                break

        print(ans)
        # print(N - LCSubStr(S, T, N, N))


# rotation()

def LCSubStr(X, Y, m, n):
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result


def determine_the_winner():
    T = int(input())
    for t in range(0, T):
        n, k = [int(x) for x in input().split()]

        if n % (k+1) != 0:
            print('Dishant')
        else:
            print('Arpa')


# determine_the_winner()


def gcdproblem():
    T = int(input())
    mod = int(1e9+7)
    for t in range(T):
        N = int(input())
        ans = 0

        if N > 3:
            combs = (N-4) + 1
            total_comb_count = 0
            cum_sum = [0] * (combs+1)
            cum_sum[1] = 1
            for i in range(2, combs+1):
                cum_sum[i] = i + cum_sum[i-1]

            for i in range(1, combs+1):
                total_comb_count += (i * cum_sum[(combs+1)-i])

            comb_count_excl_one = 0
            gcdCombMap = {}

            for gcd in range(N//4, 0, -1):
                if gcd > 2 and gcd == N//4:
                    gcdCombMap[gcd] = 1
                elif gcd > 1:
                    comb = (N//gcd - 4) + 1
                    comb_count = 0
                    for i in range(1, comb+1):
                        cum_summ = cum_sum[(comb + 1) - i]
                        comb_count += (i * cum_summ)
                    gcdCombMap[gcd] = comb_count
                    comb_count_excl_one += comb_count

                else:
                    finals_combs = total_comb_count - (comb_count_excl_one + 1)
                    if N // 4 <= 2:
                        finals_combs += 1
                    ans += finals_combs
                    gcdCombMap[1] = finals_combs

            change = 0
            for gcd in sorted(gcdCombMap.keys(), reverse=True):
                if gcd > 1:
                    i = 2
                    while i <= math.sqrt(gcd):
                        if gcd % i == 0:
                            if gcd // i == i:
                                div = i
                                gcdCombMap[div] -= gcdCombMap[gcd]
                                change += gcdCombMap[gcd]
                            else:
                                div_1 = i
                                div_2 = gcd // i
                                gcdCombMap[div_1] -= gcdCombMap[gcd]
                                gcdCombMap[div_2] -= gcdCombMap[gcd]
                                change += gcdCombMap[gcd]
                                change += gcdCombMap[gcd]
                        i += 1

                    ans += pow(gcd, 4, mod) * gcdCombMap[gcd]

            gcdCombMap[1] += change

            ans += change
            print(gcdCombMap)

        print(ans % mod)


# gcdproblem()


def function_value():
    T, P = [int(x) for x in input().split()]

    for t in range(T):
        L, R = [int(x) for x in input().split()]
        if L == 1:
            # ans = 2
            expo = (R - 1) // 2 if R % 2 == 0 else R // 2
            Rs1 = (3 * (pow(3, expo, P) - 1)) // 2
            Rs2 = (Rs1 // 2) + ((R // 2) + 1) if (R // 2) % 2 == 0 else ((Rs1 - 1) // 2) + (R // 2)
            ans = Rs1 + Rs2
        else:
            Rexpo = (R - 1) // 2 if R % 2 == 0 else R // 2
            Rs1 = (3 * (pow(3, Rexpo, P) - 1)) // 2
            Rs2 = (Rs1 // 2) + ((R // 2) + 1) if (R // 2) % 2 == 0 else ((Rs1 - 1) // 2) + (R // 2)
            Lexpo = (L - 1) // 2 if L % 2 == 0 else L // 2
            Ls1 = (3 * (pow(3, Lexpo, P) - 1)) // 2
            Ls2 = (Ls1 // 2) + ((L // 2) + 1) if (L // 2) % 2 == 0 else ((Ls1 - 1) // 2) + (L // 2)
            ans = (Rs1 + Rs2) - (Ls1 + Ls2)

        print(ans % P)


function_value()

"""



"""


def function_value_2():
    T, P = [int(x) for x in input().split()]

    for t in range(T):
        L, R = [int(x) for x in input().split()]
        ans = 0
        odd_func_value = 1
        even_func_value = 1
        for N in range(L, (R + 1)):
            if N > 2:
                if N % 2 != 0:
                    odd_expo = N // 2
                    if odd_func_value == 1:
                        odd_func_value = pow(3, odd_expo, P)
                        print(N, end=" ")
                        print(" - ", end=" ")
                        print(odd_func_value)
                    else:
                        print(N, end=" ")
                        print(" - ", end=" ")
                        odd_func_value = 3 * odd_func_value
                        print(odd_func_value)
                    ans += odd_func_value
                else:
                    if even_func_value == 1:  # when we don't have last even func value
                        expo = N // 2
                        Sn = (pow(3, expo, P) - 1) // 2
                        if expo % 2 == 0:
                            Sn += 3
                        even_func_value = Sn
                        print(N, end=" ")
                        print(" - ", end=" ")
                        print(even_func_value)
                    else:
                        print(N, end=" ")
                        print(" - ", end=" ")
                        even_func_value = ((2 * odd_func_value) - even_func_value) + 2
                        print(even_func_value)
                    ans += even_func_value
            else:
                ans += 1

        print(divmod(ans, P))
        print(ans)


# function_value_2()