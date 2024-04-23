#################################### 1

print('Welcome to Python world!')
print('Welcome to Computer Science')
print('Programming is fun!')

#################################### 2
number = int(input('Enter a number'))

def counter_number(number):
    if number < 10:
        return number
    else:
        return (number % 10) + ((number // 10) % 10) + ((number // 100) % 10) + ((number // 1000) % 10)

print(int(counter_number(number)))
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
    else:
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

##### 4.1
변수명 및 함수명 : 학습자 관점에서 보았을 때는 가능한 유추가 가능한 변수,함수 명이라면 된다고 생각합니다.
chatGPT의 함수명인 sum_of_digits는 자리수의 합이라고 유추가 되지만 만약, 입력을 456을 받았을 때, 400 + 50 + 6 라는 결과를 리턴하는 함수라면 애매할 수 있습니다.
따라서 결국 해당 함수는 내부적으로 들어가 보아야 무엇인지 정확하게 알 수 있기 때문에 변수명과 함수명은 해당 함수와 변수가 무엇인지만 유추하게끔만 해주면 좋을 것 같다고 생각합니다.
프로그램 외형 : chatGPT는 재귀함수를 이용하여 코드가 간략해지고, 이해하기 쉽다고 생각하지만, 재귀함수를 사용하는것은 반복구조를 사용하는 것이라 생각하기에 잘못되었다고 생각합니다.
논리적 흐름 : 학습자는 0과 1000사이라고 명시되어 있으므로 input 값이 1000또한 들어올 수 있다고 가정하고 만들었습니다.따라서 일,십,백,천 자리수인 최대 4자리수로 생각하여 만들었고,
chatGPT에서는 자리수가 어떻게 되든 각 자리수의 합을 계산하는 방법을 사용하여 문제의 변경성과 유지보수성을 높은 코드라고 볼 수 있다고 생각합니다.



##### 4.2
def evaluate_grade(score):
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
            grade = evaluate_grade(score)
            print(f"입력한 점수 {score}의 성적은 {grade}입니다.")
        else:
            print("잘못된 입력입니다. 점수는 0부터 100까지의 범위 내에 있어야 합니다.")
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력하세요.")

if __name__ == "__main__":
    main()

######## 4.2
- 변수명 함수명 : 위와 동일 하면서 파이썬 언어에 대한 변수,함수명에 대한 규칙만 지키면 됩니다. 다만 제가 작성한 point 보다는 score 라는 변수를 사용했더라면 '점수로 인한 등급을 평가하는 함수' 라는 결과를 좀더 쉽게 유추할 것 같습니다.
- 프로그램 외형 : 두 코드 모두 값을 입력 받고, 해당 점수를 기준으로 성적을 산출하는 비슷한 외형을 갖고 있으나, GPT 에서는 main() 함수를 사용하여 프로그램의 진입점을 명시적으로 나타내었습니다.
- 논리적 흐름 : GPT 에서는 매번 선택구조에서 return 을 시켜주었지만 저는 마지막에 return 을 한번만 해주었습니다.
각 조건문에 return 을 사용하면 조건이 충족될 때 함수가 종료되므로 불필요한 코드 실행을 방지할 수 있습니다. 이는 코드의 논리적 흐름을 더 정확하게 만들어 줍니다.
반면, 저같은 경우에는 함수 내의 조건을 모두 확인해야 함수가 종료하므로 논리적 흐름이 더 복잡해질 수 있다고 생각합니다.


