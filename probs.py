
from pandas import read_csv

df = read_csv('teste.csv')

print(df['resultado'].describe())
