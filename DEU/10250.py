def Solution(H, W, N):
    width = N // H + 1
    height = N % H

    if(height == 0):
        height = H 
        width -= 1

    print((height*100)+width)

N = int(input())
    
for _ in range(N):
    H, W, N = map(int, input().split())
    Solution(H, W, N)