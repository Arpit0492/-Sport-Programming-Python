'''
AABABBBA as
AABABB BA - 2
4:4
ABABABAB - 4


ABBAABBBB

1:7
2:8
3:11
4:16
3:9
27:54
'''

T = int(input())

for i in range(T):
    N = int(input())
    queue = str()
    for j in range(N):
        freq, character = raw_input().split(' ')
        # print freq, character
        freq = int(freq)

        while freq > 0:
            queue += character
            freq -= 1

    # print queue

