a, b = map(int, input().split())


def permutation(n, m):
    ans = 1
    for i in range(m):
        ans *= n - i

    return ans


print(permutation(a, b) // permutation(b, b))
