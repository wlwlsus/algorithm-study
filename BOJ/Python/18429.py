import sys
from itertools import permutations

kit, cal = map(int,input().split())
inc = list(map(int,input().split()))
c = 0

#[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
for i in permutations(inc, kit):
    weight = 500
    flag = True
    for j in range(kit):
        weight += i[j]
        weight -= cal

        if weight < 500:
            flag = False
            break

    if flag:
        c += 1

print(c)

# def solve(k):
#     if(k)
#     global c

#     for i in range(k):
#         if(weight+inc[i]-cal <= 500):
#             continue
#     c += 1
#     solve(k-1)


# solve(kit)
# print(c)

