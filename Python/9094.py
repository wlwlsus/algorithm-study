import sys
r = sys.stdin.readline
t = int(r())
arr = [list(map(int, r().split())) for _ in range(t)]
for k in range(t):
    count = 0
    n, m = arr[k]
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if ((a * a) + (b * b) + m) % (a * b) == 0:
                count += 1
    print(count)
