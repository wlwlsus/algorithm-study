n=int(input())
for _ in range(n):
    case = list(input())
    sum = 0
    count = 0
    for i in case:
        if(i=='O'):
            count += 1
            sum += count
        else:
            count = 0
        
    print(sum)