N = int(input())
#LL 을 L 로 치환, 문자열 기준으로 컵홀더 카운팅
t = input().replace("LL","L")
# 컵홀더 + 1로  양 옆의 컵홀더 개수 파악
holder = len(t)+1

# 컵홀더 보다 사람이 많거나 같으면 최대 컵홀더 개수 만큼 사용 가능
if(N>=holder): print(holder)
# 컵홀더가 많으면 최대 사람 수 만큼 사용 가능
else:print(N)