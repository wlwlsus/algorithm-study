N = int(input())

def rsp():
    cnt = int(input())
    li = list(list(input()) for _ in range(cnt))
    robot = [True for _ in range(1,cnt+1)]
    print(f'로봇 번호 : {robot}')

    for i in range(len(li[0])):

        temp = []
        for j in range(len(li)):
            # print(f'{i}번째{li[j][i]}')
            temp.append(li[j][i])
        print(f'{i}번 째 비교 : {temp}')
        
        if("S" not in temp):
            # S 날림
            print("S 없음")
            # R이 진다.
            # robot = [False if i=="R" else i for i in temp]

        elif("R" not in temp ):
            # P 날림
            print("R 없음")

        elif("P" not in temp):
            print("P 없음")
        else:
            print("무승부")
    
    print(robot)

for _ in range(N):
    rsp()


# ===
# R > S -> P 없으면
# S > P -> R
# P > R -> S