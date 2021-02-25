n = int(input())
r=list(map(int, input().split()))
city=list(map(int, input().split()))
price=city[0]; total=0
for i in range(n-1):
    if price > city[i]:
        price = city[i]
    total += price*r[i]

print(total)