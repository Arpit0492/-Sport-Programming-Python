

def mx(i, j):
    if i > j:
        return i
    return j


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = mx(L[i - 1][j], L[i][j - 1])

    return L[m][n]


# end of function lcs
t = int(input())

l = []
for i in range(t):
    s = input()
    nn = int(input())
    f = [x for x in input().strip().split(' ')]
    ans = 0
    # print(f)
    for fs in f:

        ans = max(ans, lcs(s, fs))

    # print(ans)
    l.append(ans)

for i in l:
    print(i)



