#!/usr/bin/env python
# coding: utf-8

get_ipython().run_line_magic('config', 'Completer.use_jedi = False')

# Import libraries and load dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
spotify = pd.read_csv('spotify.csv')
df = spotify.copy()

df.tail(10)

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


x = df.groupby(['year']).count()[['release_date']]

x.reset_index()

df.info()

df.describe().round(3)

# Data Visualization

plt.figure(figsize=(15,7)) # Create canvas
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

sns.clustermap(df.corr(),cmap="coolwarm")

#Strong relationship between year and song popularity
#Strong relationship between loudness and energy

plt.figure(figsize=(15, 6))
x = df.groupby('artists')['popularity'].mean().sort_values(ascending=False).head(20)
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
plt.xticks(rotation = 90);


# The most popular artists by average popularity are Bad Bunny and Jhay Cortez 

plt.figure(figsize=(15,6))
y= df.groupby('name')['popularity'].mean().sort_values(ascending=False).head(20)
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
plt.xticks(rotation=90);


# The most popular name by average popularity is Dakiti

plt.figure(figsize=(15,6))
artists_popular = df.groupby('artists')['popularity'].sum().sort_values(ascending=False).head(20)
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
plt.xticks(rotation=90);


# The most popular artists by sum popularity is The Beatles

# # Time Analysis

# In[15]:


plt.figure(figsize=(15,6))
sns.set_style('dark')
year_release_date = df.groupby('year')['release_date'].count()
az = sns.lineplot(year_release_date.index, year_release_date)
az.set_xlabel('Year')
az.set_ylabel('Count')
az.set_title('Count of Tracks Release Date')
plt.show();


# Mostly 2000 songs are added for each year on spotify

# In[16]:


plt.figure(figsize=(15,6))
sns.set_style('dark')
loudness_year = df.groupby('year')['loudness'].mean()
ab = sns.lineplot(loudness_year.index, loudness_year, label='loudness')
ab.set_xlabel('Year')
ab.set_ylabel('Average of Loudness')
ab.set_title('Average of Loudness every year');


# Tracks has become more loudness in recent year


plt.figure(figsize=(15,6))
sns.set_style('dark')
tempo_year = df.groupby('year')['tempo'].mean()
ac = sns.lineplot(tempo_year.index, tempo_year, label='tempo')
ac.set_xlabel('Year')
ac.set_ylabel('Average of Tempo')
ac.set_title('Average of Tempo every year');


# Tracks has become more tempo in recent year
