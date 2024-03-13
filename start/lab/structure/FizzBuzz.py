# 3의 배수는 fizz
# 5 의 배수는 buzz
# 3 과 5의 공배수는 FizzBuzz

for n in range(1, 101):
    match (n % 3, n % 5):
        case (0, 0):
            print('FizzBuzz')
        case (0, _):
            print('Fizz')
        case (_, 0):
            print('Buzz')
        case _:
            print(n)
