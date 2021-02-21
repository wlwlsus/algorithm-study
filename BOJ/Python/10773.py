arr=[]
for _ in range(int(input())):
    n=int(input())
    if n==0 and len(arr)>0:
        arr.pop()
        continue
    arr.append(n)
print(sum(arr))