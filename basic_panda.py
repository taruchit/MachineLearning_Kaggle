import pandas as pd

#Save the file path in a variable
melbourne_file_path='melb_data.csv'

#Read data from file and store in DataFrame
melbourne_data=pd.read_csv(melbourne_file_path)

#Print summary of data
print(melbourne_data.describe())

#Print list of all columns in dataset
print(melbourne_data.columns)

#dropna drops missing values
melbourne_data=melbourne_data.dropna(axis=0)

print(melbourne_data.columns)

