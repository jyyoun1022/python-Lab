y = int(input('what year were you born? '))

zen = None

if y <= 1924:
    zen = 'The Greatest Generation'
elif y <= 1945:
    zen = 'The Silent Generation'
elif y <= 1980:
    zen = 'The Baby Boomer'
elif y <= 1996:
    zen = 'The Millenial'
else:
    zen = 'The Generation Z'

print(f"You're {zen}.")