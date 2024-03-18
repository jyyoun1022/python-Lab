#   filter(함수, 리스트)

result = list(filter(lambda x: x < 5, range(10)))
print(result)

# 홀수만 돌려주는 filter
# 짝수는 2로 나누어지는 수, 홀수는 2로 나누어 떨어지지 않는수
# 짝수는 2로 나눈 나머지가 0이고, 홀수는 1
# 나머지 연산자를 구할 때는 %

test = list(filter(lambda x: x % 2, range(10)))
# 참은 1이고, 거짓은 0 이기 떄문에 자동적으로 홀수만 나오게 된다.
print(test)