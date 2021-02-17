n=int(input())
m=list(map(int,input().split()))
s=0
for i in m:              # 리스트를 순차적으로 순환        
    count = 0                   # 소수는 1과 자기자신으로만 나뉘는수 (수를 세기위한 count)        
    for j in range(1,i+1):      # 1부터 리스트의 수까지 진행            
        if i % j == 0:          # i가 j로 나누어 진다면                
            count += 1          # 나뉘는수 +1 증가        
    if count == 2:              # 나뉘는수가 2개다 = 소수            
        s += 1                # 리스트의 i항은 소수이다.
print(s)