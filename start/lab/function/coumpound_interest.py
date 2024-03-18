#   R = 원리금
#   P = 원금
#   r = 연이율
#   t = 기간
#   n = 복리 횟수

# 원리금 = 원금 * (1 + 연이율 / 복리 횟수) ** (기간 * 연이율)

def compound_interest(p, r, t, n):

    result = p * (1 + r / n) ** (n * t)
    print(result)

compound_interest(1500000, 0.043, 6 , 0.5)