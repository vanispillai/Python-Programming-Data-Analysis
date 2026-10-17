import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('employees_analysis.csv')
print(df.head())
print(df.info())
#cleaning
df.isnull().sum()
df=df.drop_duplicates()
#What is the average monthly income of all employees?
average_monthly_income = df['monthly_income'].mean()
print(average_monthly_income)
#What is the average monthly income for each department?
average_monthly_income_per_department = df.groupby('department')['monthly_income'].mean()
print(average_monthly_income_per_department)
#Which department has the highest average monthly income?
df.sort_values(by='monthly_income', ascending=False, inplace=True)
highest_avg_income_department = df.groupby('department')['monthly_income'].mean().idxmax()
print(highest_avg_income_department)
#How many employees are in each department?
employee_count_per_department = df.groupby('department').size()
print(employee_count_per_department)
#Which employees earn more than 10,000?
high_earning_employees = df[df['monthly_income'] > 10000][['department', 'employee_id', 'monthly_income']]
print(high_earning_employees)
#How many employees earn more than 10,000?
high_earning_employee_count = df[df['monthly_income'] > 10000].shape[0]
print(high_earning_employee_count)
#AGE ANALYSIS
#What is the minimum, maximum, and average age of employees?
min_age = df['age'].min()
max_age = df['age'].max()
avg_age = df['age'].mean()
print(f"Minimum Age: {min_age}, Maximum Age: {max_age}, Average Age: {avg_age}")
#What is the age distribution?
age_distribution = df['age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution of Employees')
plt.show()
#Create age groups
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 50, 100], labels=['Young', 'Middle-aged', 'Senior'])
print(df['age_group'].value_counts())
#Create a bar chart showing number of employees in each department.
employee_count_per_department = df.groupby('department').size()
employee_count_per_department.plot(kind='bar')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.title('Employee Count by Department')
plt.show()
#Create a bar chart showing average income by department.
average_income_per_department = df.groupby('department')['monthly_income'].mean()
average_income_per_department.plot(kind='bar')
plt.xlabel('Department')
plt.ylabel('Average Monthly Income')
plt.title('Average Monthly Income by Department')
plt.show()
#Visualize the age-group distribution.
df['age_group'].value_counts().plot(kind='bar')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.title('Age Group Distribution of Employees')
plt.show()
#Calculate total employees by department and job role.
total_employees_by_department_and_job_role = df.groupby(['department', 'job_role']).size()
print(total_employees_by_department_and_job_role)
#Calculate the number of employees who left in each department/job role.
attrition_count = df[df['attrition'] == 'Yes'].groupby(
    ['department', 'job_role']).size().reset_index(name='employees_left')
print(attrition_count)
#Calculate attrition rate
attrition_rate = df.groupby(['department', 'job_role']).agg(
    total_employees=('employee_id', 'count'),
    employees_left=('attrition', lambda x: (x == 'Yes').sum())).reset_index()
attrition_rate['attrition_rate'] = (
    attrition_rate['employees_left'] /
    attrition_rate['total_employees']) * 100
print(attrition_rate)
#Create an attrition visualization.
attrition_rate.plot(x='department', y='attrition_rate', kind='bar')
plt.xlabel('Department')
plt.ylabel('Attrition Rate (%)')
plt.title('Attrition Rate by Department')
plt.show()