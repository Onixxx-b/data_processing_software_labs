# Personal Task
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.width', 1000)

print('Data reading. Also could include data merging.')
data = pd.read_csv('../data/Book_Dataset_1.csv')
with pd.option_context('display.max_rows', 20, 'display.max_columns', None):
    print(data)

print('Data tidying.')
# rename first column to "Id" and 'Avilability' to correct 'Availability'
data.rename(columns={'Unnamed: 0': 'Id', 'Avilability': 'Availability'}, inplace=True)

# convert columns Id,Price,Price_After_Tax,Tax_amount,Availability,Number_of_reviews,Stars to numeric
data[['Id', 'Price', 'Price_After_Tax', 'Tax_amount', 'Availability', 'Number_of_reviews', 'Stars']] = \
    data[['Id', 'Price', 'Price_After_Tax', 'Tax_amount', 'Availability', 'Number_of_reviews', 'Stars']].apply(pd.to_numeric)

with pd.option_context('display.max_rows', 20, 'display.max_columns', None):
    print(data)

print('Data analyzing with graphics.')
print('\nWhat are the column names of the data frame?')
print(data.columns.values)
print('How many books (i.e. rows) are in this data frame?')
print(len(data.index))
print('Extract the subset of rows of the data frame where "Stars" values are equal to 5')
print(data[data['Stars'] == 5])
print('What is the mean of the "Price" column in this dataset?')
print(data['Price'].mean())
# Show count of books for each "Stars" value
data.groupby('Stars', as_index=False).count().plot(x='Stars', y='Id', kind='bar')
plt.legend(labels=['Count of books'])
# Show first 15 books with 5 stars and availability more than 10
ax = data[(data['Stars'] == 5) & (data['Availability'] > 10)].plot(x='Title', y='Price', kind='barh')
ax.set_ylim([0, 15])
# plt.show()
