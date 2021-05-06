
import os
import pandas as pd
import numpy as np
import warnings  ## Suppress warnings

os.chdir("C:\\Users\\ahernk1\\OneDrive - Dell Technologies\\Desktop\\Data Analytics for Business Course")
os.getcwd()

#for root, dirs, files in os.walk("."):
#  for filename in files:
 #      print(filename)

#pd.set_option('display.max_columns', 20)  ## display max columns
pd.set_option('display.width', 2000)  #sets the maximum width for a single field. Added in to help read CSV file in terminal
garda_data = pd.read_csv("IRELAND_CRIME_GARDA_DIVISION_wise_2003-2019.csv")
#print(garda_data.head()) ##Display the top 5 rows
#print(garda_data.shape)  ## Check the shape of the dataset
#print(garda_data.tail()) ##Check the bottom 5 rows

#print(garda_data.columns) # to get the name of the columns
print(garda_data.dtypes) ##Check the data type of each column

print(garda_data["REGION"].head()) ##Show only one column of the dataset. Showing REGION
#df1 =pd.DataFrame({
#   "city":["new york","chicago","orlando", "dublin", "galway"],
#    "temperature": [21,14,35, 28, 19],
#    "humidity" : [67,89,90,78,54]
#)
#print(df1)

#type(df1)
