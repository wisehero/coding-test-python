# a = 교환에 필요한 빈 병의 개수
# b = 교환 후 받을 수 있는 음료수의 개수
# n = 현재 가지고 있는 빈 병의 개수

def solution(a, b, n):
    answer = 0

    while n >= a:
        exchange = (n // a) * b
        answer += exchange
        n = n % a + exchange
    return answer