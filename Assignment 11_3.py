# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:30:09 2018

@author: Malini
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:28:57 2018
Assignment 11
@author: Malini
"""

import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})

print(df)

'''#1. Some values in the the FlightNumber column are missing. These numbers are meant
to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
these missing numbers and make the column an integer column (instead of a float
column)'''
                                                             
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)  
print(df['FlightNumber'])                                      
                               
'''2. The From_To column would be better as two separate columns! Split each string on
the underscore delimiter _ to give a new temporary DataFrame with the correct values.
Assign the correct column names to this temporary DataFrame.'''

df2 = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn']})                      
df2[['From','To']] = df2.From_To.str.split("_",expand=True,)
print(df2)

'''3. Notice how the capitalisation of the city names is all mixed up in this temporary
DataFrame. Standardise the strings so that only the first letter is uppercase (e.g.
"londON" should become "London".)
'''


df2['From'] = df2['From'].str.lower().str.title()
print(df2)

'''4. Delete the From_To column from df and attach the temporary DataFrame from the
previous questions.'''

# Delete the From_To Column from df
df = df.drop('From_To',1)
print(df)

# attach the temporary DataFrame from the previous questions

df = [df,df2]
Final_df=pd.concat(df, sort = 'false')
print(Final_df)

'''5. In the RecentDelays column, the values have been entered into the DataFrame as a
list. We would like each first value in its own column, each second value in its own
column, and so on. If there isn't an Nth value, the value should be NaN.
Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
delay_2, etc. and replace the unwanted RecentDelays column in df with delays.
'''
# Expand column into temporary Dataframe
df_Delay = Final_df['RecentDelays'].apply(pd.Series)

# Integrate temp columns back into original Dataframe (while naming column)
for col in df_Delay:
    Final_df["RecentDelays%d" % (col+1)] = df_Delay[col]
print(Final_df)

# replace the unwanted RecentDelays column in df with delays
Final_df = Final_df.drop('RecentDelays',1)
print(Final_df)