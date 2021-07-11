# 라인 스위핑
# 1. s, n을 tuple list로 생성
# 2. sort
# 3. s<= ns&ne <= e(한 선이 다른 선 안에 포함)과 ns<e(중첩) 등 중복된 선 길이 제거
# 4. 합
import sys

r = sys.stdin.readline
n = int(r())

arr = [tuple(map(int, r().split())) for i in range(n)]
arr.sort()

ans = 0
ns = ne = 0

for s, e in arr:
    if not ans:
        ans = abs(e - s)
        ns = s
        ne = e
        continue

    if ns <= s and ne >= e:
        continue

    ans += abs(e - s)

    if ne > s:
        ans -= abs(ne - s)

    ns = s
    ne = e

print(ans)
