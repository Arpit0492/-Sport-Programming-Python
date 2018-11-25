# n, k = [int(x) for x in raw_input().strip().split(' ')]
# A = list(map(int, input().split()))
'''
8786868
   3773
-------
   9531
'''


def add_error(a, b):
    s_a = str(a)
    s_b = str(b)
    length_s = len(s_a) if len(s_a) < len(s_b) else len(s_b)
    # print(length_s)
    prefix = s_a[:-length_s] if len(s_a) > len(s_b) else s_b[:-length_s]
    s_a = s_a[-length_s:]
    s_b = s_b[-length_s:]
    # print("Prefix = " + prefix)
    suffix = ''
    # print("HERE = " + s_a + " " + s_b)
    for i in range(length_s):
        ss = str(int(s_a[i]) + int(s_b[i]))
        suffix += (ss[-1:])
    # print('Suffix = ' + suffix)
    return int(prefix + suffix)


T = int(input())
for _ in range(T):
    A = int(input())
    B = int(input())

    actual_sum = A + B
    # print(actual_sum)
    bob_sum = add_error(A, B)
    # print(bob_sum)
    print(abs(actual_sum-bob_sum))
