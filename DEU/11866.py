def Solution(L,M):
    count = len(L)
    temp_list = []
    
    while count != 0:
        L = rotate(L,M-1)
        temp_list.append(L[0])
        del L[0]
        count -= 1
    return temp_list

def rotate(l, n):
    return l[n:] + l[:n]

N, M = map(int,input().split())

solve_list = [ i for i in range(1,N+1)]

result = Solution(solve_list,M)

print("<", end = '')
print(', '.join(map(str,result)), end = '')
print(">")

# 1 2 3 4 5 6 7