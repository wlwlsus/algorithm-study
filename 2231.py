n=int(input())
num=1
while num < n:
    if sum(list(map(int,str(num)))+[num])==n:
        break
    num+=1
if num < n:
    print(num)
else:
    print(0)