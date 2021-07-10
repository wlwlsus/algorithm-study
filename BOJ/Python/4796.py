count = 0
while True:
    count += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break

    q = (v // p * l)
    r = v % p
    answer = min(r, l)
    print(f'Case {count}: {q + answer}')
