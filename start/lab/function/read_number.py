def korean_number(num):
    # 여기서 korean_dict는 딕셔너리(Dictoionary) 이다
    # Dictionary는 키-값 쌍을 저장하는 자료구조
    korean_dict = {
        1: '일',
        2: '이',
        3: '삼',
        4: '사',
        5: '오',
        6: '육',
        7: '칠',
        8: '팔',
        9: '구',
        10: '십'
    }
    print('dict_keys() : ', korean_dict.keys()) # 딕셔너리의 키목록을 반환
    print('dict_values() : ', korean_dict.values()) # 딕셔너리의 값 목록을 반환
    print('dict_items() : ', korean_dict.items())   # 딕셔너리를 키,값 튜플의 목록으로 반환

    return korean_dict.get(num, None)

print(korean_number(11))
