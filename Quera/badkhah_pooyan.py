p, d = map(int, input().split())

while True:
    if d % p <= p / 2:
        print(d)
        break
    else:
        d += d
