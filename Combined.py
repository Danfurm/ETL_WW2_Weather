
# coding: utf-8

# In[90]:


import pandas as pd
import datetime as dt
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()


# In[15]:


thor_wwii_data_clean=pd.read_csv("WW2_Missions/data/thor_wwii_data_clean.csv")


# In[16]:


thor_wwii_data_clean.columns


# In[17]:


thor_wwii_aircraft_gloss=pd.read_csv("WW2_Missions/data/thor_wwii_aircraft_gloss.csv")


# In[18]:


thor_wwii_aircraft_gloss.head(10)


# In[19]:


thor_wwii_weapon_gloss=pd.read_csv("WW2_Missions/data/thor_wwii_weapon_gloss.csv")


# In[20]:


thor_wwii_weapon_gloss.head()


# In[21]:


Summary_of_Weather=pd.read_csv("Weather/Summary_of_Weather.csv")


# In[22]:


Summary_of_Weather.head()


# In[23]:


# selecting the col needed from the Summary_of_Weather DF
Weather =pd.DataFrame(Summary_of_Weather,columns = ["STA", "Date","Precip","WindGustSpd","MaxTemp","MinTemp",
                                                   "MeanTemp", "Snowfall"])
Weather.head()


# In[24]:


# read the Weather_Station_Locations CSV file 
Weather_Station_Locations=pd.read_csv("Weather/Weather_Station_Locations.csv")

Weather_Station_Locations.head()


# In[25]:


# Celening the Weather_Station_Locations DF by droping the unwanted col
weather_station_loc = Weather_Station_Locations.drop(columns=["LAT","LON"])
weather_station_loc.head()


# In[26]:


weather_station_loc['STATE/COUNTRY ID'].unique()


# In[27]:


thor_wwii_weapon_gloss.head()


# In[28]:


# Droping un-needed col from the wepon gloss DF.
weapon_gloss = thor_wwii_weapon_gloss.drop(columns=["weapon_type","weapon_class","number_of_bomblets"])
weapon_gloss.head()


# In[29]:


#df['1/2 ID'] = df['1/2 ID'].str.upper()
weapon_gloss["weapon_name"] = weapon_gloss["weapon_name"].str.upper()
weapon_gloss.head(10)


# In[30]:


weapon_gloss.country.value_counts()


# In[31]:


weapon_gloss.weapon_name.value_counts()


# In[32]:


thor=thor_wwii_data_clean.copy()


# In[33]:


thor['database_edit_comments'].value_counts()


# In[34]:


del thor['database_edit_comments']


# In[35]:


thor['source'].value_counts()


# In[36]:


del thor['source']


# In[37]:


del thor['mission_comments']


# In[38]:


del thor['target_comment']


# In[39]:


del thor['misc_fail_ac']


# In[40]:


del thor['mech_fail_ac']


# In[41]:


del thor['wx_fail_ac']


# In[42]:


del thor['spares_return_ac']


# In[43]:


del thor['callsign']


# In[44]:


del thor['rounds_ammo']


# In[45]:


del thor['bda']


# In[46]:


del thor['sighting_method_code']


# In[47]:


del thor['time_over_target']


# In[48]:


del thor['sighting_explanation']


# In[49]:


del thor['naf']


# In[50]:


del thor['tgt_country_code']


# In[51]:


del thor['ac_dropping']


# In[52]:


del thor['msn_type']


# In[53]:


del thor['tgt_id']


# In[54]:


del thor['tgt_industry_code']


# In[55]:


del thor['tgt_industry']


# In[56]:


missions=thor.copy()
missions.columns


# In[57]:


com = pd.merge(missions, weapon_gloss, left_on = 'type_of_ic', right_on = "weapon_name")


# In[58]:


com['type_of_ic'].value_counts()


# In[59]:


missions['msndate'] = missions['msndate'].str.replace('-','')


# In[71]:


y = []
for x in missions['msndate']:
    y.append(int(x))
missions['msndate'] = y


# In[61]:


Summary_of_Weather["Date"]= Summary_of_Weather["Date"].str.split("-", n = 2, expand = False) 


# In[72]:


missions


# In[63]:


wd=Weather['Date'].values.tolist()
new=[]

for x in wd:
   year,month,day=x.split('-')
   if len(month)<2:
       month='0'+month
   if len(day)<2:
       day='0'+day
   new.append(int(year+month+day))


# In[65]:


Weather["Date"] = new


# In[66]:


type(Weather['Date'][1])


# In[67]:


Weather.head()


# In[100]:


engine = create_engine('mysql://group07:KnuUyh4WWRqHDxNY@cwru-data-project02.ciuevunbeloh.us-east-2.rds.amazonaws.com:3306/group07')
con = engine.connect()


# 
# mission.to_sql(mission, con,group07,index=False)

# In[103]:


missions.to_sql('mission', con, 'group07' ,index=False)

