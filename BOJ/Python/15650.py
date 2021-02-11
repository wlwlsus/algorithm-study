# from itertools import combinations as p
# n,m=map(int,input().split())
# for i in p(range(1,n+1),m):
#     print(*i)
## 제너레이터를 이용해서 조합 구현 (중복 조합 X)
def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next


print("\n\ncombinations 직접 구현")
for i in combinations_2([1,2,3,4], 3):
    print(i, end=" ")
