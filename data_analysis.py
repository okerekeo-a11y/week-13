"""
Ogechukwu Okereke
CMSC 111
Week 13 Assignment2
"""
import pandas as pd
df = pd.read_csv("employee_data.csv")
print("First 5 rows:")
print(df.head())
print("\nMissing values per column:")
print(df.isna().sum())
average_salary = df["salary"].mean()
df["salary"].fillna(average_salary, inplace=True)
df["age"].fillna(df["age"].mean(), inplace=True)
print("\nData after handling missing values:")
print(df)
filtered = df[(df["department"] == "IT") & (df["salary"] > 65000)]
print("\nFiltered (IT + salary > 65000):")
print(filtered)
sorted_data = filtered.sort_values(by="salary", ascending=False)
print("\nSorted by salary (descending):")
print(sorted_data)
final_average = df["salary"].mean()
print("\nAverage salary after cleaning:")
print(final_average)