import sys
n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

#대각선 loop
for i in range(1, n):
    #i번째 대각선의 j번째 열
    for j in range(n-i):
        #i==1 , AB, BC, ... 차이가 1
        if i == 1:
            dp[j][j+i] = m[j][0]*m[j][1]*m[j+i][1]
            continue

        #최대값 설정
        dp[j][j+i] = 2**31
        for k in range(j, j+i):
            #행렬연쇄곱셈 점화식, 이전 단계 부분 문제에서 현재 문제를 푸는 k가지 방법 비교
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + m[j][0]*m[k][1]*m[j+i][1])
print(dp[0][n-1])