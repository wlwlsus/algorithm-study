M = int(input())
N = list(map(int, input().split()))

avg = []
for i in N:
    avg.append(i/max(N)*100)
    
print(sum(avg)/len(avg))