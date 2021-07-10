a, b, c, d, e, f = map(int, input().split())

# 전체 범위 -999 ~ 1000
for i in range(-999, 1000):
    for j in range(-999, 1000):
        # ax + by = c and dx + ey = f에 해당하는 값(x,y)만 출력
        if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
            print(i, j)
