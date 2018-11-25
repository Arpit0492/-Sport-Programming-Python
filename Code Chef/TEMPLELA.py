T = int(input())

for t in range(T):
    n = int(input())
    A = [int(x) for x in input().strip().split(' ')]
    result = False

    if n % 2 == 0:
        result = True
    else:

        if A[0] != 1 or A[n-1] != 1:
            result = True
        else:
            mid = n//2

            d_1 = A[0]
            d_2 = A[mid]
            for i in range(1, n):

                if i <= mid:
                    d_1 = A[i] - d_1
                    if d_1 != 1:
                        result = True
                        break
                    else:
                        d_1 = A[i]

                elif i > mid:
                    d_2 -= A[i]
                    if d_2 != 1:
                        result = True
                        break
                    else:
                        d_2 = A[i]

    if result:
        print('no')
    else:
        print('yes')

    A.clear()


