import pandas as pd
df = pd.read_csv('https://perso.telecom-paristech.fr/eagan/class/igr204//factbook.csv')

#gist of the data
print(df.head())

#some statistical information
print(df.describe ())

#column headers
print(df.columns.values)

#columns to be selected
#columns = ["Country", "Area (sq km)",sep="\t"]
#columns = [*]

#Selecting columns
#df[columns]

#df.loc[columns]