def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    left_position = 10
    right_position = 10

    for num in numbers:
        if num in left:
            answer += "L"
            left_position = num
        elif num in right:
            answer += "R"
            right_position = num
        else:
            dist_L = abs(num - left_position)
            dist_R = abs(num - right_position)

            if dist_L > dist_R:
                answer += "R"
                right_position = num

            elif dist_R > dist_L:
                answer += "L"
                left_position = num
            else:
                if hand == "right":
                    answer += "R"
                    right_position = num
                else:
                    answer += "L"
                    left_position = num

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
