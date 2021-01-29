import sys 
N = int(sys.stdin.readline())


def count_paper(x, y, N):
    global white, color
    point = paper[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if point != paper[i][j]:
                div = N//2

                count_paper(x,y,div)
                count_paper(x,y+div,div)
                count_paper(x+div,y,div)
                count_paper(x+div,y+div,div)
                return

    if point == 0:
        white += 1
    else :
        color += 1


paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
color = 0
count_paper(0,0,N)
print(white)
print(color)