import pandas as pd
df = pd.read_csv('https://perso.telecom-paristech.fr/eagan/class/igr204/data/factbook.csv')

#gist of the data
print(df.head())

#some statistical information
print(df.describe ())

#column headers
print(df.columns.values)
