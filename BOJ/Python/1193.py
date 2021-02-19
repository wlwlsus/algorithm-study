x = int(input())

line = 0
num = 0

while num < x:
    line += 1
    num += line

num -= line

if line % 2 == 0:
    i = x - num
    j = line - i + 1
else:
    i = line - (x - num) + 1
    j = x - num

print(f"{i}/{j}")