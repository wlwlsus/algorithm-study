n = int(input())


def fibonacci(m):
    cache = [-1 for _ in range(m + 1)]

    def iterate(k):
        if k < 2:
            return k
        if cache[k] != -1:
            return cache[k]

        cache[k] = iterate(k - 1) + iterate(k - 2)
        return cache[k]

    return iterate(m)


arr = [0]
for i in range(1, 80 + 1):
    arr.append(fibonacci(i))

# 가장 큰 변의 값 4번, 이전 값 2번의 합
print(4 * arr[n] + 2 * arr[n - 1])
