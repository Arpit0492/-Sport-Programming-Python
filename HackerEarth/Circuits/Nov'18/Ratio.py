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
    queue = list()
    count_A = 0
    count_B = 0
    for j in range(N):
        freq, character = [x for x in input().strip().split(' ')]
        queue.append(character+'-'+freq)
        freq = int(freq)

        if character == 'A':
            count_A += freq
        else:
            count_B += freq

        # while freq > 0:
        #     queue += character
        #     freq -= 1

    freq_A = count_A
    freq_B = count_B
    if math.gcd(freq_A, freq_B) == 1:
        print(1)
    elif count_A == 0 or count_B == 0:
            print(count_B if count_A == 0 else count_A)
    else:
        count_A //= math.gcd(freq_A, freq_B)
        count_B //= math.gcd(freq_A, freq_B)
        count_a = 0
        count_b = 0
        friend = 0
        for k in range(N):
            c_q, f_q = queue[k].split('-')
            # print(c_q + "--" + f_q)
            f_q = int(f_q)
            if c_q == 'A':
                count_a += f_q
            else:
                count_b += f_q

            if count_b >= count_B:
                if count_a >= count_A:

            # if count_a != 0 and count_b != 0 and (count_a + count_b) >= (count_A + count_B):
            #     count_a -= count_A
            #     count_b -= count_B
                # friend += 1
            freq_a = count_a / math.gcd(count_a, count_b)
            freq_b = count_b / math.gcd(count_a, count_b)
            if count_a != 0 and count_b != 0 and freq_a / freq_b == count_A / count_B and count_a / count_b != 0:
                if count_a == count_A and count_b == count_B:
                    friend += 1
            #         count_a = 0
            #         count_b = 0

        # if friend == 0:
        #     friend = 1
        print(friend)

    # print queue

