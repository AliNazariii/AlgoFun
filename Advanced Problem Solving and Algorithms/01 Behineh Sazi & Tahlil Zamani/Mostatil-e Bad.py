import math

n = int(input())
res = 0

for a in range(1, math.floor(n / 3) + 1):
    res += math.floor((n - 3*a) / 2) - max(0, math.floor(n/2) - 2*a + 1) + 1

print(int(res % (math.pow(10, 9) + 7)))
