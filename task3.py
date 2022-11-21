# Task 3. Tidying data
import pandas as pd

hike_data = pd.read_csv('data/hike_long.csv')

# Tidying dataset
# Create a new dataset clean_hike_trails with the next updates:
clean_hike_trails = hike_data
# 1. Convert columns gain, highpoint, rating to numeric values.
clean_hike_trails[['rating', 'highpoint', 'gain']] = clean_hike_trails[['rating', 'highpoint', 'gain']] \
    .apply(pd.to_numeric)


# 2. Add new column trip with the type of trip from column length (“roundtrip”, “trails”, “one-way”).


def get_trip_value(length):
    if length.find('roundtrip') != -1:
        return 'roundtrip'
    elif length.find('trails') != -1:
        return 'trails'
    elif length.find('one-way') != -1:
        return 'one-way'
    else:
        return None


clean_hike_trails['trip'] = clean_hike_trails['length'].apply(get_trip_value)
# 3. Add new column length_total with the route length from column length, considering
# that for “one-way” trip you must double the route length.
clean_hike_trails['length_total'] = pd.to_numeric(clean_hike_trails['length'].str.split(' ').str[0])
clean_hike_trails['length_total'] = clean_hike_trails.apply(lambda x: x['length_total'] * 2 if x['trip'] == 'one-way'
else x['length_total'], axis=1)
# 4. Add new column location_general with location from column location (a part before “–”).
clean_hike_trails["location_general"] = clean_hike_trails["location"].str.split(" -- ").str[0]
# 5. Add column id with row number
clean_hike_trails["row_id"] = clean_hike_trails.index


# Questioning dataset

print('Question 1. How many routes have rating more than 4.9')
print(len(clean_hike_trails[clean_hike_trails['rating'] > 4.9]))

print('Question 2. How many routes are “Good for kids” (hint: you can use (unnest function)?')
print(len(clean_hike_trails[clean_hike_trails["features"].str.contains("Good for kids")]))

print('Question 3. Which unique features can routes have?')
print(clean_hike_trails.drop_duplicates("features")["features"].tolist())

print('Question 4. What is the most common rating of a route?')
print(clean_hike_trails["rating"].value_counts().head(1))

print("Question 5. Your own question and answer: how many routes have 'Mount Rainier Area' location?")
print(len(clean_hike_trails[clean_hike_trails["location_general"] == 'Mount Rainier Area']))
