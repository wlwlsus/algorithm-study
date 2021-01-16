def solution(m,n):
    min = 0
    sum = 0
    count = 1
    num = count ** 2

    while num<=n:
        num = count ** 2
        if(m <= num <= n):
            if(sum == 0):
                min = num
            sum += num
        count += 1


    if (sum == 0):
        print(-1)
        return
    print(sum)
    print(min)


while True:
    M = int(input())
    N = int(input())
    if(M<=N):
        break

solution(M,N)