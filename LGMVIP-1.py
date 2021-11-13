#!/usr/bin/env python
# coding: utf-8

# # LGMVIP TASK-1

# # LEVEL-INTERMEDIATE

# ## EXPLORATORY DATA ANALYSIS ON DATASET TERRORISM
# 
# 
# ## OBJECTIVE - AS A SECURITY/DEFENCE ANALYST TRY TO FIND OUT THE HOT ZONE OF TERRORISM

# # AUTHOR - AMLAN DAS

# In[2]:


##IMPORTING NECESSARY LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[3]:


##READING AND UNDERSTANDING THE DATASET
data = pd.read_csv("C:/Users/AMLAN DAS/Desktop/globalterrorismdb_0718dist.csv",dtype='unicode',encoding='latin1')
data.head()


# In[4]:


data.tail()


# In[5]:


data.columns.values


# In[6]:


data.shape


# In[7]:


data.info()


# In[8]:


data.describe()


# In[9]:


##FINDING NULL VALUES
data.isnull().sum()


# In[10]:


print(data['country_txt'].value_counts().head(5))


# In[11]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['country_txt'].value_counts()[:5].index,data['country_txt'].value_counts()[:5].values)
plt.xlabel('Countries')
plt.ylabel('count')
plt.show()


# #### IRAQ IS THE MOST AFFECTED COUNTRY WITH TERRORIST ATTACKS 

# In[12]:


##TOP 5 REGIONS WITH MOST TERRORIST ATTACKS
print(data['region_txt'].value_counts().head(5))


# In[13]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['region_txt'].value_counts()[:5].index,data['country_txt'].value_counts()[:5].values)
plt.xlabel('Region')
plt.ylabel('count')
plt.show()


# #### MIDDLE EAST AND NORTH AFRICA IS THE REGION WITH MOST TERRORIST ATTACKS FOLLOWED BY SOUTH ASIA 

# In[14]:


##TOP 5 CITIES WITH MOST TERRORIST ATTACKS
print(data['city'].value_counts().head(5))


# In[15]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['city'].value_counts()[:5].index,data['country_txt'].value_counts()[:5].values)
plt.xlabel('CITY')
plt.ylabel('count')
plt.show()


# #### BAGHDAD IS THE CITY WITH MOST TERRORIST ATTACKS SINCE FIRST ONE IS UNKNOWN  

# In[16]:


##TOP 5 STATES WITH MOST TERRORIST ATTACKS
print(data['provstate'].value_counts().head(5))


# In[17]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['provstate'].value_counts()[:5].index,data['provstate'].value_counts()[:5].values)
plt.xlabel('state')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# #### BAGHDAD IS THE STATE WITH MOST TERROTIST ATTACKS

# In[18]:


##YEARS WITH MOST AND LEAST TERRORIST ATTACKS
print(data['iyear'].value_counts())


# In[21]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['iyear'].value_counts().index,data['iyear'].value_counts().values)
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# #### 2014 IS THE YEAR WITH THE MOST AND 1971 IS THE YEAR WITH LEAST TERRORIST ACTIVITIES 

# In[22]:


##TOP 5 MOST ACTIVE TERRORIST GROUPS
print(data['gname'].value_counts().head(5))


# In[23]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['gname'].value_counts()[:5].index,data['gname'].value_counts()[:5].values)
plt.xlabel('Terrorist Group')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# #### TALIBAN IS THE MOST  ACTIVE TERRORIST GROUP SINCE FIRST ONE IS UNKNOWN

# In[24]:


##TOP 5 MONTHS WITH MOST TERRORIST ATTACKS
print(data['imonth'].value_counts().head(5))


# In[25]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['imonth'].value_counts()[:5].index,data['imonth'].value_counts()[:5].values)
plt.xlabel('MONTH')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# #### MOST TERRORIST ATTACKS TOOK PLACE IN THE MONTH OF MAY 

# In[26]:


##TOP 5 METHOD OF TERRORIST ATTACKS 
print(data['attacktype1_txt'].value_counts().head(5))


# In[27]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['attacktype1_txt'].value_counts()[:5].index,data['attacktype1_txt'].value_counts()[:5].values)
plt.xlabel('ATTACK TYPE')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# # BOMBING/EXPLOSION IS THE MOST COMMON METHOD USED IN TERRORIST ATTACKS

# In[29]:


##TOP 5 TARGETS OF TERRORIST ATTACKS
print(data['targtype1_txt'].value_counts().head())


# In[30]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['targtype1_txt'].value_counts()[:5].index,data['targtype1_txt'].value_counts()[:5].values)
plt.xlabel('TARGET TYPE')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# #### PRIVATE CITIZENS AND PROPERTY ARE MOST AFFECTED BY TERRORIST  ATTACKS FOLLOWED BY MILLITARY, POLICE, GENERAL GOVERNMENT AND BUSINESS 

# In[31]:


##TOP 5 WEAPONS USED FOR TERRORIST ATTACKS
print(data['weaptype1_txt'].value_counts().head(5))


# In[32]:


##PLOTTING THE SAME IN A BAR GRAPH
plt.figure(figsize = (10,5))
sns.barplot(data['weaptype1_txt'].value_counts()[:5].index,data['weaptype1_txt'].value_counts()[:5].values)
plt.xlabel('Weapons Used')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()


# #### EXPLOSIVES ARE MOST USED AS WEAPONS FOR TERRORIST ATTACKS 

# In[33]:


data['success'].value_counts()


# # TERRORISTS ARE SUCCESSFUL 161632 TIMES AND FAITED 20059 IN CONDUCTING TERRORIST ATTACKS 

# In[34]:


data['suicide'].value_counts()


# ### 6633  PEOPOL COMMITTED SUISIDE DURING THE ATTACKS

# # CONCLUSION

# ### 1. MOST AFFECTED COUNTRY- IRAQ
# ### 2. MOST AFFECTED STATE- BAGHDAD
# ### 3. MOST AFFECTED CITY- BAGHDAD
# ### 4. MOST AFFECTED REGION- MIDDLE EAST AND NORTH AFRICA
# ### 5. MOST TERRIFIC YEAR- 2014
# ### 6. YEAR WITH LEAST TERRORIST ACTIVITIES- 1971
# ### 7. MOST COMMONLY USED ATTACK TYPE- BOMBING/EXPLOSION
# ### 8. WEAPON USED MOST NUMBER OF TIMES- EXPLOSIVES
# ### 9. MOST ACTIVE TERRORIST GROUP WITH MAXIMUM NUMBER OF ATTACKS- TALIBAN
# ### 10. AFFECTED TARGETS OF TERRORIST ATTACKS - PRIVATE CITIZENS AND PROPERTY ARE MOST AFFECTED BY TERRORIST ATTACKS FOLLOWED BY MILITARY,POLICE,GENERAL GOVERNMENT AND BUSINESS
# ### 11. MONTH WITH MOST ATTACKS- MAY 
# ### 12. THEY WERE SUCCESS MOST NUMBER OF TIMES IN THEIR ATTACKS
# 

# # HOTZONE OF TERRORISM: IRAQ

# # THANK YOU

# In[ ]:




