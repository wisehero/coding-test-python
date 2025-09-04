def solution(cards1, cards2, goal):
    answer = ''
    
    cards1_idx = 0
    cards2_idx = 0
    for element in goal:    
        
        if element == cards1[min(len(cards1)-1,cards1_idx)]:
            cards1_idx += 1
            continue
            
        
        if element == cards2[min(len(cards2)-1,cards2_idx)]:
            cards2_idx += 1
            continue
    if cards1_idx + cards2_idx == len(goal):
        answer = "Yes"
    else:
        answer = "No"
    return answer