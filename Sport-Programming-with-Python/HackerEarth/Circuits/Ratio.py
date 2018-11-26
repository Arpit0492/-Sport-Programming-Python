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
        freq, character = [x for x in raw_input().strip().split(' ')]
        # print freq, character
        freq = int(freq)

        while freq > 0:
            queue += character
            freq -= 1

        a = 0
        b = 0
        friend = 0
        for c in queue:
            if c == 'A':
                a += 1
                if a == b:
                    friend += 1
                    a = 0
                    b = 0
            else:
                b += 1
                if a == b:
                    friend += 1
                    a = 0
                    b = 0

    if a == len(queue) or b == len(queue):
        print len(queue)
    else:
        if friend == 0:
            friend = 1
        print friend

    # print queue

