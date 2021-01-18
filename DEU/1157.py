N = input().upper() # 대문자 변환

def solution(s):
    li = [] 
    for i in set(s):
        li.append(s.count(i))

    idx = [i for i,x in enumerate(li) if x == max(li)]

    if len(idx)>1 :
        print("?")
    else:
        print(list(set(s))[li.index(max(li))])

solution(N)