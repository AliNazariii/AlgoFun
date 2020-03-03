n = int(input())

res = 0
i = 1
while i * i <= n:
    if i * i == n: 
        res += 1
    elif n % i == 0:
        res += 2
    i += 1

print(res)
