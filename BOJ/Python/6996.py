for i in range(int(input())):
    a,b=map(str,input().split())
    x=list(a);y=list(b);x.sort();y.sort();
    if(x==y):print(f'{a} & {b} are anagrams.')
    else:print(f'{a} & {b} are NOT anagrams.')