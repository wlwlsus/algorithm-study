a=[]
for i in range(9):
    a.append(int(input()))
res=sum(a)
a.sort()
for i in range(9):
    for j in range(i+1,9):
        if res-a[i]-a[j]==100:
            for k in range(9):
                if k==i or k==j:continue
                else:
                    print(a[k])
            exit()