def Solution(n,m):
    sum = 0
    for i in range(N):
        sum += (ord(M[i])-96) * 31 ** i
    print(sum % 1234567891)
        
    


N = int(input())

M = input()

Solution(N,M)
    