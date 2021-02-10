# from collections import deque
# import sys
# # sys.stdout.write(str(1)+'\n')

# d=deque([1,2,3])
# d.append(4)
# d.appendleft(0)
# # print(d.pop())
# print(d)
# d.rotate(-1)
# print(d)
# # d.reverse()
# print(d[0])

# # d.extend(map(int,sys.stdin.readline().split()))

# # for i in range(10):
# #     for j in range(10):
# #         print(i, j)

# import heapq

# h = []
# heapq.heappush(h, 3)	# 첫 번째 파라미터에는 list 객체가
# heapq.heappush(h, 9)	# 두 번째 파라미터에는 삽입하려는 객체가 들어간다.
# heapq.heappush(h, 7)
# heapq.heappush(h, 8)
# heapq.heappush(h, 5)
# heapq.heappush(h, 1)

# # heapq.heappop(h)
# for _ in range(5):
# 	print(f'+:{---heapq.heappop(h)}')	# 작은 값부터 출력된다.


import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1