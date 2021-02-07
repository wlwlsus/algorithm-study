n = int(input())

for _ in range(n):
    score = list(map(int,input().split()))
    avg = sum(score[1:])/(score[0])
    s = 0
    for i in score[1:]:
        if(i>avg):
            s+= 1

    print(f'{format(s/(score[0])*100,".3f")}%')