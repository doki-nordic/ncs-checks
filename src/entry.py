from random import randrange

print('OK')

with open('../data/a.txt', 'w') as f:
  f.write(randrange(10))

