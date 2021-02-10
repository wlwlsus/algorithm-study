# 10546, 배부른 마라토너
import sys

N = int(sys.stdin.readline())

people = {}
for _ in range(2*N-1):
    name = sys.stdin.readline().rstrip()
    if people.get(name) is None:
        people[name] = 1
    else:
        del(people[name])

print(*people)