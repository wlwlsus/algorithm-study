N = int(input())
temp_sum = N
count = 0

while True:
    var_a = N // 10
    var_b = N % 10
    t = var_a + var_b
    count+=1
    N = int(str(var_b) + str(t%10))
    if(N == temp_sum):
        break

print(count)