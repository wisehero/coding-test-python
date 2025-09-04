def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    answer += '0'
    answer += answer[::-1][1:]
    return answer


print(solution([1, 3, 4, 6])) # "1223330333221"

