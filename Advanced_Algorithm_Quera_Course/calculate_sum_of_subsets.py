n = int(input())
subsets = input().split(" ")
result = 0

for i in range(n):
    result += int(subsets[i])

print((pow(2, n - 1) * result) % (pow(10, 9) + 7))
