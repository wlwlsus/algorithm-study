a, b, c = map(int, input().split())
t = (a ** 2 / (b ** 2 + c ** 2)) ** 0.5
width, height = t * b, t * c
print(int(width), int(height))