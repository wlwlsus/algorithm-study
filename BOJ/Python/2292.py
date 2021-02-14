n= int(input())
cnt=1;i=1;s=1
while s<n:
    s+=6*i
    i+=1
    cnt+=1
print(cnt)