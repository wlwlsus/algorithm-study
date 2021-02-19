n=int(input())
m=list(map(int,input().split()))
k=n
# k편의 인용 횟수가 k번 이상일 때 최대 값을 구하기 위해 정렬
m.sort()
while k>0:
    #n-k편 인용 횟수에서 k번 이하를 찾다가 k번 이상을 찾으면 break 걸로 k 출력
    if m[n-k]>=k:
        break
    k-=1
print(k) 