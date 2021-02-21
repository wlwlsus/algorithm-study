#유망성 검사
def promissing(cdx):
    # 같은 열, 대각선상에 있다면 제외
    for i in range(cdx):
        # "==" 같은 열이라면 안되고, "cdx-i행과 abs(~)연산 열"이 일치하면 대각선상이 있다고 판단한다.
        if board[cdx]==board[i] or cdx -i == abs(board[cdx] - board[i]):
            return False
    return True

# 백트래킹 def
def n_queen(cdx):
    global cnt
    # cdx가 마지막 행까지 수행하고 여기까지 오면, 찾기 완료
    if cdx == n:
        cnt += 1
        return
    else:
        for i in range(n):
            #cdx번째 행, i번째 열에 queen을 놓아본다.
            board[cdx]=i
            
            #백트랙킹은 이 단계를 건너뛴다.
            #이후 그 행에 둔 것에 대한 유망성을 판단한다.
            if promissing(cdx): # 그 자리가 유망하다면,
                # 그 다음행에 대해 퀸을 놓는다.
                n_queen(cdx+1)

n=int(input())
cnt =0
board=[0]*15
n_queen(0)
print(cnt)