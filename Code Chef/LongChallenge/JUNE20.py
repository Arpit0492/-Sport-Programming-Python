


def CHFICRM():

    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split(' ')]

        '''
        5 5 10
        '''
        canGive = True
        coins = {5: 0, 10: 0, 15: 0}
        for ai in a:
            if ai == 5:
                coins[ai] += 1
            elif ai == 10:
                if coins[5] >= 1:
                    coins[5] -= 1
                    coins[ai] += 1
                else:
                    canGive = False
                    break
            elif ai == 15:
                if coins[10] >= 1:
                    coins[10] -= 1
                    coins[15] += 1
                elif coins[5] >= 2:
                    coins[5] -= 2
                    coins[15] += 1
                else:
                    canGive = False
                    break

        if canGive:
            print("YES")
        else:
            print("NO")


# CHFICRM()

def PRICECON():
    t = int(input())
    for _ in range(t):
        n, k = [int(i) for i in input().split(' ')]
        a = [int(i) for i in input().split(' ')]

        chefRevenueLoss = 0
        for ai in a:
            if ai > k:
                chefRevenueLoss += ai-k
        print(chefRevenueLoss)


# PRICECON()


def XYSTR():
    t = int(input())
    for _ in range(t):
        s = input()
        # xyxxy
        pairCount = 0
        i = 0
        while i < len(s) - 1:
            if s[i] == 'x' and s[i + 1] == 'y' or s[i] == 'y' and s[i + 1] == 'x':
                pairCount += 1
                i += 2
            else:
                i += 1

        print(pairCount)

# XYSTR()


def EOEO():
    t = int(input())
    for _ in range(t):
        ts = int(input())
        while ts % 2 == 0:
            ts = ts // 2
        print(ts // 2)

# EOEO()


def write_desc(x, y):
    for i in range(y-1, x-1, -1):
        print(i, ' ', end='')


def write_incr(x, y):
    for i in range(x, y):
        print(i, ' ', end='')


def EVNM():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x = 1
        i = 1
        while i <= n:
            if i % 2 != 0:
                y = x + n
                write_incr(x, y)
                print(end='\n')
            elif i % 2 == 0:
                y = x + n
                write_desc(x, y)
                print(end='\n')
            x = x + n
            i += 1


# EVNM()



class PlAYER:
    def reply(self, val):
        print(val)
        return input()

def playagain(variableslist, playerr):
    while True:

        if len(variableslist) < 4:
            for v in variableslist:
                s = playerr.reply(v)
                if s == 'E':
                    return v

        m = len(variableslist)

        lowerB = m // 3
        upperB = 2 * lowerB

        s1 = playerr.reply(variableslist[lowerB])

        if s1 == 'E':
            return variableslist[lowerB]

        s2 = playerr.reply(variableslist[upperB])

        if s2 == 'E':
            return variableslist[upperB]
        elif s1 == 'L' and s2 == 'L':
            variableslist = variableslist[:upperB]
            continue
        elif s1 == 'G' and s2 == 'G':
            variableslist = variableslist[lowerB + 1:]
            continue

        s3 = playerr.reply(variableslist[upperB])

        if s2 == 'L' and s3 == 'L':
            variableslist = variableslist[:upperB]
            continue
        elif s2 == 'G' and s3 == 'G':
            variableslist = variableslist[upperB + 1:]
            continue

        s4 = playerr.reply(variableslist[lowerB])

        if s3 == 'L' and s4 == 'L':
            variableslist = variableslist[:upperB]
        elif s3 == 'G' and s4 == 'G':
            variableslist = variableslist[lowerB + 1:]
        else:
            variableslist = variableslist[:lowerB] + variableslist[upperB + 1:]



def GUESSG():
    n = int(input())
    p = PlAYER()
    playagain(list(range(1, n + 1)), p)

GUESSG()