def solution(s):
    stack = []

    for char in s:
        # 스택이 비어있지 않고, 스택의 마지막 문자와 현재 문자가 같으면 제거
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0