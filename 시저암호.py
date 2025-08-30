def solution(s, n):
    answer = ''
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'

    for i in s:
        if i in alphabet_upper:
            index = alphabet_upper.index(i)
            new_index = (index + n) % 26
            answer += alphabet_upper[new_index]
        if i in alphabet_lower:
            index = alphabet_lower.index(i)
            new_index = (index + n) % 26
            answer += alphabet_lower[new_index]
        if i == ' ':
            answer += ' '
    

    return answer

print(solution("AB", 1)) # "BC"