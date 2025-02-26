# -*- coding: utf-8 -*-
"""CognitiveASS(7).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/github/Aditi31kapil/Cognitive_Computing/blob/main/CognitiveASS(7).ipynb

Ques 1
"""

import numpy as np
import pandas as pd

roll_number = 102317261
np.random.seed(roll_number)

"""Part 1"""

# Creating DataFrame
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']
sales_data = np.random.randint(1000, 5001, (12, 4))
sales_df = pd.DataFrame(sales_data, columns=categories, index=months)

"""Part II"""

print(sales_df.head())
print(sales_df.describe())

total_sales_category = sales_df.sum()
print("Total sales per category:\n", total_sales_category)

sales_df['Total Sales'] = sales_df.sum(axis=1)
print("Total sales per month:\n", sales_df['Total Sales'])

average_growth = sales_df.pct_change().mean()

print("\nAverage sales growth between consecutive months:")
print(average_growth)

sales_df['Growth Rate'] = sales_df['Total Sales'].pct_change() * 100  # Percentage change

print("Percentage change in Total Sales from the previous month.:\n", sales_df['Growth Rate'])#since no month before january

if roll_number % 2 == 0:
    sales_df['Electronics'] *= 0.9  # 10% discount
else:
    sales_df['Clothing'] *= 0.85  # 15% discount

print("\nSales data after discount:")
print(sales_df)

"""Part III"""

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 5))
sales_df[categories].plot(marker='o')
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.legend()
plt.grid()
plt.show()

# Boxplot for sales distribution
plt.figure(figsize=(8, 5))
sns.boxplot(data=sales_df[categories])
plt.title("Sales Distribution by Category")
plt.show()

"""Ques 2"""

array = np.array([[1, -2, 3],[-4, 5, -6]])
print("Element-wise absolute:", np.abs(array))

flattened_array = array.flatten()
print("Percentiles:", np.percentile(flattened_array, [25, 50, 75]))
print("Mean:", np.mean(flattened_array))
print("Median:", np.median(flattened_array))
print("Standard Deviation:", np.std(flattened_array))

"""Ques 3"""

a = np.array([-1.8, -1.6, -0.5, 0.5,1.6, 1.8, 3.0])
print("Floor:", np.floor(a))
print("Ceiling:", np.ceil(a))
print("Truncated:", np.trunc(a))
print("Rounded:", np.round(a))

"""Ques 4"""

def swap_list_elements(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp
    return lst

example_list = [1, 2, 3, 4, 5]
print("Before Swap:", example_list)
print("After Swap:", swap_list_elements(example_list, 1, 3))

"""Ques 5"""

example_set = {10, 20, 30, 40, 50}
example_list = list(example_set)
example_list[0], example_list[1] = example_list[1], example_list[0]
example_set = set(example_list)
print("Swapped Set:", example_set)