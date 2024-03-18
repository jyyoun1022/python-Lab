jjang = '09'

jjang = 'pig dad'

def ban():
    jjang1 = '07'
    print('jjang =', jjang1)


ban()
# ban() 함수 안에서 jjang = '07' 을 하면 새로운 변수를 만드는 것이다.
# 기존의 jjang 에는 영향을 미치지 않는다. 그리고 ban함수가 끝날 때는 그 함수 내에서
# 만들었던 변수들은 모두 없어진다.
print(jjang)

# 함수안에 만들어진 변수를 지역변수
# 함수 밖에서 만들어진 변수를 전역 변수

x = 10
def printx():
    print(x)

printx()


def e_is_10():
    global e
    e = 10
    print('e = ', e)

e_is_10()
print('global: E', e)
