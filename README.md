# MissionWiredFeb2023
These two pieces of code are used to as part of the response for the Data Engineer Exercises:

main.py
Read in simulated CRM datasets and create a data file with:
* email : primary email address
* code : source code
* is_unsub : is the associated email address unsubscribed?
* created_dt : datetime the person was created in the dataset
* updated_dt : datetime the person was last updated in the dataset
The output file is 'people.csv'

acquisition_facts.py
Read in the output from main.py (or another file with a column of dates) and output a file with:
* acquisition_date : a list of all the calendar dates that people were created in the dataset
* acquisitions : the number of constituents that were acquired on that date
The output file is 'acquisition_facts.csv'

To run these files locally, you need to install the following python packages:
pandas
datetime

The following files that were provided in the exercise must be present in a 'data' directory within the directory of the *.py files.
* cons.csv
* cons_email.csv
* cons_email_chapter_subscription.csv

