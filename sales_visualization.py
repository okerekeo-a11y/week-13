"""
Ogechukwu Okereke
CMSC 111
Week 13 Assignment2
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

print("Sales Data:")
print(df)
daily_sales = df.groupby("date")["sales"].sum()

plt.figure()
plt.plot(daily_sales.index, daily_sales.values, marker="o")
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure()
plt.hist(df["sales"], bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

