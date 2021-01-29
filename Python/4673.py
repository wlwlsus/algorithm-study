def solve(n):
    result = n
    t= list(str(n))
    for i in t:
        result += int(i)

    return result

li = []
for j in range(10000):
    li.append(solve(j))

li.sort()

for k in range(10000):
    if(k in li):
        continue
    else:
        print(k)
