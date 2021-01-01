import sys 
#sys.setrecursionlimit(10**9) #재귀호출 횟수 셋팅

def count_paper(x, y, N):
    global minus, zero, one
    point = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if point != paper[i][j]:    #처음 좌표와 비교하며 다른 값이 있을 경우 (2)의거,9분할 진행
                div = N//3              # 9분할

                count_paper(x, y, div)           #좌측 상단
                count_paper(x+div, y, div)       #중앙 
                count_paper(x+(div*2), y, div)   #우측 

                count_paper(x, y+div, div)               #좌측 중앙
                count_paper(x+div, y+div, div)           #중앙 
                count_paper(x+(div*2), y+div, div)       #우측 

                count_paper(x, y+(div*2), div)             #좌측 하단
                count_paper(x+div, y+(div*2), div)         #중앙 
                count_paper(x+(div*2), y+(div*2), div)     #우측 
                
                return


    if point == -1:
        minus += 1
    elif point == 0 :
        zero += 1
    else:
        one += 1

N = int(sys.stdin.readline())


paper = [list(map(int, input().split())) for _ in range(N)]
minus = 0
zero = 0
one = 0

count_paper(0, 0, N)
print(minus)
print(zero)
print(one)
