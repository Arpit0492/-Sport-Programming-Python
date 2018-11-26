import math
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

    count_A = 0
    count_B = 0
    # first_char = ''
    for j in range(N):
        freq, character = [x for x in input().strip().split(' ')]
        # if j == 0:
        #     first_char = character
        freq = int(freq)

        if character == 'A':
            count_A += freq
        else:
            count_B += freq

        while freq > 0:
            queue += character
            freq -= 1

    freq_A = count_A
    freq_B = count_B
    if math.gcd(freq_A, freq_B) == 1:
        print(1)
    else:
        count_A //= math.gcd(freq_A, freq_B)
        count_B //= math.gcd(freq_A, freq_B)
        count_a = 0
        count_b = 0
        friend = 0
        for c in queue:
            if c == 'A':
                count_a += 1
            else:
                count_b += 1

            freq_a = count_a/math.gcd(count_a, count_b)
            freq_b = count_b/math.gcd(count_a, count_b)
            if count_a != 0 and count_b != 0 and freq_a / freq_b == count_A / count_B and count_a/count_b != 0:
                # if count_a == count_A and count_b == count_B:
                    friend += 1
                    count_a = 0
                    count_b = 0

        if count_a == len(queue) or count_b == len(queue):
            print(len(queue))
        else:
            if friend == 0:
                friend = 1
            print(friend)

    # print queue

