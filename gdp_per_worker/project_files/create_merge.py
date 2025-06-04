import pandas as pd

#Load the 2 datasets
preliminary_data = pd.read_csv("../project_data/preliminary_data.csv")
final_data_uncleaned = pd.read_csv("../project_data/final_data.csv")

columns_to_drop = [ #These are duplicate columns in the 2 files, remove before merge
    "X3 - True Value Disposable Income",
    "Y -  Nominal GDP Per Worker"
]

final_data = final_data_uncleaned.drop(columns = columns_to_drop) #Drop the 2 columns

#Merge the datasets and save
merged_data = pd.merge(preliminary_data, final_data, on = "STATE/PROVINCE", how = "outer")

#Column ordering in merged_data
column_order = [
    "STATE/PROVINCE",
    "Y -  Nominal GDP Per Worker",
    "X1 - % Workforce in STEM",
    "X2 - Urbanization Rate (%)",
    "X3 - True Value Disposable Income",
    "GDP Total",
    "Employment Total",
    "Disposable Income",
    "$USD True Value"
]

merged_data = merged_data[[column for column in column_order if column in merged_data.columns]]

#Make sure your inside project_files folder before running 
merged_data.to_csv("../project_data/merged_gdp_data.csv", index = False)
