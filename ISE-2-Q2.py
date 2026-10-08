import pandas as pd

df = pd.read_csv("employees.csv")

salary = float(input("Enter minimum salary: "))
experience = int(input("Enter minimum experience: "))
department = input("Enter department: ")

filtered = df[
    (df["Salary"] >= salary) &
    (df["Experience"] >= experience) &
    (df["Department"].str.lower() == department.lower())
]

print(filtered)