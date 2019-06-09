"""
https://www.codechef.com/JUNE19B/problems/PROXYC#

"""


def count_attendance(count_of_P, D):
    return count_of_P/D


def proxyc():
    t = int(input())
    for _tc in range(0, t):
        D = int(input())
        attendance = list(input())

        count_of_P = sum(1 for char in attendance if char == 'P')
        # count_of_A = D - count_of_P

        current_attendance = count_attendance(count_of_P, D)
        # print(current_attendance)

        ans = 0
        if current_attendance < 0.75:
            achieved = False
            for d in range(0, len(attendance)):
                prev = d-1
                prevprev = d-2
                nexxt = d+1
                nextnext = d+2
                if attendance[d] == 'A' and prevprev >= 0 and nextnext <= len(attendance)-1 and (attendance[prev] == 'P' or attendance[prevprev] == 'P') and (attendance[nexxt] == 'P' or attendance[nextnext] == 'P'):
                    attendance[d] = 'PP'
                    count_of_P += 1
                    ans += 1
                    current_attendance = count_attendance(count_of_P, D)
                    if current_attendance >= 0.75:
                        achieved = True
                        break

            if achieved:
                print(ans)
            else:
                print(-1)

        else:
            print(ans)


# proxyc()

'''
TCs

1
10
PPAAPPAAAP
1
6
PAAAPA
1
10
PPPAAAPPAA
'''


def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r


def KS2():
    t = int(input())

    for _tc in range(0, t):

        N = int(input()) * 10

        while N:
            if sum_digits(N) % 10 == 0:
                print(N)
                break
            else:
                N += 1


# KS2()

def RSIGNSBF():
    t = int(input())
    mod = int(1e9+7)
    for _tc in range(0, t):
        K = int(input())
        ans = 10 * pow(2, K-1, mod)
        print(ans % mod)

RSIGNSBF()