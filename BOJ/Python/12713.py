from functools import lru_cache

M = 2*3*5*7
uglies = list(filter(lambda n: (int(n)%2 == 0 or
                                int(n)%3 == 0 or
                                int(n)%5 == 0 or
                                int(n)%7 == 0),
                     range(M)))

@lru_cache(maxsize=None)
def f(line, k=None):
    if k == None:
        return sum([f(line, k) for k in uglies])

    return sum([
        (1 if (int(line) % M) == k else 0),

        sum([f(line[:p],
               (k-int(line[p:])) % M)
             for p in range(1, len(line))]),

        sum([f(line[:p],
               (k+int(line[p:])) % M)
             for p in range(1, len(line))]),
        ])

if __name__ == '__main__':
    import sys
    data = sys.stdin.read().splitlines()[1:]
    case = 1
    for line in data:
        print('{:.0%}'.format(case/len(data)), file=sys.stderr)
        print('Case #{}: {}'.format(case,
                                    f(line)))
        case += 1
