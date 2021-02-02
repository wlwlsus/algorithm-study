N = int(input())

def rsp():
    cnt = int(input())
    li = list(list(input()) for _ in range(cnt))

    for i in range(len(li[0])):
        temp = []
        for j in range(len(li)):
            # print(f'{i}번째{li[j][i]}')
            temp.append(li[j][i])
        print(f'{i}번 째 비교 : {temp}')
        
        if("P" not in temp):
            # S 날림
            print("S 없음")
        elif("R" not in temp ):
            # P 날림
            print("R 없음")

        elif("P" not in temp):
            print("P 없음")
        else:
            print("무승부")

for _ in range(N):
    rsp()


# ===
# R > S -> P 없으면
# S > P -> R
# P > R -> S