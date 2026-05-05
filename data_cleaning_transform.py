"""
Ogechukwu Okereke
CMSC 111
Week 13 Assignment1
"""
import pandas as pd
df = pd.read_csv("sales_data.csv")
print("First 5 rows:")
print(df.head())
print("\nMissing values per column:")
print(df.isna().sum())
df["units_sold"] = df["units_sold"].fillna(df["units_sold"].median())
df["unit_price"] = df["unit_price"].fillna(df["unit_price"].mean())

print("\nData after filling missing values:")
print(df)
rows_before = len(df)
df_cleaned = df.drop_duplicates()
rows_after = len(df_cleaned)

print("\nRows before removing duplicates:", rows_before)
print("Rows after removing duplicates:", rows_after)

print("\nData after removing duplicates:")
print(df_cleaned)
original_cleaned = df_cleaned.copy()
encoded_df = pd.get_dummies(df_cleaned, columns=["region", "product"])

print("\nColumns after one-hot encoding:")
print(encoded_df.columns)

print("\nData after one-hot encoding:")
print(encoded_df)
for column in ["units_sold", "unit_price"]:
    encoded_df[column] = (
        (encoded_df[column] - encoded_df[column].min()) /
        (encoded_df[column].max() - encoded_df[column].min()))
print("\nData after normalizing units_sold and unit_price:")
print(encoded_df)
summary = original_cleaned.groupby("region").agg(
    total_units_sold=("units_sold", "sum"),
    average_unit_price=("unit_price", "mean"))
print("\nSummary statistics by region:")
print(summary)