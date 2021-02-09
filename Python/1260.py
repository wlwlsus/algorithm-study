from collections import deque

n,m,v=map(int,input().split())
s = [[0] * (n + 1) for i in range(n + 1)]
visit = [0 for i in range(n + 1)]

for i in range(m):
    x,y = map(int,input().split())
    s[x][y]=1
    s[y][x]=1

"""
예제1)의 매트릭스 상태
[[0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1],
 [0, 1, 0, 0, 1],
 [0, 1, 0, 0, 1],
 [0, 1, 1, 1, 0]]  1-2 1-3 1-4 2-4 3-4 양방향
"""

#한 노드만 계속 파고 들어간다.
#dfs 호출 시 root 를 설정하고 for문을 돌면서 노드 하나하나 를 재귀로 검색한다. 
#if visit 으로 방문을 체크하고 해당 노드가 '1'일때 방문(재귀호출 ) -> 끝까지 돌았을 때 리스트 반환
def dfs(root):
    #재귀로 호출된 root 출력
    print(root, end=' ')
    #방문한 root는 체크 표시
    visit[root]=1
    for i in range(1,n+1):
        #for문 돌면서 방문안한 root가 있으면 재귀 호출!
        if visit[i]==0 and s[root][i]==1:
            dfs(i)

def bfs(root):
    node_list=[]
    #1.  deque 를 선언한다.
    #2. 시작 루트를 삽입한다.
    d=deque([root])
    #시작 노드도 방문했다는 표시를 남겨주자.
    visit[root]=0

    #while문으로 큐가 소진될 때 까지 반복한다
    while d:
        #반한된 노드를 출력한다. 노드리스트에 추가한다.
        root=d.popleft()
        node_list.append(root)
        
        #pop과 동시에 expand가 이루어져야 하므로 자식노드가 방문한 적이 있는지, 초기화 때 설정해둔 '1'에 해당하는지 확인
        # ??: 왜 1부터 n+1의 범위를 설정해야하는지?
        # -> 아마,, 처음 배열 선언할 때 1 ~ n+1 범위로 설정했기 때문에 트리의 모든 경로를 탐색하기 위해서 이렇게 설정해뒀을 거라 생각한다.
        for i in range(1, n+1):
            # 왜 visit은 s와 다르게 왜 1차원 배열인지? s[root][]에서 왜 s의 1차원배열은 root로 설정해둔건지?
            # -> s[root]는 시작 노드를 기준으로 탐색이 이루어지기 때문에 root가 고정인 듯하다. : 틀림
            # -> root는 고정이 아니다. pop 해주면서 root를 변경해주고 변경된 root를 기준으로 자식 노드를 검사한다.
            # 그러므로 root로 인해 뽑아낸 노드를 list에 넣어줘야 하는 것..
            # -> visit이 1차원 배열인 이유는 s[root][i]에서 i번째 배열이 방문되었는가 판단하기 위한 것 이므로 1차원이 아닐까?\
            if visit[i]==1 and s[root][i]==1:
                # 노드를 추가해주며 방문했다는 체크 표시를 남긴다.
                d.append(i)
                visit[i]=0

    return node_list
    
dfs(v)
print()
print(*bfs(v))