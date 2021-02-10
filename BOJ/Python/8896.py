N = int(input())

def rsp():
    c = int(input())
    #로봇 목숨
    robot = []
    # R, S, P 데이터 리스트
    w = []
    # 게임 진행 상황 리스트
    li = []
    #패배한 수 저장 str
    lose=""
    #초기화 - 로봇 목숨 할당, 게임 판 생성
    for _ in range(c):
        robot.append(True)
        li.append(input())

    k=len(li)

    for i in range(k):
        #입력받을 R, S, P 초기화
        for k in range(3): w=[0]*3

        for j in range(c):
            if(robot[j] != True): continue
            #게임 마다 R,S,P 체크
            #각각 0,1,2에 할당
            if(li[j][i]=="R"): w[0]=1
            elif(li[j][i]=="S"): w[1]=1
            elif(li[j][i]=="P"): w[2]=1

        #w의 합이 1,3이라면 하나 혹은 R,S,P 모두 있을 경우 -> 무승부
        #w의 합이 2라면 R,S,P 중 2개 -> 하나가 없으므로 승부가 갈린다.
        if(w[0]+w[1]+w[2]==2):
            #P가 없다면
            if(w[0]==0): lose='P'
            #R이 없다면
            elif(w[1]==0): lose='R'
            #S가 없다면
            elif(w[2]==0): lose='S'

            #lose에 할당된 패배 로봇을 탈락시킨다.
            for j in range(c):
                if(li[j][i]==lose):
                    robot[j] = False

    #남아있는 로봇의 수, 로봇의 번호 할당
    cnt = 0; result = 0
    for i in range(c):
        if(robot[i]):
            cnt +=1; result=i+1
    
    #로봇의 수가 1이 아니면 무승부 -> 0, 1이면 i 출력
    if(cnt!=1): result=0
    print(result)

for i in range(N):
    rsp()

# N = int(input())

# def rsp():
#     cnt = int(input())
#     li = list(list(input()) for _ in range(cnt))

#     for i in range(len(li[0])):
#         temp = []
#         for j in range(len(li)):
#             # print(f'{i}번째{li[j][i]}')
#             temp.append(li[j][i])
#         print(f'{i}번 째 비교 : {temp}')
        
#         if("P" not in temp):
#             # S 날림
#             print("S 없음")
#         elif("R" not in temp ):
#             # P 날림
#             print("R 없음")

#         elif("P" not in temp):
#             print("P 없음")
#         else:
#             print("무승부")

# for _ in range(N):
#     rsp()


# # ===
# # R > S -> P 없으면
# # S > P -> R
# # P > R -> S

