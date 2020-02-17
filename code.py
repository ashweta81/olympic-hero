# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)

#Code starts here
data.rename(columns={'Total':'Total_Medals'}, inplace=True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer', (np.where(data['Total_Summer']<data['Total_Winter'], 'Winter','Both')))
data['Better_Event'].value_counts()
better_event='Summer'


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries=top_countries.drop(top_countries.index[-1])
def top_ten(input_df,column_name):
    country_list=[]
    country_list=input_df.nlargest(10,column_name)['Country_Name'].tolist()
    return country_list
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=[i for i in top_10_summer if i in top_10_winter and i in top_10]


# --------------
#Code starts here

#For Summer

#Creating the dataframe for Summer event
summer_df= data[data['Country_Name'].isin(top_10_summer)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

#Changing the graph title
plt.title('Top 10 Summer')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')


#For Winter

#Creating the dataframe for Winter event
winter_df=data[data['Country_Name'].isin(top_10_winter)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

#Changing the graph title
plt.title('Top 10 Winter')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')



#For both the events

#Creating the dataframe for both the events
top_df=data[data['Country_Name'].isin(top_10)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])

#Changing the graph title
plt.title('Top 10')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')





# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()


summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].values[0]

print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].values[0]
print(winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'].values[0]
print(top_country_gold)


# --------------
#Code starts here
#print(data.shape)
data_1=data.drop(data.index[-1])
#print(data_1.shape)
data_1['Total_Points']= (3*(data_1['Gold_Total'])+ 2*(data_1['Silver_Total']) + 1*(data_1['Bronze_Total']))
most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points'] == most_points]['Country_Name'].values[0]
print(best_country)


# --------------
#Code starts here
best=data.loc[data.Country_Name==best_country, ['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


