def solution(s):
    answer = ''
    is_first = True
    for c in s:
        if c == ' ':
            answer += c
            is_first = True
        else:
            if is_first:
                answer += c.upper()
                is_first = False
            else:
                answer += c.lower()
    return answer