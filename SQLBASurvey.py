import pandas as pd
import re
import os

# set your working directory
os.chdir(default_path) 
# load data
survey = pd.read_csv("survey_results_public.csv")

# convert fields to string format
survey['DevType'] = survey['DevType'].astype('str')
survey['DatabaseWorkedWith'] = survey['DatabaseWorkedWith'].astype('str')

#searches for business analyst in devtype and categorizes them
def CategorizeBA(x):
    if re.search(r'business analyst',x['DevType']):
        return 'Business Analyst'
    else:
        return  'Not Business Analyst'
    
#searches for SQL in database worked with and categorizes them
def CategorizeSQL(x): 
    if re.search(r'SQL',x['DatabaseWorkedWith']):
        return 'Works with SQL'
    else:
        return  'Does Not Work With SQL'

# categorizes business analysts
survey['Business Analyst'] = survey.apply(CategorizeBA, axis = 1)    
# categorizes SQL requirements
survey['Worked With SQL'] = survey.apply(CategorizeSQL, axis = 1)

#save to Excel file
survey.to_excel("SQL_for_BA_survey.xlsx", index=False) 