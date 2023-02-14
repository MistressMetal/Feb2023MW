import pandas as pd
from datetime import datetime

# read in the data files
df_cons = pd.read_csv('data/cons.csv', usecols = ['cons_id', 'source',
       'create_dt', 'modified_dt'])
df_cons_email = pd.read_csv('data/cons_email.csv', usecols=['cons_email_id', 'cons_id', 'is_primary', 'email'])
df_cons_email_chapter = pd.read_csv('data/cons_email_chapter_subscription.csv', usecols=['cons_email_id', 'chapter_id',
       'isunsub'])

# we are only interested in records where the 'chapter_id' is 1
df_cons_email_chapter = df_cons_email_chapter.loc[df_cons_email_chapter['chapter_id']==1]

# join the df_cons_email to the df_cons_email_chapter.
# the join is on df_cons_email_chapter because a 'chapter_id' value of 1 is needed, and this field is only in df_cons_email_chapter
df_people_emails = pd.merge(df_cons_email, df_cons_email_chapter, how='right', on='cons_email_id')

# join the df_people_emails to the df_cons_id_keep
# the join is on the df_people because a 'chapter_id' value of 1 is needed, and this field is only in df_people_emails
df_people = pd.merge(df_cons, df_people_emails, how='right', on='cons_id')

# we are only interested in the records with the primary email
df_people = df_people.loc[df_people['is_primary']==1]

# collect the relevant fields
data={'email': df_people['email'],
      'code': df_people['source'],
      'is_unsub': df_people['isunsub'],
      'created_dt' : df_people['create_dt'],
      'updated_dt' : df_people['modified_dt']}

# create the DF and reset the index
df_people_output=pd.DataFrame(data=data)
df_people_output.reset_index(inplace=True)
df_people_output.drop(['index'], axis=1, inplace=True)

# convert dates to datetime type
df_people_output['updated_dt']=df_people_output['updated_dt'].apply(lambda x: datetime.strptime(x, '%a, %Y-%m-%d %H:%M:%S'))
df_people_output['created_dt']=df_people_output['created_dt'].apply(lambda x: datetime.strptime(x, '%a, %Y-%m-%d %H:%M:%S'))

# save to csv
df_people_output.to_csv('people.csv', index=False)