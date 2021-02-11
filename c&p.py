# 조합
def combinations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations(arr[i+1:],r-1):
                yield [arr[i]] + next

# 중복 조합
def combinations_with_replacement(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combinations_with_replacement(arr[i:],r-1):
                yield [arr[i]] + next

# 순열
def permutations(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in permutations(arr[:i]+arr[i+1:],r-1):
                print(f'arr의 상태 : {arr[i]}, next의 상태 : {next}')
                yield [arr[i]] + next

# 중복 순열
def product(arr,r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in product(arr+1,r-1):
                yield [arr[i]] + next

for combi in permutations([1,2,3,4],2):
    print(combi)