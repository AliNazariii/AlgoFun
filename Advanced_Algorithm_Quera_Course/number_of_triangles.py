def method_1():
    result = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if (i + j > k) and (k >= j):
                    result += 1
    return result


def method_2():
    result = 0
    for i in range(n):
        for j in range(i, n):
            if (i + j > n - i - j) and (n - i - j >= j):
                result += 1
    return result


def method_3():
    result = 0
    for i in range(int(n / 3)):
        result += (int((n - 3 * i) / 2) - max(0, int(n / 2) - 2 * i + 1)) + 1
    return result + 1


n = int(input())
print(method_3() % (pow(10, 9) + 7))
