n, m = map(int, input().split())

rules = []
for i in range(m):
    temp_array = list(map(int, input().split()))
    rules.append(temp_array)

for i in range(m):
    for j in range(i + 1, m):
        a = max(rules[i][0], rules[j][0])
        b = min(rules[i][1], rules[j][1])
        if b > a and rules[i][2] != rules[j][2] and b - a != 0:
            print("-1")
            print(rules[i][0], rules[i][1], rules[j][0], rules[j][1])
            exit(0)

result = []
temp = 0
for i in range(n):
    if i == 0:
        result.append(i)
    else:
        for j in range(m):
            if (i + 1) <= rules[j][1] and (i + 1) > rules[j][0]:
                if rules[j][2] == 1:
                    temp += 1
                else:
                    temp -= 1
                result.append(temp)
                break
            elif (j + 1) == m:
                result.append(temp)

offset = 0
if min(result) < 1:
    offset = 1 - min(result)

for i in range(n):
    result[i] += offset

print(*result)