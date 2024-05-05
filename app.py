
from controller import JogoBicho
from pandas import DataFrame

jb = JogoBicho(bicho='Cachorro')

c = 0

l = []

while(True):

    l.append(jb())

    c += 1

    print(c, end = '\r')

    if c >= 10000:
        break

df = DataFrame(l)

print(df)

df.to_csv('teste.csv')
