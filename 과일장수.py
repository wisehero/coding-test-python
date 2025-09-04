def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    start = 0
    end = m
   
    while end <= len(score):
        answer += score[start:end][-1] * m 
        
        start += m
        end += m
    
    return answer