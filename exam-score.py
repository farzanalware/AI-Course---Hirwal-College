import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Histogram 
data = np.random.normal(70,10,1000)
plt.hist(data, bins = 30 , edgecolor="Red",
alpha=0.7, color="#306998")
plt.title("Exams Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.axvline(data.mean(), color ="Red",
            linestyle="--", lable ="Mean")
plt.legend()
plt.show()


#----------------------------#

import matplotlib.pyplot as plt 
import numpy as np
# Line Plot
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.title("Trigonometric Functions")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.grid(True)
plt.show()

#---------------------------#

import numpy as np
# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 4))
d = np.arange(0, 10, 2)
e = np.linspace(0, 1, 5)
# Array properties
print(a.shape)
print(a.dtype)
print(a.ndim)
# Reshaping
matrix = np.arange(12).reshape(3, 4)
print(matrix)

#----------------------------#
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# Basic indexing
print(arr[0])
print(arr[-1])
print(arr[1:4])
# 2D indexing
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m[1, 2])
print(m[:, 1])
print(m[0:2, :])
# Boolean masking
scores = np.array([85, 42, 91, 67, 73])
passed = scores[scores >= 70]
print(passed)
# Fancy indexing
idx = [0, 3, 4]
print(arr[idx])


#--------------------------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import os

# read Datasets
df = pd.read_csv("retail_store_sales.csv")

# Basic Inspections
print(df)
print(df.info())
print(df.describe())

# Missing Values
print(df.isnull().mean())
print(df.isnull().mean()*100)

# Check duplicates (added missing parentheses)
df[df.duplicated]
df1 = df

# Data cleaning
df1.head(15)
df2 = df1.drop(columns=["Transaction ID"])
df2.head(15)
