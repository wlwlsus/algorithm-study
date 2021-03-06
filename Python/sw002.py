def main():
    dict = {}
    for i in range(1, p + 1):
        dict[i] = 0
    for _ in range(n):
        pc, time = map(int, input().split())

        if h > time:
            dict[pc] += time * 1000

    for i in range(1, p + 1):
        print(i, dict[i])


if __name__ == "__main__":
    p, n, h = map(int, input().split())
    main()