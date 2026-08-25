# 🐍 Python Data Analysis

<h1 align="center">Python Data Analysis</h1>

<p align="center">
  <b>NumPy • Pandas • Matplotlib • Seaborn</b>
</p>

<p align="center">
  A practical Python project covering array operations, data analysis,
  data cleaning, and data visualization.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.x-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=for-the-badge\&logo=python\&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13+-4C72B0?style=for-the-badge)

</p>

---

# 📌 About

This repository contains my practical learning and implementation of **Python Data Analysis**.

The project combines multiple concepts into one complete Python program, including:

* 🔢 NumPy
* 🐼 Pandas
* 🧹 Data Cleaning
* 📊 Data Analysis
* 📈 Data Visualization
* 📂 CSV Dataset Handling

The main goal is to move from individual Python concepts to a practical **data analysis workflow**.

---

# 🧠 Learning Journey

```text
Python
   │
   ▼
NumPy
   │
   ▼
Pandas
   │
   ▼
Data Cleaning
   │
   ▼
Data Visualization
   │
   ▼
Data Analysis
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Machine Learning
   │
   ▼
Data Science
```

---

# 🚀 Features

## 🔢 NumPy Practice

* Array creation
* Array properties
* Reshaping
* Indexing
* Slicing
* 2D array operations
* Boolean masking
* Fancy indexing

## 🐼 Pandas Practice

* DataFrame creation
* Filtering
* Sorting
* Creating new columns
* GroupBy
* Aggregation
* Renaming columns

## 🧹 Data Cleaning

* CSV file loading
* Column name standardization
* Dataset inspection
* Statistical summary
* Missing-value detection
* Duplicate detection
* Column removal
* Conditional data cleaning

## 📊 Visualization

* Histogram
* Mean line
* Sine graph
* Cosine graph
* Grid and legend
* Chart customization

---

# 💻 Complete Program

```python
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. NUMPY BASE PRACTICE
# ==========================================

# Creating arrays
a = np.array([1, 2, 3, 4, 5])
b = np.zeros((3, 3))
c = np.ones((2, 4))
d = np.arange(0, 10, 2)
e = np.linspace(0, 1, 5)

# Array properties
print("Array A properties:", a.shape, a.dtype, a.ndim)

# Reshaping
matrix = np.arange(12).reshape(3, 4)
print("\nReshaped Matrix:\n", matrix)

# Indexing & Slicing
arr = np.array([10, 20, 30, 40, 50])

print("\nFirst & Last:", arr[0], arr[-1])
print("Slice [1:4]:", arr[1:4])

# 2D indexing
m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nElement at (1,2):", m[1, 2])
print("Second column:", m[:, 1])
print("First two rows:\n", m[0:2, :])

# Boolean masking & Fancy indexing
scores = np.array([85, 42, 91, 67, 73])
passed = scores[scores >= 70]

print("\nPassed Scores:", passed)
print("Fancy Indexing:", arr[[0, 3, 4]])


# ==========================================
# 2. PANDAS BASE PRACTICE
# ==========================================

# Create DataFrame
df_demo = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Dept": ["IT", "HR", "IT", "HR"],
    "Salary": [70000, 65000, 80000, 72000]
})

# Filtering
it_team = df_demo[df_demo["Dept"] == "IT"]
high_pay = df_demo[df_demo["Salary"] > 70000]

# Sorting
sorted_df = df_demo.sort_values(
    "Salary",
    ascending=False
)

# New Column
df_demo["Bonus"] = df_demo["Salary"] * 0.1

# Aggregation
dept_avg = df_demo.groupby("Dept")["Salary"].mean()

print("\n--- Department Average Salary ---")
print(dept_avg)

# Clean DataFrame columns
df_demo = (
    df_demo
    .drop(columns=["Bonus"])
    .rename(columns={"Dept": "Department"})
)


# ==========================================
# 3. DATA CLEANING & ANALYSIS WORKFLOW
# ==========================================

file_path = "retail_store_sales.csv"

if os.path.exists(file_path):

    # Load dataset
    df = pd.read_csv(file_path)

    # Standardize column headers
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("\n--- Dataset Summary ---")
    df.info()

    print("\n--- Statistical Overview ---")
    print(df.describe())

    # Missing values
    missing_pct = df.isnull().mean() * 100

    print("\n--- Missing Value Percentage ---")
    print(missing_pct)

    # Duplicate rows
    duplicates = df[df.duplicated()]

    print(f"\nDuplicate Rows Found: {len(duplicates)}")

    # Remove unnecessary column
    df_cleaned = df.drop(
        columns=["transaction_id"],
        errors="ignore"
    )

    # Fill missing item conditionally
    condition = (
        (df_cleaned["item"].isna()) &
        (df_cleaned["price_per_unit"] == 33.5) &
        (df_cleaned["category"] == "Furniture")
    )

    df_cleaned.loc[
        condition,
        "item"
    ] = "Item_20_FUR"

    # View updated records
    target_items = df_cleaned[
        (df_cleaned["price_per_unit"] == 33.5) &
        (df_cleaned["category"] == "Furniture")
    ]

    print("\n--- Updated Targeted Records ---")
    print(target_items)

else:
    print(
        f"\nNote: '{file_path}' not found. "
        "Skipping file read steps."
    )


# ==========================================
# 4. VISUALIZATIONS
# ==========================================

# Chart 1: Exam Score Distribution
plt.figure(figsize=(8, 4))

data = np.random.normal(70, 10, 1000)

plt.hist(
    data,
    bins=17,
    edgecolor="#4A5568",
    alpha=0.7,
    color="#4FD1C5"
)

plt.axvline(
    data.mean(),
    color="#E53E3E",
    linestyle="--",
    linewidth=2,
    label=f"Mean: {data.mean():.2f}"
)

plt.title(
    "Exam Score Distribution",
    fontsize=12,
    pad=10
)

plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.show()


# Chart 2: Trigonometric Functions
plt.figure(figsize=(8, 4))

x = np.linspace(0, 10, 100)

plt.plot(
    x,
    np.sin(x),
    label="sin(x)",
    linewidth=2
)

plt.plot(
    x,
    np.cos(x),
    label="cos(x)",
    linewidth=2,
    linestyle="--"
)

plt.title(
    "Trigonometric Functions",
    fontsize=12,
    pad=10
)

plt.xlabel("x")
plt.ylabel("y")

plt.grid(
    True,
    linestyle=":",
    alpha=0.6
)

plt.legend()

plt.tight_layout()
plt.show()
```

