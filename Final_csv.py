#!/usr/bin/env python
# coding: utf-8

# In[5]:


url = 'https://raw.githubusercontent.com/master-your-money-bw/data-science/master/datasets/almost_final.csv'


# In[23]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import statsmodels.api as sm


# In[7]:


df = pd.read_csv(url)

df.head()


# In[8]:


df['Necessities'] = (df['Total Housing'] + df['Total Food'] + df['Total Transportation cost'])

df['Necessities'].head()


# In[10]:


df['50%'] = (df['Necessities']/3) / ((df['FINATXEM'])/12)

df['50%'].head()


# In[11]:


df['30%'] = ((df['Luxury expenses'] + df['Entertainment']) / 3) / ((df['FINATXEM'])/12)

df['30%'].head()


# In[12]:


df['20%'] = ((df['possible savings'])/3) / (df['FINATXEM'] / 12)

df['20%'].head()


# In[14]:


df.head()


# In[18]:


df['50%'].describe()


# In[17]:


df = df.loc[(df!=0).all(1)]


# In[20]:


df['20%'].describe()


# In[19]:


df['30%'].describe()


# ##Model##
#

# In[22]:


features = ['FINATXEM']

target = '50%'

X = df[features]
y = df[target]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)


# In[26]:


model = LinearRegression()
model.fit(X_train, y_train)
y_pred = np.exp(model.predict(X_test)) # Apply exponential function (inverse of natural log) to the predictions
print('R^2', model.score(X_test, y_pred))


# In[ ]:
