
n = int(input())

# n, k = [int(x) for x in input().strip().split(' ')]

A = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i+1, n):
        if A[i]+A[j]==i+j:
            count += 1

print(count)


