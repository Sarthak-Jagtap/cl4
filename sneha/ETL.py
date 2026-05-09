# =====================================================
# ETL PROCESS AND DATA VISUALIZATION USING JUPYTER
# =====================================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# EXTRACT
# =====================================================

# Read data from Excel file
df = pd.read_excel("employee_data.xlsx")

# Employee_ID, Name, Department, Salary, Experience, Age, City

# Display original dataset
print("Original Dataset:\n")
print(df)

# =====================================================
# TRANSFORM
# =====================================================

# 1. Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# 2. Remove missing values
df = df.dropna()

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Rename column names
df.rename(columns={'Department':'Dept'}, inplace=True)

# 5. Change datatype
df['Salary'] = df['Salary'].astype(int)

# 6. Create new column
df['Bonus'] = df['Salary'] * 0.10

# 7. Filter IT department data
it_data = df[df['Dept'] == 'IT']

print("\nFiltered IT Department Data:\n")
print(it_data)

# 8. Sort data by salary
df = df.sort_values(by='Salary')

# 9. Grouping and aggregation
avg_salary = df.groupby('Dept')['Salary'].mean()

print("\nAverage Salary by Department:\n")
print(avg_salary)

# Display transformed dataset
print("\nTransformed Dataset:\n")
print(df)

# =====================================================
# LOAD
# =====================================================

# Save transformed data into CSV
df.to_csv("cleaned_employee_data.csv", index=False)

print("\nData Loaded Successfully into CSV File")

# =====================================================
# DATA VISUALIZATION
# =====================================================

# ---------------- BAR CHART ----------------

plt.figure(figsize=(6,4))

avg_salary.plot(kind='bar')

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

# ---------------- PIE CHART ----------------

plt.figure(figsize=(6,6))

df['Dept'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Department Distribution")

plt.ylabel("")

plt.show()

# ---------------- LINE CHART ----------------

plt.figure(figsize=(6,4))

plt.plot(
    df['Experience'],
    df['Salary'],
    marker='o'
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

# ---------------- HISTOGRAM ----------------

plt.figure(figsize=(6,4))

plt.hist(df['Salary'])

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

# ---------------- HEATMAP ----------------

plt.figure(figsize=(6,4))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()

# ---------------- SCATTER PLOT ----------------

plt.figure(figsize=(6,4))

plt.scatter(
    df['Experience'],
    df['Salary']
)

plt.title("Experience vs Salary Scatter Plot")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()