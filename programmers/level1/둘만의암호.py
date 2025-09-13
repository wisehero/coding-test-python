def solution(s, skip, index):
    """
    주어진 문자열을 암호화하는 함수
    skip에 포함된 문자는 제외하고 index만큼 뒤의 문자로 변환
    """
    result = ''
    
    # skip할 문자들을 set으로 변환 (O(1) 검색을 위해)
    skip_chars = set(skip)
    
    # 사용 가능한 알파벳 리스트 생성
    available_chars = []
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in skip_chars:
            available_chars.append(char)
    
    # 각 문자의 인덱스 매핑 (빠른 검색을 위해)
    char_to_index = {char: i for i, char in enumerate(available_chars)}
    total_chars = len(available_chars)
    
    # 문자열의 각 문자를 변환
    for char in s:
        current_index = char_to_index[char]
        new_index = (current_index + index) % total_chars
        result += available_chars[new_index]
    
    return result