---

# 📂 Project Structure

```text
python-data-analysis/
│
├── 📄 README.md
├── 🐍 data_analysis.py
├── 📊 retail_store_sales.csv
└── 📦 requirements.txt
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-data-analysis.git
```

Move into the project folder:

```bash
cd python-data-analysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Create a `requirements.txt` file:

```text
numpy
pandas
matplotlib
seaborn
```

---

# ▶️ Run the Project

```bash
python data_analysis.py
```

---

# 📊 Data Analysis Workflow

```text
        📂 DATASET
            │
            ▼
      ┌──────────────┐
      │  Load Data   │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │   Inspect    │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │ Clean Data   │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │   Analyze    │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │  Visualize   │
      └──────┬───────┘
             │
             ▼
          💡 INSIGHTS
```

---

# 🧠 Concepts Covered

```text
NUMPY
│
├── Array Creation
├── Array Properties
├── Reshaping
├── Indexing
├── Slicing
├── Boolean Masking
└── Fancy Indexing


PANDAS
│
├── DataFrames
├── Filtering
├── Sorting
├── New Columns
├── GroupBy
└── Aggregation


DATA CLEANING
│
├── CSV Loading
├── Column Standardization
├── Missing Values
├── Duplicate Detection
├── Column Removal
└── Conditional Cleaning


VISUALIZATION
│
├── Histogram
├── Mean Line
├── Line Plot
├── Sine Function
└── Cosine Function
```

---

# 🎯 Learning Objectives

Through this project, I practiced how to:

* Work with NumPy arrays
* Manipulate data using Pandas
* Load CSV datasets
* Inspect dataset structure
* Identify missing values
* Detect duplicate records
* Clean unnecessary data
* Perform conditional data updates
* Create statistical visualizations
* Visualize mathematical functions
* Build a basic data analysis workflow

---

# 🚀 Future Plans

* [ ] Advanced Pandas
* [ ] Missing-value handling techniques
* [ ] Data type conversion
* [ ] Merge and Join
* [ ] Pivot Tables
* [ ] Exploratory Data Analysis
* [ ] Advanced Seaborn
* [ ] Statistical Analysis
* [ ] Data Analysis Dashboards
* [ ] Machine Learning Projects

---

# ⭐ Repository Goal

> **Learn → Practice → Analyze → Visualize → Build Projects**

---

<p align="center">

### 💻 Learn • Practice • Analyze • Build

</p>

<p align="center">

**🐍 Python → 🔢 NumPy → 🐼 Pandas → 🧹 Data Cleaning → 📊 Visualization → 🔍 Data Analysis → 🤖 Machine Learning**

</p>

---

# 👨‍💻 Author

**Farzan Alware**

Python Learner • Data Analysis Enthusiast

⭐ If you find this repository useful, consider giving it a star!
