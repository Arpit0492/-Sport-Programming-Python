
def generateRandomNumbers(size):
    rangee = 1000000007
    multiplierOne = 2017
    multiplierSecond = 2027
    lastNumber = 0
    secondLastNumber = 1
    maxNumberGeneratedTillNow = 0
    ll = dict()
    for I in range(size):
        newNumber = (lastNumber * multiplierOne
                     + secondLastNumber * multiplierSecond + maxNumberGeneratedTillNow) % rangee + 1
        secondLastNumber = lastNumber
        lastNumber = newNumber
        if newNumber > maxNumberGeneratedTillNow:
            maxNumberGeneratedTillNow = newNumber
        ll[newNumber] = 1
    return ll


n, q = [int(x) for x in input().strip().split(' ')]

l = generateRandomNumbers(n)
# print(l)

for i in range(q):
    if int(input()) in l.keys():
        print('YES')
    else:
        print('NO')

