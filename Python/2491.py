N = int(input())
li=list(map(int,input().split()))

cnt = 1
result = 1

#감소하는 지 확인 
for i in range(1,N):
    #이전과 비교, 이전이 작으면 +1 아니면 1로 초기화
    if(li[i-1]>=li[i]):
        cnt += 1
    else:
        cnt = 1

    #현재 카운터가 증가했는지 확인 후 갱신
    if(result < cnt):
        result = cnt

#증가 카운터 초기화
cnt = 1
#증가하는 지 확인 
for i in range(1,N):
    if(li[i-1]<=li[i]):
        cnt += 1
    else:
        cnt = 1

    if(result < cnt):
        result = cnt

print(result)

