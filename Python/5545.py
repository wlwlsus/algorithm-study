#Greedy 
N = int(input())
dough_price, topping_price = map(int,input().split())
dough_calorie = int(input())

topping_calorie_list = []

for i in range(N):
    topping_calorie_list.append(int(input()))

# 토핑 칼로리 리스트, 내림차순 정렬
topping_calorie_list.sort(reverse=True)

# 토핑이 추가되지 않은 상태, 도우만 있는 상태 설정
base_price = dough_price
base_calorie = dough_calorie
per_calorie = dough_calorie / dough_price

# for문을 돌며 토핑, 가격 추가 -> 1원당 열량 계산 후 이전과 비교
for i in range(N):
    base_price += topping_price
    base_calorie += topping_calorie_list[i]
    value =  base_calorie / base_price

    # 열량(value)가 내려가면 이전 값이 MAX 이므로 break
    if(per_calorie > value) :
        break
    else :
        per_calorie = value
    
print(int(per_calorie))