import sys

r = sys.stdin.readline
case = int(r())

for i in range(case):
    info = int(r())
    arr = [list(map(int, r().split())) for x in range(info)]

