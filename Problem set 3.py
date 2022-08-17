#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Question 1


# In[44]:



import pandas as pd
import numpy as np

users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|')
print("           ")
print(users.groupby('occupation').mean().age.round(2))

print(users.groupby('occupation').gender.value_counts().loc[:,'M']/users.groupby('occupation').gender.count().round(2).sort_values(ascending=False))

print("           ")
print(users.groupby('occupation').age.agg([min, max]))

print("             ")
print(users.groupby(['occupation', 'gender']).age.mean().round(2))

print("            ")
print(round((users.groupby('occupation').gender.value_counts().loc[:,'F']/users.groupby('occupation').gender.count())*100, 2))


# In[ ]:


# question 2


# In[12]:


import pandas as pd
import numpy as np

euro12=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv')

print(euro12.Goals)


num_teams = len(euro12.groupby('Team').groups)
print(num_teams)

cols = euro12.shape[1]
print(cols)


discipline = euro12[["Team","Yellow Cards", "Red Cards"]]
print(discipline)
 
discipline = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print(discipline)

mean_yellow_cards_per_team = discipline.groupby('Team').agg({'Yellow Cards': 'mean'})
print(mean_yellow_cards_per_team)

mean_yellow_cards_overall = mean_yellow_cards_per_team.mean()
print(mean_yellow_cards_overall)


# In[46]:


#Question 3


# In[45]:


import pandas as pd
import numpy as np

s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))

s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))

s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

Housing = pd.concat([s1, s2, s3], axis=1)
Housing.head()

Housing.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
Housing.head()

bigcolumn = pd.DataFrame(pd.concat([s1, s2, s3], axis=0))
bigcolumn

bigcolumn.iloc[95:105,]
bigcolumn.reset_index(inplace = True) 
bigcolumn.iloc[95:105,]


# In[ ]:


# Question 5


# In[59]:


import pandas as pd
import numpy as np

chipo = pd.read_csv('https://raw.githubusercontent.com//justmarkham//DAT8//master//data//chipotle.tsv', sep = '\t')
chipo.head(10)
len(chipo)
len(chipo.columns)
chipo.columns
chipo.index

chipo['item_name'].value_counts().head(1)
most_ordered = chipo['item_name'].value_counts().head(1) 
print(most_ordered)
chipo['choice_description'].value_counts().head(1)

total_items_orders = chipo['quantity'].sum()
print(total_items_orders)


chipo['item_price_float'] = chipo['item_price'].apply(lambda x : float(x[1:]))
revenue = (chipo['quantity']*chipo['item_price_float']).sum()
print(revenue)

chipo['order_id'].value_counts().count()
avg_order = revenue/chipo['order_id'].value_counts().count()
print(avg_order)
chipo['item_name'].value_counts().count()


# In[ ]:


# Question 6


# In[5]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
usmarriages = pd.read_csv("C:\\Users\\Babur\\OneDrive\\Desktop\\us-marriages-divorces-1867-2014.csv")
line1 = sns.lineplot(data = usmarriages, x="Year", y = "Marriages_per_1000", legend = "brief", label = "Marriages_per_1000")
line2 = sns.lineplot(data = usmarriages, x="Year", y = "Divorces_per_1000", legend = "brief", label = "Divorces_per_1000")
plt.ylabel("Marriages and Divorces per 1000")


# In[ ]:


# Question 7  


# In[25]:


import pandas as pd 
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
usmarriages = pd.read_csv("C:\\Users\\Babur\\OneDrive\\Desktop\\us-marriages-divorces-1867-2014.csv")#, names=['Year', 'Marriages', 'Divorces', 'Population','Marriages_per_1000', 'Divorces_per_1000']) #read csv into dataframe and specify column names
usmarriages.head()

fd = usmarriages[(usmarriages['Year'] == 1900) | (usmarriages['Year'] == 1950) |(usmarriages['Year'] == 2000)]

fd.plot(x="Year", y = ["Marriages_per_1000","Divorces_per_1000"], kind = "bar", figsize = (12,10), label =  ["Marriages_per_1000","Divorces_per_1000"])


plt.show()


# In[ ]:


# Question 8 


# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sea
get_ipython().run_line_magic('matplotlib', 'inline')

actors = pd.read_csv("C:\\Users\\Babur\\OneDrive\\Desktop\\actor_kill_counts.csv")

sea.barplot(x = "Count", y = "Actor", data = actors.sort_values("Count",ascending = False), label= "Actor kill count")


# In[ ]:


# Question 9


# In[28]:


import pandas as pd 
import matplotlib.pyplot as plt

romanemp  = pd.read_csv("C:\\Users\\Babur\\OneDrive\\Desktop\\roman-emperor-reigns.csv", names=['Emperor','Length_of_Reign','Cause_of_Death'])
plt.pie(romanemp.groupby(['Cause_of_Death']).count().Emperor, labels=romanemp.groupby(['Cause_of_Death']).count().Emperor.index, autopct='%1.1f%%',
        shadow=True, startangle=270)
plt.title(label = "cause of death of emperor")


# In[ ]:


# Question 10


# In[2]:


import seaborn
import pandas as pd
 
 
seaborn.set(style='whitegrid')
computerscience= pd.read_csv("C:\\Users\\Babur\\OneDrive\\Desktop\\arcade-revenue-vs-cs-doctorates.csv")
 
seaborn.scatterplot(x="Computer Science Doctorates Awarded (US)",
                    y="Total Arcade Revenue (billions)",label="Computer Science Doctorates Awarded (US)",
                    data=computerscience,c =['#C4E57D','#2AC280','#FFAE39','#DC5B3B','#52E397','#C5CBA3','#9CD5F6','#6E50D9','#9A5E59','#9BC8F5'])


# In[ ]:




