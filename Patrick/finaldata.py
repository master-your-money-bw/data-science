#%%
import pandas as pd


#%%
data = pd.read_csv('https://raw.githubusercontent.com/Hira63S/Master-Your-Money/master/2017%20Quarter%204%20-Big%20Categories%20expenditure.csv')
data.head()


#%%
data['Luxury expenses'] = data['Total expenses'] - (data['Entertainment'] + data['Total Transportation cost'] +
                                                   data['Total Housing'] + data['Total Food'])

#%%
data.rename(columns={'FINCBTAX':'Income before tax'}, inplace=True)
data.head()

#%%
data['Income minus total expenses'] = ((data['Income After Taxes']/4) - data['Total expenses'])
data.head()

#%%
data['possible savings'] = data['Income minus total expenses']/3
data.head(20)

#%%
fmli = pd.read_csv('./datasets/intrvw17/fmli174.csv')
fmli['FINATXEM'].head()

#%%
data['FINATXEM'] = fmli['FINATXEM']
data.head(20)

#%%
data['possible savings'].describe()

#%%
data.to_csv(path_or_buf='C:/Users/Patrick/Desktop/Repos/data-science/datasets/almost_final.csv')

#%%
"""Remove NaN and other unwanted data and load new dataset file"""
data = pd.read_csv('../datasets/almost_final.csv')
data.head()

#%%
data.rename(columns={'FINATXEM':'Income After Tax'}, inplace=True)
data.head()


#%%
data['Necessities'] = (data['Total Transportation cost'] + data['Total Housing'] +
                      data['Total Food'])
data.head()
#%%
data['50%'] = data['Necessities']/(data['Income After Taxes']/4) 
data.head(20)

#%%
data['30%'] = data['Luxury expenses']/(data['Income After Taxes']/4)
data.head()

#%%
data['20%'] = (data['possible savings']*3) / (data['Income After Taxes']/4)
data.head(20)

#%%
data['50%_delta'] = data['50%']-.5
data['30%_delta'] = data['30%']-.3
data['20%_delta'] = data['20%']-.2
data.head()

#%%
data['target']