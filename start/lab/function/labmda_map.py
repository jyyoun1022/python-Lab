# map(함수, 리스트)

# 함수와 리스트를 인자로 받는다.
# 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음
# 그 결과를 새로운 리스트에 담아준다.

first = map(lambda x: x ** 2, range(5))
print(first)

result = list(map(lambda x: x ** 2, range(5)))
print(result)