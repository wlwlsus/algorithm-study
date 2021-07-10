card = int(input())
card_list = [i for i in range(1, card + 1)]
drop = []

while len(card_list) != 1:
    drop.append(card_list.pop(0))
    card_list.append(card_list.pop(0))

print(*drop + card_list)