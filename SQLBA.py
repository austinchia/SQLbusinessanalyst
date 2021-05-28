import pandas as pd
import re
import os

# load data
os.chdir(default_path)
ba = pd.read_csv("BusinessAnalyst2.csv")

#filters out data analyst positions
ba_noda = ba[~ba['Job Title'].str.contains('Data Analyst')] 

#removes line breaks
ba_noda['Job Description'] = ba_noda['Job Description'].replace("\n", " ") 

#searches for SQL in job description and categorizes them
def CategorizeSQL(x): 
    if re.search(r'SQL',x['Job Description']):
        return 'Requires SQL'
    else:
        return  'Does Not Require SQL'
    
# apply categorize function
ba_noda['SQL Requirement'] = ba_noda.apply(CategorizeSQL, axis = 1)

#save to Excel file
ba_noda.to_excel("SQL_for_BA.xlsx", index=False) 