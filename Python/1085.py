x,y,w,h = map(int, input().split())
print(min(x,y,w-x,h-y))
"""
1. x : y축에서 (x,y) 까지 길이
2. y : x축에서 (x,y) 까지 길이
3. w-x : (x,y)에서 우측 y축까지 평행하는 길이
4. h-y : (x,y)에서 위 경계선까지 길이
"""