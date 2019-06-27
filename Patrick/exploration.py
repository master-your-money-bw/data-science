#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('https://raw.githubusercontent.com/Hira63S/Master-Your-Money/master/2017-4th%20Quarter.csv')
df


#%%
numerics = ['float16', 'float32', 'float64']
strings = ['object']
newdf = df.select_dtypes(include=numerics)
strings_df = df.select_dtypes(include=strings)
column_list = newdf.columns.tolist()
print(column_list)
columns_strings = strings_df.columns.tolist()
#%%
column_list.count('FSMPFRXM')

#%%
"""total food cost from home and away"""
df.FOODTOT.head()

#%%
df.FOODHOME.head()

#%% 
df.FOODAWAY.head()

#%%
df.FINCBEFM.head()

#%%
print(columns_strings)
len(columns_strings)

#%%
"""amount of income from wage before deduction"""
df.FWAGEXM.head()

#%%
df[column_list].head()

#%%
df['AGE2'].hist()

#%%
df.NETRENTX.value_counts()

#%%
"""opening fmli171 csv file and only looking at float type columns"""
fmli = pd.read_csv('./dataSets/fmli171x.csv')
numerics = ['float16', 'float32', 'float64']
fmli_numrc = fmli.select_dtypes(include=numerics)
fmli_numrc.head()

#%%
fmli_columns = fmli_numrc.columns.tolist()
print(fmli_columns)

#%%
new_merics.OTHREGX.value_counts()

#%%
columns = ['INC_RNKM', 'INC_RNK5', 'INC_RNK4', 'INC_RNK3', 'INC_RNK2', 'INC_RNK1', 'INC_RANK']
new_merics[columns].head()

#%%
itbi = pd.read_csv('./dataSets/itbi171x.csv')
numerics = ['int64','float16', 'float32', 'float64']
itbi_numrc = itbi.select_dtypes(include=numerics)
column_list = itbi_numrc.columns.tolist()
print(column_list, '\n\n', itbi.head())

#%%
itbi.shape

#%%
"""scrip will load each csv in a file and check if a 
   column is in that csv"""

from os import listdir
from os.path import isfile, join
mypath = './datasets/expn17'
csvs = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for csv in csvs:
    df = pd.read_csv('./datasets/expn17/{}'.format(csv))
    have = df.columns.tolist().count('MRTPMTX')
    print(str(csv),have)
  

#%%
