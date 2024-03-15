# 직장인 A씨는 1년 동안 열심히 일해서
# 연말에 성과급으로 천만 원을 받았습니다.
# 연이율 3.875%(단리)인 고정금리 상품에 예금하려고 합니다.
# 5년 동안 넣어두면 이자가 얼마 붙는지 계산

# 이자 = 원금 * 이율 * 기간
# 원리금 = 원금 (1 + (이율*시간))

# 원금(principal)
# 이율(rate)
# 기간(time)
# 이자(interest)

# 이자 = I = p * r * t
# 원리금 = M = p * (1 + r * t)
def interest():
    deposit = int(10000000)
    deposit = deposit + (deposit * 0.03875 * 5)
    print(deposit)

# interest()

def simple_interest(p, r, t):
    return p * r * t

def simple_interest_mount(p, r, t):
    return p * (1 + (r*t))

if __name__ == '__main__':
    print('Quiz1\n'
          'ex 1 : ', simple_interest(int(10000000), 0.03875, 5), '\n'
          'ex 2 : ', simple_interest(int(1100000), 0.05, 5/12), '\n',
          '\nQuiz2\n',
          'ex 1 : ', simple_interest_mount(int(10000000), 0.03875, 5), '\n',
          'ex 2 : ', simple_interest_mount(int(1100000), 0.05, 5/12)
          )

