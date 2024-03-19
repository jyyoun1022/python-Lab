# 놀이기구의 이름과 키 제한을 나타낸 문자열을 입력받아,
# 놀이기구의 이름, 탑승가능한 키의 하한과 상한을 각 행에 출력

# exText : 플라이벤처 : 100cm ~ 125cm

def ridingInfo(input):
    name, limit = map(str.strip, input.split(':'))

    cmmin, cmmax = None

    if '~' in limit:
        templist = []
        for x in limit.split('~'):
            templist.append(x.replace('cm', ''))
        cmmin, cmmax = templist[0], templist[1]
    elif '이상' in limit:
        cmmin = int(limit.split('cm')[0])

    return name, cmmin, cmmax
def read(text):
    ridename, limit = map(str.strip, text.split(':'))

    cmmin = cmmax = None

    if '~' in limit:
        templist = []
        for x in limit.split('~'):
            templist.append(x.replace('cm', ''))

        cmmin, cmmax = templist[0], templist[1]
    elif '이상' in limit:
        cmmin = int(limit.split('cm')[0])


    return ridename, cmmin, cmmax


if __name__ == '__main__':
    ridename, cmmin, cmmax = ridingInfo(input())
    print('이름 : ', ridename)
    print('하한 : ', cmmin)
    print('상한 : ', cmmax)

