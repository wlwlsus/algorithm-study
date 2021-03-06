def add_lesson():
    # 블루레이 개수
    count = 0
    total = 0
    for i in range(n):
        if total + lesson[i] > mid:
            count += 1
            total = 0
        total += lesson[i]

    else:
        if total:
            count += 1
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    lesson = list(map(int, input().split()))

    left = max(lesson)
    right = sum(lesson)

    while left <= right:
        mid = (left + right) // 2
        # 중앙 값을 기준으로 레슨의 합 -> 블루레이 개수를 구한다.
        cnt = add_lesson()

        # 블루레이 개수가 적으면 mid 값을 줄이고
        if cnt <= m:
            right = mid - 1
        # 블루레이 개수가 많으면 mid 값을 늘려준다
        elif cnt > m:
            left = mid + 1

    print(left)
