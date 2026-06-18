import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = [0] * n
    cur = 1
    for i in range(0, n, 2):
        a[i] = cur
        cur += 2

    for i in range(1, n, 2):
        a[i] = cur
        cur += 2

    print(*a)
