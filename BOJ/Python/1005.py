for i in range(int(input())):
    x=int(input());y=int(input())
    s=[j for j in range(1,y+1)]

    for k in range(x):
        for n in range(1,y):
            s[n] += s[n-1]
    print(s[-1])