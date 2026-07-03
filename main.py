# CLEAN AND PROCESS DATA

# import the pandas library
import pandas as pd

# read the excel file
df = pd.read_excel("sales_Dataset_500_Records.xlsx")

#display the first 5 rows
print(df.head())

#display the last 5 row
print("\n=======last 5 row========")
print(df.tail())

#display the shape(row and columns)
print("\n====== dataset shape======")
print(df.shape)

#display column namaes
print("\n======column name=======")
print(df.columns)

#display data types
print("\n======data types======")
print(df.dtypes)

# Display complete information about the dataset
print("\n========== DATASET INFORMATION ==========")
df.info()

# Display data types
print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Display complete information
print("\n========== DATASET INFORMATION ==========")
df.info()

# Check for duplicate rows
print("\n========== DUPLICATE RECORDS ==========")

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)

# Summary statistics
print("\n========== SUMMARY STATISTICS ==========")
print(df.describe()) 

 #INDENTIFY SALES TRENDS
 
 # Total Sales
total_sales = df["Sales"].sum()

# Total Profit
total_profit = df["Profit"].sum()

print("\n========== BUSINESS OVERVIEW ==========")
print("Total Sales: ", round(total_sales, 2))
print("Total Profit: ", round(total_profit, 2))

# Convert Order Date to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create a new column for Month
df["Month"] = df["Order Date"].dt.month_name()

# Create a new column for Month Number (for correct sorting)
df["Month Number"] = df["Order Date"].dt.month

# Group sales by month
monthly_sales = df.groupby(["Month Number", "Month"])["Sales"].sum().reset_index()

# Sort by month number
monthly_sales = monthly_sales.sort_values("Month Number")

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# Find the month with the highest sales
highest_month = monthly_sales.loc[monthly_sales["Sales"].idxmax()]

# Find the month with the lowest sales
lowest_month = monthly_sales.loc[monthly_sales["Sales"].idxmin()]

print("\n========== SALES TREND ANALYSIS ==========")
print(f"Highest Sales Month : {highest_month['Month']} ({highest_month['Sales']:.2f})")
print(f"Lowest Sales Month  : {lowest_month['Month']} ({lowest_month['Sales']:.2f})")

import matplotlib.pyplot as plt

# Create a figure
plt.figure(figsize=(10, 5))

# Plot Monthly Sales
plt.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o"
)

# Add title
plt.title("Monthly Sales Trend")

# Label X-axis
plt.xlabel("Month")

# Label Y-axis
plt.ylabel("Sales")

# Add grid
plt.grid(True)

# Rotate month names
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Display chart
plt.savefig("charts/monthly_sales_trend.png")
plt.show()


# ANALYZE TOP-SELLING PRODUCTS

# Group data by Product and calculate total sales
top_products = df.groupby("Product")["Sales"].sum()

# Sort products by sales in descending order
top_products = top_products.sort_values(ascending=False)

# Display the Top 10 products
print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(top_products.head(10))

# Create a bar chart for Top Selling Products

plt.figure(figsize=(10,5))

top_products.plot(kind="bar")

plt.title("Top Selling Products")

plt.xlabel("Product")

plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("charts/top_products.png")

plt.show()

# Group by Product and calculate total quantity sold
top_quantity = df.groupby("Product")["Quantity"].sum()

# Sort in descending order
top_quantity = top_quantity.sort_values(ascending=False)

print("\n========== TOP PRODUCTS BY QUANTITY ==========")
print(top_quantity)

# Group by Category and calculate total sales
category_sales = df.groupby("Category")["Sales"].sum()

# Sort categories by sales
category_sales = category_sales.sort_values(ascending=False)

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

# Create a bar chart for Sales by Category

plt.figure(figsize=(8,5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/sales_by_category.png")

plt.show()

# Group by Category and calculate total profit
category_profit = df.groupby("Category")["Profit"].sum()

# Sort categories by profit
category_profit = category_profit.sort_values(ascending=False)

print("\n========== PROFIT BY CATEGORY ==========")
print(category_profit)

# Create a bar chart for Profit by Category

plt.figure(figsize=(8,5))

category_profit.plot(kind="bar")

plt.title("Profit by Category")

plt.xlabel("Category")

plt.ylabel("Profit")

plt.xticks(rotation=0)

plt.tight_layout()

plt.tight_layout()

plt.savefig("charts/profit_by_category.png")

plt.show()

plt.show()

# Group by Region and calculate total sales
region_sales = df.groupby("Region")["Sales"].sum()

# Sort regions by sales
region_sales = region_sales.sort_values(ascending=False)

print("\n========== SALES BY REGION ==========")
print(region_sales)

# Create a bar chart for Sales by Region

plt.figure(figsize=(8,5))

region_sales.plot(kind="bar")

plt.title("Sales by Region")

plt.xlabel("Region")

plt.ylabel("Total Sales")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/sales_by_region.png")

plt.show()

# Group by Region and calculate total profit
region_profit = df.groupby("Region")["Profit"].sum()

# Sort by profit
region_profit = region_profit.sort_values(ascending=False)

print("\n========== PROFIT BY REGION ==========")
print(region_profit)

# Create a bar chart for Profit by Region

plt.figure(figsize=(8,5))

region_profit.plot(kind="bar")

plt.title("Profit by Region")

plt.xlabel("Region")

plt.ylabel("Total Profit")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("charts/profit_by_region.png")

plt.show()