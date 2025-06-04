import pandas as pd

#Load the 2 datasets
preliminary_data = pd.read_csv("./gdp_per_worker/project_data/preliminary_data.csv")
final_data_uncleaned = pd.read_csv("./gdp_per_worker/project_data/final_data.csv")

columns_to_drop = [ #These are duplicate columns in the 2 files, remove before merge
    "X3 - True Value Disposable Income",
    "Y -  Nominal GDP Per Worker"
]

final_data = final_data_uncleaned.drop(columns = columns_to_drop) #Drop the 2 columns

#Merge the datasets and save
merged_data = pd.merge(preliminary_data, final_data, on = "STATE/PROVINCE", how = "outer")
merged_data.to_csv("merged_gdp_data.csv", index = False)
