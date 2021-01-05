N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

def Solution(data):
    height = data[0]
    width = data[1]
    seq = data[2]

    tempH = 1
    tempW = 1

    for i in range(height*width):
        
        print(tempH)
        seq -= 1
        if(tempH == height):
            tempH = 1
            tempW += 1

        if(seq == 0):
            print((tempH*100) + tempW)    
            return

for i in info:
    Solution(i)