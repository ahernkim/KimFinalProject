import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings  ## Suppress warnings

# set working directory
os.chdir("C:\\Users\\ahernk1\\OneDrive - Dell Technologies\\Desktop\\Data Analytics for Business Course")
# print(os.getcwd())  # Print working directory
# print(os.listdir(os.getcwd()))  ##Print all of the files in the working directory


pd.set_option('display.max_columns', 20)  ## display max columns
pd.set_option('display.width',
              2000)  # sets the maximum width for a single field. Added in to help read CSV file in terminal
pp_2020 = pd.read_csv("PPR-2020-Cork.csv", index_col=0)  ##Read in Dataset. Set Index as Column 0
pp_2021 = pd.read_csv("PPR-2021-Cork.csv", index_col=0)  ##Read in Dataset. Set Index as Column 0
# print(pp_2020.dtypes) ##Check data types for csv 2020
# print(pp_2021.dtypes)


##Verifying the pp_2020 Dataset

# print(pp_2020.head()) #Preview the first 5 lines
# print(pp_2020.tail()) # Preview the last 5 lines
# print(pp_2020.columns) # to get the name of the columns
# print(pp_2020.shape) #Check shape of dataframe


# print(pp_2021.head()) #Preview the first 5 lines
# print(pp_2021.tail()) # Preview the last 5 lines
# print(pp_2021.columns)  # to get the name of the columns
# print(pp_2021.shape)  # Check shape of dataframe. Shape showing as (1403, 8)

pp_2020_tidy = pp_2020.rename(columns={'Price (�)': 'Price'})  ##Rename column headings
# print(pp_2020_tidy.columns)  ##verify new headings
# print(pp_2020_tidy.shape)  # verify shape of dataframe
pp_2020_tidy['Price'] = pp_2020_tidy['Price'].astype(str).astype(float)  # convert price column from object to float
# print(pp_2020_tidy.dtypes)


pp_2021_tidy = pp_2021.rename(columns={'Price (�)': 'Price'})  ##Rename column headings
pp_2021_tidy['Price'] = pp_2021_tidy['Price'].astype(str).astype(float)  ##Convert Price column from object to a string
# print(,pp_2021_tidy.dtypes)
# print(pp_2021_tidy.columns)  ##verify new headings
# print(pp_2021_tidy.shape)  # verify shape of dataframe

df_2020 = pp_2020_tidy.dropna(axis=1)  # dropping columns that contain NA values
# print(pp_2020.shape, df_2020.shape) #check shape

df_2021 = pp_2021_tidy.dropna(axis=1)  # dropping columns that contain NA values
# print(pp_2021_tidy.shape, df_2021.shape) ##Shows shape after columns have been dropped. Now showing as (1403,6)
# print(df_2021.shape) #Verify shape

# for index, row in dropcolumns.iterrows():  #Use Iterrows to loop over the DataFrame
# print(index)
# print(row)
#   print(f'Data Sold: {index},Property Description:{row.values}')

price_df = df_2020[["Price"]]  # sort columns using indexing operator
# print(check_df)

print("The means for property prices for the year 2020")

jan_df = price_df.loc["02/01/2020":"31/01/2020"]
jan_df_mean = jan_df.mean()
print("Januarys average house price was", jan_df.mean)
feb_df = price_df.loc["03/02/2020":"29/02/2020"]
feb_df_mean = feb_df.mean()
print("February's average house price was", feb_df.mean())
march_df = price_df.loc[("02/03/2020"):("31/03/2020")]
march_df_mean = march_df.mean()
print("March's average house price was", march_df.mean())
april_df = price_df.loc[("01/04/2020"):("30/04/2020")]
april_df_mean = april_df.mean()
print("Aprils average house price was", april_df.mean())
may_df = price_df.loc[("01/05/2020"):("29/05/2020")]
may_df_mean = may_df.mean()
print("Mays average house price was", may_df.mean())
june_df = price_df.loc[("01/06/2020"):("30/06/2020")]
june_df_mean = june_df.mean()
print("Junes average house price was", june_df.mean())
july_df = price_df.loc[("01/07/2020"):("31/07/2020")]
july_df_mean = july_df.mean()
print("Julys average house price was", july_df.mean())
aug_df = price_df.loc[("03/08/2020"):("31/08/2020")]
aug_df_mean = aug_df.mean()
print("August average house price was", aug_df.mean())
sept_df = price_df.loc[("01/09/2020"):("30/09/2020")]
sept_df_mean = sept_df.mean()
print("September average house price was", sept_df.mean())
oct_df = price_df.loc[("01/10/2020"):("31/10/2020")]
oct_df_mean = oct_df.mean()
print("October average house price was", oct_df.mean())
nov_df = price_df.loc[("01/11/2020"):("30/11/2020")]
nov_df_mean = nov_df.mean()
print("November average house price was", nov_df.mean())
dec_df = price_df.loc[("01/12/2020"):("31/12/2020")]
dec_df_mean = dec_df.mean()
print("December average house price was", dec_df.mean())

yr_review = pd.concat(
    [jan_df, feb_df, march_df, april_df, may_df, june_df, july_df, aug_df, sept_df, oct_df, nov_df, dec_df])
