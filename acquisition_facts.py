import pandas as pd
from datetime import datetime

# read in the data file (this file can be created using main.py)
df_people = pd.read_csv('people.csv')

# convert the created date into just the calendar day
df_people['created_dt'] = df_people['created_dt'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
df_people['created_dt'] = pd.to_datetime(df_people['created_dt']).dt.date

# create a series with the count of each of the values in 'created_dt'
df_acquisition_counts=df_people['created_dt'].value_counts()

# print the series to a csv file
df_acquisition_counts.to_csv('acquisition_facts.csv', index_label=['acquisition_date'], header=['acquisitions'])
