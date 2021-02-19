import sys
def binary_search(_list, _target, low, high):
    if low > high:
        return False

    mid = (low+high)//2
    if _list[mid]>_target:
        return binary_search(_list,_target,low,mid-1)
    elif _list[mid]<_target:
        return binary_search(_list,_target,mid+1,high)
    else:
        # Middle == _Target
        return True


n=int(sys.stdin.readline())
m=sorted(list(map(int,sys.stdin.readline().split())))
x=int(sys.stdin.readline())
y=list(map(int,sys.stdin.readline().split()))

for i in y:
    if binary_search(m,i,0,n-1):
        print(1)
    else:
        print(0)

#시간초과 python3

# def BinarySearch(arr, val, low, high):
#     if low > high:
#         return False
    
#     mid = (low + high) // 2
#     if arr[mid] > val:
#         return BinarySearch(arr, val, low, mid - 1)
#     elif arr[mid] < val:
#         return BinarySearch(arr, val, mid + 1, high)
#     else:
#         return True

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# M_list = list(map(int, input().split()))
# A = sorted(A)     

# for m in M_list:
#     if BinarySearch(A, m, 0, N-1):
#         print(1)
#     else:
#         print(0)