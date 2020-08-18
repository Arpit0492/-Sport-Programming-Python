

def no_of_triangles():
    t = int(input())
    for _ in range(t):
        A = [int(i) for i in input().split(' ')]
        vertices = A[0]
        s1 = A[1]
        s2 = A[2]

        sides = vertices
        var = 1
        adjacent = abs(s1-s2)
        if adjacent < 2 or adjacent == vertices - 1:
            sides -= 3
        elif adjacent == 2 or adjacent == vertices - 2:
            sides -= 4
        else:
            sides -= 4
            var += 1
        ans = sides * (vertices - 5) + var
        print(ans)

# no_of_triangles()


def bubble_sort():
    n = int(input())
    A = [int(i) for i in input().split(' ')]
    count = 0
    swapped = True
    while swapped:
        swapped = False
        count += 1
        for i in range(n-1):
            if A[i] > A[i+1]:
                temp = A[i+1]
                A[i+1] = A[i]
                A[i] = temp
                swapped = True

    print(count)


# bubble_sort()