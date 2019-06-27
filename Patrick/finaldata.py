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
data['Income minus total expenses'] = ((data['FINATXEM']/4) - data['Total expenses'])
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