# pandas if library used for data manipulation, used for data analysis and data cleaning
# has 2 main data structures: series and data frames
# series is 1 dimensional array like object and data frame is 2 dimensional, size mutable potentially hetrogeneous

import pandas as pd
import numpy as np

# serios one dimensional array that can hold any data type similar to column in a table

data=[1,2,3,4]
series=pd.Series(data)
print('Series: ',series) # 2 cols indices and values
print(type(series))
# series from dictionary
dict={'a':1, 'b':2, 'c':3}
print(pd.Series(dict)) # key becomes the index so key and values
print(type(pd.Series(dict))) 

data=[10,20,30]
index=['a','b','c']
print(pd.Series(data,index=index))

# data frame 2 dimensional hetrogeneous mutable datau
# create a data fram from dictionary or list

data={'Name':['Krish',"John",'Jack'],'Age':[23,34,45],'City':['Banglore',"New York",'Texas']}
print(data)
print(pd.DataFrame(data))
dataframe=pd.DataFrame(data)
print(type(dataframe))
print(dataframe.shape)
print(np.array(dataframe))

# create a datafram from list of dictionaries

data=[{'Name':"Krish", 'Age':33, "City":'Banglore'},{'Name':"Madhav", 'Age':23, "City":'Delhi'},{'Name':"Rohit", 'Age':25, "City":'Texas'}]
data=pd.DataFrame(data)
print(data)
print(type(data))
# pd.read_csv() converts a csv file to data frame
# df.head(5) top 5 elements
# df.tail(5) last 5 elements

# accessing elements from dataframe
print(data)
print(data['Name']) # series
print(type(data['Name'])) # series data type

print(data.loc[0]) # first row
print(data.iloc(0)) # col

# accesing a specified element
print(data.at[1,'Age'])
print(data.at[0  ,'Age'])

# data manipulation with dataframes
print(data)
data['Salary']=['50000','70000','60000'] # adding a row
print(data)
data.drop('Salary', axis=1, inplace=True) # removing a column
# default axis is 0 for rows and 1 for columns
print(data)

## add age to a specified column
data['Age']=data['Age']+1
print(data)

#df.describe() statiscal summary for each column
