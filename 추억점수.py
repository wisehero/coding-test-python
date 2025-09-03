def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    
    for p in photo:
        e = 0
        for pp in p:
            if pp in dic.keys():
                e += dic[pp]
        answer.append(e)
    
    return answer