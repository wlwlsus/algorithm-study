def solution(w,e):
    site = 1
    if w != e:
        #29부터 13까지 1씩 감소하면서 곱셈
        for i in range(e, e-w, -1):
            print(site)
            site *= i
        #겹침선 제거를 위해 13부터 1까지 나누기..
        for i in range(w, 1, -1):
            print(site)
            site //= i
    print(site)


T = int(input())
M = [list(map(int,input().split())) for _ in range(T)]

for i in M:
    west = i[0]
    east = i[1]

    solution(west,east)