arr = map(int, input().split())

n = 0
for i in arr:
    n += i ** 2

print(n%10)