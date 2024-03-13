is_leap_year = None

year = int(input('search Year :\n'))

if year % 4 == 0: #4로 나누어 떨어지면 윤년일 가능성이 있다.
    if year % 100 == 0: # 100으로 나누었을때 나머지가 0 이라면
        if year % 400 == 0: # 400으로 나누어 떨어진다면 윤년이다.
            is_leap_year = True
        else:               # 이때 400으로 나누어 떨어지지 않는다면 윤년이 아니다
            is_leap_year = False
    else:               # 100으로 나누어떨이지지 않는다면 윤년이다
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(f'출생 연도 {year} 년은 {{윤년}}입니다.');
else:
    print(f'출생 연도 {year} 년은 {{평년}}입니다.');