
def test1 ():
    num = int(input('how many num : '))

    for i in range(num):
        print(num)

    print(range(num)) # range(4) == range(0,4)

def test2():
    num = int(input('num : '))

    for i in range(1,num+1):
        print(f'{i} {(i)**2}')

# test1()
def temperature():
    minV, maxV = map(int,input('min,max temperature : ').split(','))
    print(f'{minV}, {maxV}')

    temp = int(input('temp : '))

    while temp != -999:
        if minV <= temp <= maxV:
            print('Noting to report')
            temp = int(input('re temp : '))
        else:
            print('alert!')
            break

temperature()

