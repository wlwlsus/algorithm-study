n = int(input())
m = sorted(list(map(int, input().split())))
t = int(input())
ans = 0
left, right = 0, n-1
# 같은 자리 두개를 더할 수 없다.
while left < right:
    temp = m[left] + m[right]
    if temp > t:
        right -= 1
    elif temp < t:
        left += 1
    else:
        ans += 1
        left += 1
        right -= 1

print(ans)