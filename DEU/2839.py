def Solution(n):
    result = 0

    while True:
        if(n%5 == 0):
            result += n//5

            break

        n -= 3
        result += 1

        if(n<0):
            result = -1
            break

    return result

N = int(input())

print(Solution(N))





# N이 5의 배수일 때 n/5 봉지만큼 계산
# while문으로 3씩 감소하면서 3감소 1봉지 증가하여 계산
# 3감소 중 음수 될 경우 -1 출력
