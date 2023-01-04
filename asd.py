import math
import sys


def check_prime(num):
    if num == 1:
        return 0
    for k in range(2, int(math.sqrt(num)) + 1):
        if num % k == 0:
            return 0
    else:
        return 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    count = 0
    for j in range(n + 1, 2 * n + 1):
        count += check_prime(j)
    print(count)