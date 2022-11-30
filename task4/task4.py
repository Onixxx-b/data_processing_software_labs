# Task 4. Getting and Clearning Data
import os
import pandas as pd

# Reading the data
pathdata = os.path.join("../data/UCI HAR Dataset")
xtrain = pd.read_csv(os.path.join(pathdata, "train", "X_train.txt"), sep="\\s+", header=None)
ytrain = pd.read_csv(os.path.join(pathdata, "train", "y_train.txt"), sep="\t", header=None)
subject_train = pd.read_csv(os.path.join(pathdata, "train", "subject_train.txt"), sep="\t", header=None)
xtest = pd.read_csv(os.path.join(pathdata, "test", "X_test.txt"), sep="\\s+", header=None)
ytest = pd.read_csv(os.path.join(pathdata, "test", "y_test.txt"), sep="\t", header=None)
subject_test = pd.read_csv(os.path.join(pathdata, "test", "subject_test.txt"), sep="\t", header=None)
features = pd.read_csv(os.path.join(pathdata, "features.txt"), sep=" ", header=None)
activityLabels = pd.read_csv(os.path.join(pathdata, "activity_labels.txt"), sep=" ", header=None)

xtrain.columns = features[1]
ytrain.columns = ["activityId"]
subject_train.columns = ["subjectId"]
xtest.columns = features[1]
ytest.columns = ["activityId"]
subject_test.columns = ["subjectId"]
activityLabels.columns = ['activityId', 'activityType']

merged_train = pd.concat([xtrain, subject_train, ytrain], axis=1)
merged_test = pd.concat([xtrain, subject_train, ytrain], axis=1)

# Tasks
print('\n1. Merges the training and the test sets to create one data set.')
merged_dataset = pd.concat([merged_train, merged_test], axis=0)
merged_dataset.index = range(len(merged_dataset))
print(merged_dataset)

print('\n2. Extracts only the measurements on the mean and standard deviation for each measurement.')
print(merged_dataset[[i for i in merged_dataset.keys() if 'mean()' in i or 'std()' in i]])

print('\n3. Uses descriptive activity names to name the activities in the data set')
merged_dataset = merged_dataset.merge(activityLabels, on='activityId')
print(merged_dataset)

print('\n4. Appropriately labels the data set with descriptive variable names')
print('Already done before merging datasets (see merged dataset in first task)')

print('\n5. From the data set in step 4, creates a second, independent tidy data set with the average '
      'of each variable for each activity and each subject.')
tidy_dataset = merged_dataset.groupby(['subjectId', 'activityId']).mean()
print(tidy_dataset)
