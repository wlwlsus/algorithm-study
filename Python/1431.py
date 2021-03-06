n = int(input())
guitar = [input() for _ in range(n)]


def sum_num(num):
    total = 0
    for i in num:
        if i.isdigit():
            total += int(i)
    return total


# 길이, 숫자의 합, 사전 순
guitar.sort(key=lambda x: (len(x), sum_num(x), x))

for x in guitar:
    print(x)
