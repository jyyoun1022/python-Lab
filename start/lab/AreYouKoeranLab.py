year = int(input('what year were you born? '))

zen = None


if year <= 1924:
    zen = 'The Greatest Generation'
elif year <= 1945 or (year <= 1954 and str(input('Are you Korean ? (Y/N)').lower()[0]) == 'y'):
    zen = 'The Silent Generation'
elif year <= 1963 or (year <= 1964 and str(input('Are you Korean ? (Y/N)').lower()[0]) != 'y'):
    zen = 'a baby bommer'
elif year <= 1980:
    zen = 'The Baby Boomer'
elif year <= 1996:
    zen = 'The Millenial'
else:
    zen = 'The Generation Z'

print(zen)