
def add_number(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


# print(add_number(9, 10))


# Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits
def narcissistic_number(number):
    digits_count = count_of_digits(number)
    sum = 0
    dup = number

    while dup > 0:
        sum += pow(dup % 10, digits_count)
        dup //= 10

    return sum == number


def count_of_digits(number):
    if number == 0:
        return 0
    return 1 + count_of_digits(number // 10)


# print(narcissistic_number(1634))
# print(narcissistic_number(1633))
