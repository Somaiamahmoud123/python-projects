#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


data = pd.read_csv("C:/Users/Allewaa/Downloads/udemy_courses-raw.csv")


# In[3]:


data


# In[4]:


data.info()


# In[5]:


data['subject'].value_counts()


# In[6]:


data['subject'].describe()


# In[7]:


pd.to_datetime(data['published_timestamp'])


# In[8]:


data.dtypes


# In[31]:





# In[9]:


data[ 'published_timestamp' ] = pd.to_datetime(data['published_timestamp'])


# In[10]:


data.dtypes


# In[11]:


data['year'] = data['published_timestamp'] .dt.year


# In[12]:


data


# In[13]:


data['month'] = data['published_timestamp'] .dt.month_name()


# In[14]:


data['quarter'] = data['published_timestamp'] .dt.quarter


# In[15]:


data


# In[17]:


data.set_index(data['published_timestamp'],inplace = True)


# In[18]:


data


# In[19]:


data['profit'] = data['price'] * data['num_subscribers']


# In[20]:


data


# In[21]:


data[data.duplicated(keep=False)]


# In[22]:


data.drop_duplicates(inplace=True)


# In[23]:


data.duplicated().sum()


# In[24]:


data['content_duration'].sort_values()


# In[25]:


data['duration']=pd.qcut(data['content_duration'],6,['0-1','1-3','3-7','7-12','12-20','20+'])


# In[26]:


data


# In[27]:


data.rename(columns={'duration':'duration_category'} , inplace=True)


# In[28]:


data


# In[51]:


data['subject'].value_counts().plot(kind='bar')


# In[30]:


data['subject'].value_counts().plot(kind='pie')


# In[31]:


data['subject'].describe(include='o')


# In[32]:


data.groupby('subject').sum()['num_subscribers']


# In[33]:


fig = px.bar(data_frame=data,
     x=data.groupby('subject').sum()['num_subscribers'].index,
    y=data.groupby('subject').sum()['num_subscribers'].values
      )
fig.update_xaxes(title='subject')
fig.update_yaxes(title='#courses')
fig.show()


# In[36]:


data.groupby('subject',as_index=False)['profit'].sum().sort_values(by='profit',ascending=False)


# In[34]:


data.groupby('subject').sum()['profit']


# In[35]:


plt.xticks(rotation=45)
sns.barplot(data=data,
  x=data.groupby('subject').sum()['profit'].index,
   y=data.groupby('subject').sum()['profit'].values         
           )


# In[37]:


fig = px.bar(data_frame=data,
   x = data['subject'],
   color = data['is_paid'])          
fig.update_xaxes(title='subject')
fig.update_yaxes(title='#courses')
fig.show()


# In[40]:


df = sns.load_dataset("titanic")
sns.countplot(x=data["subject"])


# In[53]:


sns.countplot(data=data,x="subject",hue="level")


# In[48]:


data['price'].describe()


# In[ ]:




