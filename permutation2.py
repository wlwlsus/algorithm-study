def dfs(L):
    # 종료조건
    if L==m:
        print(*result)
    else:
        for i in range(len(n)):
            if checklist[i]==0:
                result[L]=n[i]
                checklist[i]=1
                dfs(L+1)
                checklist[i]=0
    

if __name__ == "__main__" :
    n,m=map(int,input().split())
    n= list(range(1,n+1))

    result=[0]*m
    checklist = [0] * len(n)

    dfs(0)