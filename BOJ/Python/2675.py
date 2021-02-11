def print_word(r,w):
    for i in list(w):
        print(i*int(r), end='')
    print()

n=int(input())
for _ in range(n):
    repeat, word = map(str,input().split())
    print_word(repeat, word)