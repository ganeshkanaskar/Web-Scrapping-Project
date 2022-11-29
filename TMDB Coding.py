#!/usr/bin/env python
# coding: utf-8

# In[71]:


import requests
from bs4 import BeautifulSoup


# In[72]:


url_lst=[]
base_url='https://www.themoviedb.org/movie?page='

for item in range(1,51):
    url_lst.append(base_url+str(item))


# In[75]:


for data in url_lst:
    print(data)


# In[76]:


movie_url_lst =[]
common_url = 'https://www.themoviedb.org'
for url in url_lst:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko Chrome/56.0.2924.76 Safari/537.36'}
    source_data=requests.get(url, headers=headers).text
    soup_data=BeautifulSoup(source_data,'lxml')
    all_divs=soup_data.find_all('div', class_='card style_1')
    for item in all_divs:
        movie_url=item.find('a')['href']
        movie_url=common_url+movie_url
        movie_url_lst.append(movie_url)


# In[77]:


common_url = 'https://www.themoviedb.org'
movie_info=[]

for val in movie_url_lst:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko Chrome/56.0.2924.76 Safari/537.36'}
    source_data1=requests.get(val, headers=headers).text
    soup_data1=BeautifulSoup(source_data1,'lxml')
    all_divs1=soup_data1.find_all('div', class_='single_column')
    for v in all_divs1:
        try:
            mn=v.find('h2').text.split('(')[0].strip()
            #print(mn)
        except:
            mn=('None')
            #print(mn)
        try:
            rt=v.find('div',class_='user_score_chart')['data-percent']
            #print(rt)
        except:
            rt=('None')
            #print(rt)
        try:
            gn=v.find('span',class_='genres').text.replace('\xa0',' ').strip()
            #print(gn)
        except:
            gn=('None')
            #print(gn)
        try:
            rd=v.find('span',class_='release').text.split('(')[0].strip()
            #print(rd)
        except:
            rd=('None')
            #print(rd)
        try:
            ru_t=v.find('span',class_='runtime').text.strip()
            #print(ru_t)
        except:
            ru_t=('None')
            #print(ru_t)
        try:
            dn=v.find('ol', class_="people no_image").text.replace('\n',' ').strip()
            #print(dn)
        except:
            dn=('None')
            #print(dn)
        try:
            mu=v.find('h2')
            mu=(common_url+mu.find('a')['href'])
            #print(mu)
        except:
            mu=('none')
            #print(mu)
            
    all_movie_info={
        'Name':mn,
        'Rating':rt,
        'Genre':gn,
        'Release Date':rd,
        'Runtime':ru_t,
        'Director':dn,
        'Url':mu
    }
    
    movie_info.append(all_movie_info)
    #print(movie_info)


# In[78]:


import pandas as pd


# In[79]:


df = pd.DataFrame(movie_info)


# In[80]:


df


# In[81]:


df.to_excel('Movie_Database.xlsx')


# In[ ]:




