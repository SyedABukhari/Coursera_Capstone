#!/usr/bin/env python
# coding: utf-8

# # This code uses COVID 19 data for visualization of total number of cases in a country and display an interactive world map. User can move the cursor on the map to find out the cases in a specific country. This data presents total number of cases on August 25, 2020

# First of all, I will install pyecharts library.

# In[1]:


#install pyecharts

pip install pyecharts==1.7.1


# # Import all the libraries to be used

# In[4]:


#import libraries
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import numpy as np
import pandas as pd
import xlsxwriter


# # Import data set: The data was downloaded from https://ourworldindata.org/coronavirus

# In[17]:


#import data

dataset = pd.read_excel (r'C:\Users\Asad\Downloads\owid-covid-data.xlsx')
print (dataset)


# # Data needs to be cleaned before further processing

# In[29]:


#Sort data type and pick a particlular date
dataset["date"]=pd.to_datetime(dataset["date"])
df = dataset.sort_values(by=['date'], ascending=False) #sort data by date
map_df=df[df['date']=='2020-08-25']
map_df.reset_index(drop=True, inplace=True)
map_df


# # Adding total number of cases per country on world's map

# In[30]:


country=list(map_df["location"])
totalcases=list(map_df["total_cases"])


# In[31]:


list1 = [[country[i],totalcases[i]] for i in range(len(country))] #prepare data for visualization
map_1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px')) #create the map and set the size of the map
map_1.add("Total Confirmed Cases", list1, maptype='world') #add world map
map_1.set_global_opts( #set global config
 visualmap_opts=opts.VisualMapOpts(max_=1100000,    is_piecewise=False),
 legend_opts=opts.LegendOpts(is_show=False), #show legend 
 )
map_1.render_notebook() #show the map 


# # A total of 212 countries displayed on map. The data looks clumsy. We can get rid of countries name to make it more attaractive

# In[32]:


list1 = [[country[i],totalcases[i]] for i in range(len(country))] 
map_1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px')) 
map_1.add("Total Confirmed Cases", 
 list1, maptype='world') 
map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) #remove country names
map_1.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1100000,is_piecewise=False),
 legend_opts=opts.LegendOpts(is_show=False))
map_1.render_notebook()


# In[35]:


list1 = [[country[i],totalcases[i]] for i in range(len(country))] 
map_1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px')) 
map_1.add("Total Confirmed Cases", 
 list1, 
 maptype='world',
 is_map_symbol_show=False)
map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) 
map_1.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=1100000,is_piecewise=False),
 legend_opts=opts.LegendOpts(is_show=False))
map_1.render_notebook() 


# # Let's organize the data with a color map by adding limits on number of cases.

# In[ ]:


list1 = [[country[i],totalcases[i]] for i in range(len(country))] 
map_1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px')) 
map_1.add("Total Confirmed Cases", 
 list1, 
 maptype='world',
 is_map_symbol_show=False) 
map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) 
map_1.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=50000000,is_piecewise=True,pieces=[
 {"min": 900000},
 {"min": 200000, "max": 499999},
 {"min": 100000, "max": 199999},
 {"min": 50000, "max": 99999},
 {"min": 10000, "max": 49999},
 {"max": 9999},]),
 legend_opts=opts.LegendOpts(is_show=False))
map_1.render_notebook() 


# # We can add a title of on the interactive map with a date when the data was processed

# In[61]:


list1 = [[country[i],totalcases[i]] for i in range(len(country))] 
map_1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px')) 
map_1.add('Total Confirmed Cases', 
 list1,
 maptype='world',
 is_map_symbol_show=False)
map_1.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) 
map_1.set_global_opts(
visualmap_opts=opts.VisualMapOpts(max_=1100000,is_piecewise=True,pieces=[
 {"min": 500000},
 {"min": 200000, "max": 499999},
 {"min": 100000, "max": 199999},
 {"min": 50000, "max": 99999},
 {"min": 10000, "max": 49999},
 {"max": 9999},]),
 title_opts=opts.TitleOpts(
 title='Covid-19 Worldwide Total Cases',
 subtitle='Till Aug 25th,2020',
 pos_left='center',
 padding=0,
 item_gap=2,# gap between title and subtitle 
 title_textstyle_opts= opts.TextStyleOpts(color='magenta',
 font_weight='bold',
 font_family='Courier New',
 font_size=30), 
 subtitle_textstyle_opts= opts.TextStyleOpts(color='grey',
 font_weight='bold',
 font_family='Courier New',
 font_size=13)), 
 legend_opts=opts.LegendOpts(is_show=False))
map_1.render_notebook() 


# # Further analysis is beyond the scope of this project. The data file is rich and can potentially be used for pridictive modeling using machine learning algorithms.

# In[ ]:




