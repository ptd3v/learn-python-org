#This is a summary of content and completed test exercise from learnpython.org

#Pandas Basics
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

#Set brics index
brics.index = ["BR", "RU", "IN", "CH", "SA"]

#Print out brics with new index values
print(brics)

#Import pandas as pd
import pandas as pd

#Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

#Print out cars
print(cars)

#Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#Print out country column as Pandas Series
print(cars['cars_per_cap'])

#Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

#Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

#Series can only contain single list with index, whereas dataframe can be made of more than one series
#Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#Print out first 4 observations
print(cars[0:4])

#Print out fifth and sixth observation
print(cars[4:6])

#You can also use loc and iloc to perform just about any data selection operation. loc is label-based, which means that you have to specify rows and columns based on their row and column labels. iloc is integer index based, so you have to specify rows and columns by their integer index like you did in the previous exercise.

#Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#Print out observation for Japan
print(cars.iloc[2])

#Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])