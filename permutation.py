# def permutation(arr, r):
#     # 1.
#     arr = sorted(arr)
#     used = [0 for _ in range(len(arr))]

#     def generate(chosen, used):
#         # 2.
#         if len(chosen) == r:
#             print(chosen)
#             return
	
# 	# 3.
#         for i in range(len(arr)):
#             if not used[i]:
#                 chosen.append(arr[i])
#                 used[i] = 1
#                 generate(chosen, used)
#                 used[i] = 0
#                 chosen.pop()
#     generate([], used)

# permutation(range(1,3+1),2)

def generator():
    for i in range(10):
        yield i**i

for k in generator():
    print(k)