import math
def find_zero(num):
    count = 0
    i = 5
    while (num / i >= 1):
        count += int(num / i)
        i *= 5

    return int(count)

num = 20
print(math.factorial(num))
print(find_zero(num))
