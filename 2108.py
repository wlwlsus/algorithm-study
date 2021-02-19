from collections import Counter
import sys
n=int(sys.stdin.readline())
m=[]
for i in range(n):
    m.append(int(sys.stdin.readline()))
m.sort()
print(round(sum(m)/len(m)))
print(m[len(m)//2])

k=Counter(m).most_common()
if len(m) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0]) 
    else : print(k[0][0]) 
else : print(m[0]) 
print(m[-1]-m[0])