n=input().split('-')
num=[]

for i in n:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)

# '-'로 분리해준 식을 모두 연산해준다.
# 제일 처음 수 를 m 에 대입
m=num[0]
# 1부터 num리스트 끝까지 돌며 - 연산 진행
for i in range(1, len(num)):
    m-=num[i]
# 최소값 출력
print(m)