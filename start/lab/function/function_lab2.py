from datetime import datetime


def triple(x):
    print(x * 3)

triple(2)
triple('x')

def today():
    today = datetime.today()
    print(f'year : {today.year} \n'
          f'month : {today.month} \n'
          f'day : {today.day} \n')

    definitionToday = datetime(2021, 3, 21, 15, 46, 1, 94942)
    print(definitionToday)
today()

def calculate_korean_age(year):
    curr_year = datetime.today().year

    print(curr_year - year + 1)

calculate_korean_age(1996)

if __name__ == '__main__':
    print('current module is main')
else:
    print('what')


