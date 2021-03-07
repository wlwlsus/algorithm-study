import sys
r = sys.stdin.readline

n, c = map(int, r().split())
m = int(sys.stdin.readline())
box = [list(map(int, r().split())) for _ in range(m)]
# 1. 받는 마을 기준으로 오름차순 정렬 - 보내는 사람 기준 정렬 시 1번째 마을에서 최대 용량을 실을 때 반례가 존재.
box.sort(key=lambda k: k[1])

# 2. 받는 마을 기준 정렬 시 보내는 마을 순서가 꼬인다.
#    -> 각 마을의 최대 용량을 설정하고 마을 방문 시 용량에서 택배 개수만큼 차감해준다.
ans = 0
vol = [c] * n

for i in range(m):
    start, end, parcelCount = box[i]
    maxLimit = c
    # 보내는 마을, 받는 마을을 돌며 보낼 수 있는 최대 한도를 구한다.
    for j in range(start, end):
        maxLimit = min(maxLimit, vol[j])
    # 음수를 피하기 위해 최대 한도와 택배 개수를 비교하여 최솟 값으로 마을 마다 택배 개수를 차감한다. 
    maxLimit = min(maxLimit, parcelCount)
    for j in range(start, end):
        vol[j] -= maxLimit
    # 배송 완료된 택배
    ans += maxLimit
print(ans)