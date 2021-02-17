# n=input()
# s=0
# for i in n:
#     if i in "ABC":
#         s+=2
#     elif i in "DEF":
#         s+=3
#     elif i in "GHI":
#         s+=4
#     elif i in "JKL":
#         s+=5
#     elif i in "MNO":
#         s+=6
#     elif i in "PQRS":
#         s+=7
#     elif i in "TUV":
#         s+=8
#     elif i in "WXYZ":
#         s+=9
# s+=len(n)
# print(s)

B='22233344455566677778889999'
s=0

a=input()

for i in a:
   s+=(int(B[ord(i)-65])+1)
print(s)