import sys

#머리가 나빠서 몸이 고생한 문제
def tetromino(list):
    temp = []
    global N, M
    for i in range(N):
        for j in range(M-3): 
            temp.append(list[i][j] + list[i][j+1] + list[i][j+2] + list[i][j+3])        # ㅡ


    for i in range(N-1):
        for j in range(M-1): 
            temp.append(list[i][j] + list[i][j+1] + list[i+1][j] + list[i+1][j+1])      #ㅁ

        for j in range(M-2):    
            temp.append(list[i][j] + list[i+1][j] + list[i][j+1] + list[i][j+2])        #┌-
            temp.append(list[i][j] + list[i+1][j] + list[i+1][j+1] + list[i+1][j+2])    #ㄴ-
            temp.append(list[i][j] + list[i][j+1] + list[i][j+2] + list[i+1][j+2])      #-ㄱ
            temp.append(list[i][j] + list[i][j+1] + list[i+1][j+1] + list[i+1][j+2])    #ㄱ+ㄴ
            temp.append(list[i][j] + list[i][j+1] + list[i][j+2] + list[i+1][j+1])      #ㅜ


    for i in range(N-2):
        for j in range(M-1):
            temp.append(list[i][j] + list[i+1][j] + list[i+1][j+1] + list[i+2][j+1])    #세로 ㄴㄱ
            temp.append(list[i][j] + list[i+1][j] + list[i+2][j] + list[i+2][j+1])      #ㄴ
            temp.append(list[i][j] + list[i][j+1] + list[i+1][j+1] + list[i+2][j+1])    #ㄱ
            temp.append(list[i][j] + list[i+1][j] + list[i+2][j] + list[i][j+1])        #┌
            temp.append(list[i][j] + list[i+1][j] + list[i+2][j] + list[i+1][j+1])      #ㅏ


    for i in range(N-3):
        for j in range(M): 
            temp.append(list[i][j] + list[i+1][j] + list[i+2][j] + list[i+3][j])        #ㅣ


    for i in range(1, N):
        for j in range(M-2):
            temp.append(list[i][j] + list[i][j+1] + list[i][j+2] + list[i-1][j+2])      #-┘
            temp.append(list[i][j] + list[i][j+1] + list[i-1][j+1] + list[i-1][j+2])    #가로┘+┌
            temp.append(list[i][j] + list[i][j+1] + list[i-1][j+1] + list[i][j+2])      #ㅗ
            

    for i in range(2, N):
        for j in range(M-1):
            temp.append(list[i][j] + list[i][j+1] + list[i-1][j+1] + list[i-2][j+1])    #┘
            temp.append(list[i][j] + list[i-1][j] + list[i-1][j+1] + list[i-2][j+1])    #세로┘+┌

        for j in range(1, M):
            temp.append(list[i][j] + list[i-1][j] + list[i-1][j-1] + list[i-2][j])      #ㅓ
            
            
    return max(temp)



N, M = list(map(int,sys.stdin.readline().split()))
list1 = [list(map(int,sys.stdin.readline().split())) for _ in range (N)]

print(tetromino(list1))