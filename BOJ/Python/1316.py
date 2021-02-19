# cnt=0
# for _ in range(int(input())):
#     w={}
#     idx=""
#     word=input()
#     if len(word)==word.count(word[0]) and len(word)>2:
#         continue
#     for i in word:
#         if (i not in w)or idx==i:
#             w[i]=True
#         else:
#             w[i]=False
#         idx=i
#     if False not in list(w.values()):
#         cnt += 1
# print(cnt)

# n=int(input())
# cnt=0
# for i in range(n):
#     w=input()
#     for k in range(len(w)):
#         if k != len(w)-1:
#             if w[k]==w[k+1]:
#                 pass
#             elif w[k] in w[k+1:]:
#                 break
#         else:
#             cnt+=1
# print(cnt)

result = int(input())
for _ in range(result):
    word = input()
    for i in range(1, len(word)):
        if word.find(word[i-1]) > word.find(word[i]):
            result -= 1
            break
print(result)

"""
단어에서 두 글자씩을 비교하여 앞 글자가 처음 등장하는 인덱스보다 
뒷 글자가 처음 등장하는 인덱스가 더 작으면, 뒷 글자는 앞서 이미 등장한 글자가 됩니다.
"""