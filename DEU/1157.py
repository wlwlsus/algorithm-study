N = input().upper() # 대문자 변환

def solution(s):
    li = [] 
    for i in set(s):        #리스트를 set으로 묶어서 중복값 제거
        li.append(s.count(i))   #리스트에 담아준다.

    idx = [i for i,x in enumerate(li) if x == max(li)] #리스트 중 제일 높은 값을 리스트 담는다 -> 중복 최대 확인

    if len(idx)>1 : #idx > 2 , 중복 최대 2개 이상 이면 ? 츨력
        print("?")
    else:
        print(list(set(s))[li.index(max(li))]) #set s를 리스트로 묶고 최대값 인덱스 위치에 있는 값을 출력

solution(N)