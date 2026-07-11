import numpy as np
import pandas as pd

# importing data from csv file

# df=pd.read_csv('path of the file')
# df.head(5)  first 5 rows of the dataset
# df.tail(5) last 5 rows of the dataset
# df.describe() statistical summary of the dataset
# df.dtypes() tells us about the data type of each column

# handling missing values

# in actual dataset there are a lot of chances that it might contain missing values
# df.isnull() 
# gives boolean dataset True for null/missing False for not null

# df.isnull().sum() gives how many values are null the count of the null values

# df.fillna(0) giving default 0 value to the missing values
# df_filled=df.fillna(0) good practice to store the new dataset separately

# filling missing values with the mean of the column