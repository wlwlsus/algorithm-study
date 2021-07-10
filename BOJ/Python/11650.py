# import sys
#
# n = int(sys.stdin.readline())
#
# so = []
#
# # Receive input in list form.
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))
#
# so.sort(key = lambda x: (x[0], x[1]))
#
# # 람다를 통해 정렬 기준을 정한다.
# for i in so:
#     print(i[0], i[1])
#

import sys

r = sys.stdin.readline
n = int(r())

arr = [list(map(int, r().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))

for i in arr:
    print(*i)
