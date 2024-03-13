def forInElse():
    for x in [1,2,3,4]:
        print(x)
    else: # java의 finally와 비슷
        print('리스트의 원소를 모두 출력했다.')



def forInElseAndBreak():
    for x in [1,2,3,4]:
        if x % 3:
            print(x)
        else:
            break
    else:
        print('리스트의 원소를 모두 출력했다.')
    # 반복문을 break 해버리면 그럴 때는 else 블록이 실행 되지 않는다.


def whileElse():
    countdown = 5
    while countdown > 0:
        print(countdown)
        countdown -= 1
        if input() == '중단':
            break
    else:
        print('발사!')
# 마찬가지로 중간에 while 문이 break 될 경우에는 else 블록이 실행되지 않습니다.


# whileElse()
# forInElse()
# forInElseAndBreak()

