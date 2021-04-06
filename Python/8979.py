import sys
r = sys.stdin.readline

n, k = map(int, r().split())
arr = [list(map(int, r().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 국가 번호 셋팅
for i in range(n):
    if arr[i][0] == k:
        temp = i

# 동점이 있다면 + 1 출력
for i in range(n):
    if arr[temp][1:] == arr[i][1:]:
        print(i + 1)
        break
