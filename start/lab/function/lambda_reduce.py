#   reduce(함수, 시퀀스)
# 시퀀스의 원소들을 누적적으로 함수에 적용

from functools import reduce

result = reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])

print(result)

strResult = reduce(lambda x, y: y + x, 'abcde')

print(strResult)

# 초기 값으로 'a'를 가져옵니다.
# 다음 문자 'b'가 올 때, 람다 함수에 따라 'b' + 'a'로 결합됩니다. 따라서 'ba'가 됩니다.
# 다음 문자 'c'가 올 때, 람다 함수에 따라 'c' + 'ba'로 결합됩니다. 따라서 'cba'가 됩니다.
# 다음 문자 'd'가 올 때, 람다 함수에 따라 'd' + 'cba'로 결합됩니다. 따라서 'dcba'가 됩니다.
# 마지막으로 문자 'e'가 올 때, 람다 함수에 따라 'e' + 'dcba'로 결합됩니다. 따라서 'edcba'가 최종 결과가 됩니다.