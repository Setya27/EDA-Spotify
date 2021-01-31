#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('config', 'Completer.use_jedi = False')


# In[2]:


# Import libraries and load dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
spotify = pd.read_csv('spotify.csv')
df = spotify.copy()


# In[3]:


df.tail(10)


# In[4]:


# How many unique values and nullvalues each column?
column = []
for column_item in df.columns:
    column.append(column_item)

nunique = []
for nunique_item in df.columns:
    nunique.append(df[nunique_item].nunique())
    
isnull = []
isnull_percent = []
for null_item in df.columns:
    isnull.append(df[null_item].isnull().sum())
    isnull_percent.append((df[null_item].isnull().sum()/len(df[null_item]))*100)
    
pd.DataFrame({'Column': column, 'Total Unique': nunique, 'Null Value': isnull, 'Null Value (%)': isnull_percent})


# In[5]:


df.info()


# In[6]:


df.describe().round(3)


# In[7]:


# Data Visualization


# In[8]:


plt.figure(figsize=(15,7)) # Create canvas
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')


# In[9]:


sns.clustermap(df.corr(),cmap="coolwarm")

Strong relationship between year and song popularity
Strong relationship between loudness and energy
# In[10]:


plt.figure(figsize=(15, 6))
x = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(5)
ax = sns.barplot(x.index, x);
for ax_value in ax.patches:
    ax.annotate(format(ax_value.get_height(), '.1f'), 
                   (ax_value.get_x() + ax_value.get_width() / 2., ax_value.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')

ax.set_title('Top Artists with Popularity by Mean')
ax.set_ylabel('Popularity')
ax.set_xlabel('Artists')


# The most popular artists by average popularity are Bad Bunny and Jhay Cortez 

# In[11]:


plt.figure(figsize=(15,6))
y= df.groupby('name')['popularity'].mean().sort_values(ascending=False).head(5)
ay = sns.barplot(y.index, y);
for ay_value in ay.patches:
    ay.annotate(format(ay_value.get_height(), '.1f'), 
                   (ay_value.get_x() + ay_value.get_width() / 2., ay_value.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
    
ay.set_xlabel('Tracks');
ay.set_ylabel('Popularity');
ay.set_title('Top Tracks with Popularity');


# The most popular name by average popularity is Dakiti

# In[12]:


plt.figure(figsize=(15,6))
artists_popular = df.groupby('artists')['popularity'].sum().sort_values(ascending=False).head(5)
aa = sns.barplot(artists_popular.index, artists_popular)
for aa_value in aa.patches:
    aa.annotate(format(aa_value.get_height(), '.1f'), 
                   (aa_value.get_x() + aa_value.get_width() / 2., aa_value.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
aa.set_xlabel('Artists')
aa.set_ylabel('Popularity')
aa.set_title('Top Artists with Popularity')


# The most popular artists by sum popularity is The Beatles

# # Time Analysis

# In[13]:


plt.figure(figsize=(15,6))
sns.set_style('dark')
year_release_date = df.groupby('year')['release_date'].count()
az = sns.lineplot(year_release_date.index, year_release_date)
az.set_xlabel('Year')
az.set_ylabel('Count')
az.set_title('Count of Tracks Release Date')
plt.show();


# Mostly 2000 songs are added for each year on spotify

# In[14]:


plt.figure(figsize=(15,6))
sns.set_style('dark')
loudness_year = df.groupby('year')['loudness'].mean()
ab = sns.lineplot(loudness_year.index, loudness_year, label='loudness')
ab.set_xlabel('Year')
ab.set_ylabel('Average of Loudness')
ab.set_title('Average of Loudness every year');


# Tracks has become more loudness in recent year

# In[15]:


plt.figure(figsize=(15,6))
sns.set_style('dark')
tempo_year = df.groupby('year')['tempo'].mean()
ac = sns.lineplot(tempo_year.index, tempo_year, label='tempo')
ac.set_xlabel('Year')
ac.set_ylabel('Average of Tempo')
ac.set_title('Average of Tempo every year');


# Tracks has become more tempo in recent year
