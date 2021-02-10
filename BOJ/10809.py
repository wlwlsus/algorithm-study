m=[-1]*26
u = list(input())
for i in range(len(u)):
    idx=ord(u[i])-97
    if(m[idx] == -1):
        m[idx] = i
print(*m)