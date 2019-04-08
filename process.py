import pandas as pd
import numpy as np

df = pd.read_excel('dataset.xlsx', 1)

''' Data Preprocessing '''
# 1. Data Cleaning
df = df.apply(pd.to_numeric, errors="coerce")
df = df.dropna()

# 2. Data Reduction
df = df.drop(columns=['TC'])
print(df.head())

''' Data Augmentation '''

ph = df['pH']
cod = df['COD']
bod = df['BOD']
nh3 = df['AMM.']
tkn = df['TKN']
do = df['DO']
wt = df['WT']

phs = np.std(ph)
cods = np.std(cod)
bods = np.std(bod)
nh3s = np.std(nh3)
tkns = np.std(tkn)
dos = np.std(do)
wts = np.std(wt)

dataset = []

for _,row in df.iterrows():
        temp = {
            'PH': row['pH'],
            'COD': row['COD'],
            'BOD': row['BOD'],
            'AMM.': row['AMM.'],
            'TKN': row['TKN'],
            'DO': row['DO'],
            'WT': row['WT']
        }
        dataset.append(temp)
        print(temp)

for _ in range(20):
    for _,row in df.iterrows():
        temp = {
            'PH': row['pH'] + np.random.uniform(phs),
            'COD': row['COD'] + np.random.uniform(cods),
            'BOD': row['BOD'] + np.random.uniform(bods),
            'AMM.': row['AMM.'] + np.random.uniform(nh3s),
            'TKN': row['TKN'] + np.random.uniform(tkns),
            'DO': row['DO'] + np.random.uniform(dos),
            'WT': row['WT'] + np.random.uniform(wts)
        }
        dataset.append(temp)
        print(temp)

print(len(dataset), "entries synthetically created.")

''' Save the new Dataset '''

df = pd.DataFrame(dataset)
df.to_csv('newDataset.csv')