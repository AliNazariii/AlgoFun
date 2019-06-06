n, m, k = map(int, input().split())
broken = [[0 for i in range(2)] for j in range(k)]
for i in range(k):
    broken[i][0], broken[i][1] = map(int, input().split())

if k > m * n:
    print("-1")
elif k == m * n and k % 2 == 0:
    print("-1")
elif k % 2 == 1:
    print("0")
else:
    print("1")
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not [i, j] in broken:
                print(i, j)
                exit()
