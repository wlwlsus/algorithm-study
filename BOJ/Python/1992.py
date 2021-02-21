n=int(input())
matrix=[list(map(int,input().rstrip())) for _ in range(n)]

def quad(x,y,n):    
    point = matrix[x][y]

    global res
    for i in range(x,x+n):
        for j in range(y,y+n):
            if matrix[i][j] != point:
                print('(', end='')

                quad(x,y,n//2)
                quad(x,y+n//2,n//2)
                quad(x+n//2,y,n//2)
                quad(x+n//2,y+n//2,n//2)
                print(')', end='')
                return
    if point == 0:
        print('0',end='')
        return
    else:
        print('1',end='')
        return

res=""
quad(0,0,n)
print(res)
