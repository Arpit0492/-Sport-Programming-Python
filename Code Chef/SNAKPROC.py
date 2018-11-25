
T = int(input())

for t in range(T):
    n = int(input())
    prc = input()

    f = False
    c_H = prc.count('H')
    c_T = prc.count('T')

    if c_H != c_T:
        f = True
    elif c_H == c_T != 0:
        c = str()
        for char in prc:
            if char == 'H' or char == 'T':
                c += char

        if c[0] == 'T':
            f = True
        else:
            for j in range(0, len(c)-1, 2):
                if c[j] != 'H' or c[j+1] != 'T':
                    f = True
                    break

    if f:
        print('Invalid')
    else:
        print('Valid')
