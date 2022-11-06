# Task 1. Exploraring a dataset
import pandas as pd

air_quality = pd.read_csv('airquality.csv')

print('Question 1. What are the column names of the data frame?')
print(air_quality.columns.values)

print('Question 2. What are the row names of the data frame?')
print(list(air_quality.index))

print('Question 3. Extract the first 6 rows of the data frame and print them to the console')
print(air_quality.head(6))

print('Question 4. How many observations (i.e. rows) are in this data frame?')
print(len(air_quality.index))

print('Question 5. Extract the last 6 rows of the data frame and print them to the console')
print(air_quality.tail(6))

print('Question 6. How many missing values are in the “Ozone” column of this data frame?')
print(air_quality['Ozone'].isnull().sum())

print('Question 7. What is the mean of the “Ozone” column in this dataset? Exclude missing values (coded as NA) from '
      'this calculation.')
print(air_quality.dropna(subset=['Ozone'])['Ozone'].mean())

print('Question 8. Extract the subset of rows of the data frame where Ozone values are above 31 and Temp values are '
      'above 90.')
print(air_quality[(air_quality['Ozone'] > 31) & (air_quality['Temp'] > 90)])

print('Question 9. Use a for loop to create a vector of length 6 containing the mean of each column in the data frame '
      '(excluding all missing values).')
means = []
for col in air_quality.columns.values:
    means.append(air_quality.dropna(subset=[col])[col].mean())
print(means)

print('Question 10. Use the apply function to calculate the standard deviation of each column in the data frame '
      '(excluding all missing values).')
stds = []
for col in air_quality.columns.values:
    stds.append(air_quality.dropna(subset=[col])[col].std())
print(stds)

print('Question 11. Calculate the mean of “Ozone” for each Month in the data frame and create a vector '
      'containing the monthly means (exclude all missing values).')
monthly_means = []
for month in range(1, 13):
    monthly_means.append(air_quality[(air_quality['Ozone'].notnull()) & (air_quality['Month'] == month)]['Ozone']
                         .mean())
print(monthly_means)

print('Question 12. Draw a random sample of 5 rows from the data frame')
print(air_quality.sample(5))
