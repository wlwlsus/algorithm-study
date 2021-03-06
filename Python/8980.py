import sys

r = sys.stdin.readline

n, c = map(int, r().split())
m = int(r())
arr = [list(map(int, r().split())) for _ in range(m)]
arr.sort(key=lambda x: x[0])
destination = {}
for i in range(2, n+1):
    destination[i] = 0
vol = 0
for i in range(len(arr)):
    k, y, z = arr[i]
    if k in destination:
        print("있음 ㄷㄷ", y )

    vol += z
    destination[y] += z

    # if (c - vol) > 0:
    #     if (vol + z) > c:
    #         vol += (c - z)
    #     else:
    #         vol += z
print(destination)
print(vol)