print(yr_review)

# Create a dictionary from the means.
data_mean_20 = {'Means': [240564.786401, 255561.398529, 255593.268327, 251242.985103,
                       257064.467909, 272570.637962, 245663.075518, 300831.322556, 266127.074665,
                       259095.3477, 267788.692462, 318739.068602],

             'Frame': ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'Nov',
                       'Dec']}

# Make dataframe from dictionary
data_df = pd.DataFrame(data_mean_20, columns=['Means', 'Frame'])

print(data_df)

# Plot new dataframe
#data_df.plot(x='Frame', y='Means')
#plt.title('The means of property prices sold 2020')
#plt.show()


## Getting the means of property prices sold in 2021
price_df21 = df_2021[["Price"]]  # sort columns using indexing operator
#print(price_df21)

print("The mean property prices for the year 2021")

jan_df21 = price_df21.loc["04/01/2021":"31/01/2021"]
jan_df21_mean = jan_df21.mean()
print(jan_df21_mean)

print("Januarys average house price was", jan_df21.mean)
feb_df21 = price_df21.loc["01/02/2021":"26/02/2021"]
feb_df21_mean = feb_df21.mean()
print("February's average house price was", feb_df21.mean())
march_df21 = price_df21.loc[("01/03/2021"):("31/03/2021")]
march_df_mean = march_df21.mean()
print("March's average house price was", march_df21.mean())
april_df21 = price_df21.loc[("01/04/2021"):("16/04/2021")]
april_df_mean = april_df21.mean()
print("Aprils average house price was", april_df21.mean())

data_mean_21 = {'Means': [278353, 261664, 271134, 247189],

             'Frame': ['Jan', 'Feb', 'March', 'April']}

# Make dataframe from dictionary
data_df21 = pd.DataFrame(data_mean_21, columns=['Means', 'Frame'])

print(data_df21)

# Plot new dataframe
data_df21.plot(x='Frame', y='Means')
plt.title('The means of property prices sold 2021')
plt.show()




# Created a new dataset selecting only rows with New Dwelling.
description_2020 = df_2020[df_2020["Description of Property"] == "New Dwelling house /Apartment"]
description_2021 = df_2021[df_2021["Description of Property"] == "New Dwelling house /Apartment"]

#   print(description_2020.head()) # Check the first 5 rows
#   print(description_2020.shape) ##Check the shape of my new dataset. Showing as (1192,6)

# print(description_2021.head())
# print(description_2021.shape) ##Check the shape of my new dataset. Showing as (189,6)

merge = description_2020.append(description_2021)  ##Merged the two datasets together
print(merge.head())
# print(merge.tail())
# print(merge.shape)  # shape now showing as (1381,6)

max_price = merge['Price'].max()
print("The Maximum a new house or apartment was sold for in Cork between 2020 and 2021 was", max_price)
min_price = merge['Price'].min()
print("The Minimum a new house or apartment was sold for in Cork between 2020 and 2021 was", min_price)

print("The Average House Price in 2020 was ", df_2020["Price"].mean())
print("The Average House Price so far in 2021 is ", df_2021["Price"].mean())

## Create Numpy Array from house prices in December
check_df = df_2020[["Price"]]  # sort columns using indexing operator
print(check_df)

december_df = check_df.loc[("01/12/2020"):("31/12/2020")]  #
#   print("Printing all houses sold in December 2020", first)
# print(first.head())
# print(check.shape)
december_price = np.array(december_df[1:], dtype=float)  ##Create numpy array using prices from December
# print(december_price)

december_mean = np.mean(december_price)
december_min = np.min(december_price)
december_max = np.max(december_price)
print("The Average house sold in december 2020 was", december_mean)
print("The Minimum house sold in december 2020 was", december_min)
print("Maximum house sold in december 2020 was ", december_max)

november_df = check_df.loc[("01/11/2020"):("30/11/2020")]  #
# print("Printing all houses sold in November 2020", first)
# print(check.shape)

## Create Numpy Array from house prices in November
november_price = np.array(november_df[1:], dtype=float)  ##Create numpy array using prices from December
# print(november_price)
november_mean = np.mean(november_price)
november_min = np.min(november_price)
november_max = np.max(november_price)
print("The Average house sold in November 2020 was", november_mean)
print("The Minimum house sold in November 2020 was", november_min)
print("Maximum house sold in November 2020 was ", november_max)

if november_max > december_max:
    print("The month of November sold a more expensive house than december")
    print("It was", november_max - december_max, "more expensive")

else:
    print("December sold a more expensive house than November")
    print("It was", december_max - november_max, "more expensive")

if november_min < december_min:
    print("The month of November sold a cheaper house than december")
    print("It was", december_min - november_min, "more cheaper")

else:
    print("December sold a more cheaper house than November")
    print("It was", november_min - december_min, "cheaper")

if november_mean > december_mean:
    print("The month of November had a higher average house price")
    print("It was", november_max - december_max, "more")

else:
    print("December had higher average per house sold than November")
    print("It was", december_max - november_max, "higher")




# np_property = df_2020[df_2020['Description of Property']].to_numpy()

# print(df_2020.shape)

# row = df_2020.iloc[4:8]
# print(row)
