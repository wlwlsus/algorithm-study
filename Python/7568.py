n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in arr:
    result = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            result += 1
    print(result, end=" ")
