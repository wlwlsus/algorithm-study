# 기본 재귀
def fibo(n):
    if n>=2:
        print(f'피보 진행 상황 : {n}')
        return fibo(n-1)+fibo(n-2)
    else: 
        return n

k=int(input())
for n in range(1,k+1):
    print(n, fibo(n))