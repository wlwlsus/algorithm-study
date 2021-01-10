def Solution(L,M):
    temp_list = []
    temp = M - 1
    i = 0

    while len(L):
        i = (i+temp) % len(L)
        temp_list.append(L.pop(i))

    return temp_list


N, M = map(int,input().split())

solve_list = [ i for i in range(1,N+1)]

result = Solution(solve_list,M)

print("<"+', '.join(map(str,result)) + ">")

# 1 2 3 4 5 6 7