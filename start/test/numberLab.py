#################################### 1

print('Welcome to Python world!')
print('Welcome to Computer Science')
print('Programming is fun!')

#################################### 2
number = int(input('Enter a number'))

def sum_of_digit(number):
    if number < 10:
        return number
    else:
        return (number % 10) + ((number // 10) % 10) + (number // 100)

print(int(sum_of_digit(number)))
##################################### 3


myPoint = int(input('Enter your point'))
result = None
def calculate_grade(myPoint):
    if myPoint > 100:
        result = '잘못된 점수'
    elif 90 < myPoint <= 100:
        result = 'A'
    elif 80 < myPoint <= 89:
        result = 'B'
    elif 70 < myPoint <= 79:
        result = 'C'
    elif 60 < myPoint <= 69:
        result = 'D'
    elif 0 < myPoint <= 59:
        result = 'F'
    elif 0 > myPoint:
        result = '잘못된 점수'
    return result + '입니다.'

print(calculate_grade(myPoint))

##################################### 4.1
def sum_of_digits(num):
    # 기저 사례: 한 자리 숫자인 경우
    if num < 10:
        return num

    # 재귀적으로 각 자릿수의 합을 계산
    return num % 10 + sum_of_digits(num // 10)


def main():
    # 사용자로부터 정수 입력 받기
    while True:
        try:
            num = int(input("0과 1000 사이의 정수를 입력하세요: "))
            if 0 <= num <= 1000:
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")
        except ValueError:
            print("잘못된 입력입니다. 다시 입력하세요.")

    # 각 자릿수의 합 계산
    digit_sum = sum_of_digits(num)

    # 결과 출력
    print(f"{num}의 각 자릿수의 합은 {digit_sum}입니다.")


if __name__ == "__main__":
    main()
##### 4.2
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        score = float(input("점수를 입력하세요: "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"입력한 점수 {score}의 성적은 {grade}입니다.")
        else:
            print("잘못된 입력입니다. 점수는 0부터 100까지의 범위 내에 있어야 합니다.")
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")

if __name__ == "__main__":
    main()
