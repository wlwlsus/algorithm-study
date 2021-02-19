#정방향
target = 25
m = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m)
m.sort()
print(m)
left = 0
right = length-1

while left <= right:
    mid = (left+right)//2
    if m[mid]==target:
        print(mid+1)
        break
    elif m[mid]>target:
        right=mid-1
    else:
        left=mid+1

