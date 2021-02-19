for _ in range(int(input())):
    a,b=map(int,input().split())
    distance=b-a
    count=0
    move=1
    totalMove=0
    while totalMove<distance:
        count +=1
        totalMove+=move
        if count %2==0:
            move+=1
    print(count)