#!/usr/bin/env python
# coding: utf-8

# In[147]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# In[176]:


df = pd.read_csv(r"E:\GEProject\generic_ballot_pollsNEW.csv")
df.head()
df.stb.freq(['parliament'])


# In[177]:


from IPython.html import widgets
from IPython.display import display

geo={'JOHOR':['SEGAMAT','PAGOH'],'KEDAH':['LANGKAWI','LED'],'PERAK':['BAGAN DATUK']}

def print_city(city):
    print (city)

def select_city(state):
    cityW.options = geo[state]


scW = widgets.Dropdown(options=geo.keys())
init = scW.value
cityW = widgets.Dropdown(options=geo[init])
j = widgets.interactive(print_city, city=cityW)
i = widgets.interactive(select_city, state=scW)
display(i)
display(j)


# In[178]:


pd.set_option('display.max_columns', None)


# In[179]:


#df = df[df['state']==scW.value]
df = df[df['parliament']==cityW.value]
df.head()


# In[180]:


import sidetable


# In[181]:


results_df = pd.read_csv(r"E:\GEProject\generic_ballot_pollsNEW.csv")


# In[182]:


results_df.head()


# In[183]:


results_df.stb.freq(['parliament'])
#results_df.stb.freq(['state'])


# In[184]:


#results_df = results_df[results_df['state']==scW.value]
results_df = results_df[results_df['parliament']==cityW.value]


# In[185]:


results_df['actual_margin'] = results_df['gov'] - results_df['opp']
results_df['poll_margin'] = results_df['gov_poll'] - results_df['opp_poll']
results_df['error'] = abs(results_df['actual_margin'] - results_df['poll_margin'])
results_df


# In[186]:


df['undecided'] = 100 - df['gov'] - df['opp']
df['notvote'] = df['undecided']
df['actual_margin'] = results_df['actual_margin']
df['poll_margin'] = results_df['poll_margin']
df['error'] = results_df['error']


# In[187]:


df['gov'] = df['gov'] + 0.5 * df['undecided']
df['opp'] = df['opp'] + 0.5 * df['undecided']
df = df[['gov', 'opp','notvote', 'actual_margin','poll_margin', 'error']]


# In[188]:


means = df.mean()
avg_error = results_df['error'].mean()


# In[189]:


results_df.head()


# In[190]:


gov_victories = 0

for x in range(0, 100000):
    error = np.random.normal(scale=avg_error)
    
    adj_gov = means['gov'] + error
    adj_opp = means['opp'] - error
        
    if adj_gov > adj_opp:
        gov_victories = gov_victories + 1
        
gov_victories / 100000


# In[191]:


gov_victories = 0

for x in range(0, 100000):
    error = np.random.normal(scale=avg_error)
    
    adj_gov = means['gov'] + error
    adj_opp = means['opp'] - error
        
    if adj_gov > adj_opp:
        gov_victories = gov_victories + 1
        
trial1 = gov_victories / 100000


# In[192]:


gov_victories = 0

for x in range(0, 100000):
    error = np.random.normal(scale=avg_error)
    
    adj_gov = means['gov'] + error
    adj_opp = means['opp'] - error
        
    if adj_gov > adj_opp:
        gov_victories = gov_victories + 1
        
trial2 = gov_victories / 100000


# In[193]:


gov_victories = 0

for x in range(0, 100000):
    error = np.random.normal(scale=avg_error)
    
    adj_gov = means['gov'] + error
    adj_opp = means['opp'] - error
        
    if adj_gov > adj_opp:
        gov_victories = gov_victories + 1
        
trial3 = gov_victories / 100000


# In[194]:


gov_victories = 0

for x in range(0, 100000):
    error = np.random.normal(scale=avg_error)
    
    adj_gov = means['gov'] + error
    adj_opp = means['opp'] - error
        
    if adj_gov > adj_opp:
        gov_victories = gov_victories + 1
        
trial4 = gov_victories / 100000


# In[195]:


gov_victories = 0

for x in range(0, 100000):
    error = np.random.normal(scale=avg_error)
    
    adj_gov = means['gov'] + error
    adj_opp = means['opp'] - error
        
    if adj_gov > adj_opp:
        gov_victories = gov_victories + 1
        
trial5 = gov_victories / 100000


# In[196]:


print('1 trial : ', trial1)
print('2 trial : ', trial2)
print('3 trial : ', trial3)
print('4 trial : ', trial4)
print('5 trial : ', trial5)


# In[ ]:





# In[ ]:




