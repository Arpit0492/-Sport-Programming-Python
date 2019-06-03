

def already_has(num_list, num_check):
    for n in num_list:
        for dig in str(n):
            if dig in num_check:
                return True
    return False


def num_to_int(elem):
    return int(elem)


T = int(input())

for tc in range(T):
    N = int(input())
    num_str_list = input()
    numbers = sorted(num_str_list.split(' '), reverse=True, key=num_to_int)
    combs = []
    ans = 0
    for num_str in numbers:
        num = num_to_int(num_str)
        if len(combs) > 0:
            for comb in combs:
                if already_has(comb, num_str) is False:
                    newComb = []
                    newComb.extend(comb)
                    newComb.append(num)
                    combs.append(newComb)
        else:
            combs.append([])
            combs.append([num])

    for comb in combs:
        if len(comb) > 0:
            new_sum = sum(comb)
            if new_sum > ans:
                ans = new_sum

    print(ans)