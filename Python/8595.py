n = int(input())
word = list(input())
num = []
temp = ''
for i in word:
    if not i.isalpha():
        temp += i
    else:
        if not temp == '':
            num.append(int(temp))
        temp = ''
if not temp == '':
    num.append(int(temp))

print(sum(num))
