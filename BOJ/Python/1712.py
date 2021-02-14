x,y,z= map(int,input().split())
i=1;c=0
if i*(z-y)<=0:
    print(-1)
else:
    i = x//(z-y)
    print(i+1)