import sys


def factorial(n):
    if(n <= 1): #재귀 이므로 n 범위를 정해준다 .n 이 1 이하면 1을 반환 *1 *1 *1 ..
        return 1
    else:
        return n * factorial(n-1)

N = int(sys.stdin.readline())
print(factorial(N))