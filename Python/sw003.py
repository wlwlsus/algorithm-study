def main(peanut, start):
    food = list(map(int, input().split()))
    red = 0
    while peanut:
        dist = []
        for i in food:
            t = abs(start - i)
            dist.append(t)


        red += min(dist)
        start = food[dist.index(min(dist))]
        peanut -= 1
    return red

if __name__ == "__main__":
    n, m, e = map(int, input().split())
    print(main(m,e))