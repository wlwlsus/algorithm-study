def main(combo):
    for i in combo:
        for j in combo:
            if i[-1] == j[0]:
                result.append(i + [j[1]])

    return result


if __name__ == "__main__":
    skill = list(map(str, input().split()))
    skill_cnt = int(input())
    rel = [list(input().split()) for _ in range(skill_cnt)]
    result = []

    for x in main(rel):
        print(*x)
