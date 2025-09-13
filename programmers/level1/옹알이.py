def solution(babbling):
    """
    문자열 치환을 이용한 방법
    연속된 같은 발음을 먼저 체크한 후, 유효한 발음들을 제거해서 빈 문자열이 되는지 확인
    """
    count = 0
    
    for word in babbling:
        # 연속된 같은 발음이 있는지 체크
        if "ayaaya" in word or "yeye" in word or "woowoo" in word or "mama" in word:
            continue
        
        # 유효한 발음들을 하나씩 제거
        temp = word
        for sound in ["aya", "ye", "woo", "ma"]:
            temp = temp.replace(sound, " ")  # 공백으로 치환
        
        # 공백만 남았다면 유효한 단어
        if temp.strip() == "":
            count += 1
    
    return count