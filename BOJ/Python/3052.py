temp_list = []

for _ in range(10):
    data = int(input())

    value = data % 42
    if(value not in temp_list):
        temp_list.append(value)

print(len(temp_list))