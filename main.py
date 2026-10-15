import pandas as pd
import numpy as np
import functions as fn

# Reading the CSV file containing student data
try:
    df = pd.read_csv('students.csv')
    print("--- Student Data Successfully Loaded ---\n")
except FileNotFoundError:
    print("Error: students.csv nahi mili. Kripya file check karein.")
    exit()

# data processing using functions from functions.py
df = fn.calculate_total_and_average(df)
df = fn.apply_grades_and_status(df)

print("--- Processed Student Data (First 5 Records) ---")
print(df[['Student_ID', 'Name', 'Total_Marks', 'Average', 'Grade', 'Status']].head())
print("\n" + "="*40 + "\n")

# data analysis and insights
print("=== FINAL PERFORMANCE ANALYSIS ===\n")

# overall class average
class_average = np.mean(df['Average'])
print(f"Overall Class Average: {class_average:.2f}%")

# Pass/Fail 
total_students = len(df)
passed = len(df[df['Status'] == 'Pass'])
failed = len(df[df['Status'] == 'Fail'])
print(f"Total Students: {total_students} | Passed: {passed} | Failed: {failed}")

# Highest and Lowest 
highest_avg = np.max(df['Average'])
lowest_avg = np.min(df['Average'])
print(f"Highest Average: {highest_avg}%")
print(f"Lowest Average: {lowest_avg}%")

# Top Performing Student(s)
top_students = df[df['Average'] == highest_avg]['Name'].tolist()
print(f"Top Performer(s): {', '.join(top_students)}")

# Subject-wise Performance
print("\n--- Subject-wise Averages ---")
maths_avg = np.mean(df['Maths'])
physics_avg = np.mean(df['Physics'])
chemistry_avg = np.mean(df['Chemistry'])

print(f"Maths: {maths_avg:.2f}")
print(f"Physics: {physics_avg:.2f}")
print(f"Chemistry: {chemistry_avg:.2f}")

# best performing subject
subjects = {'Maths': maths_avg, 'Physics': physics_avg, 'Chemistry': chemistry_avg}
best_subject = max(subjects, key=subjects.get)
print(f"Best Performing Subject: {best_subject}")
print("\n" + "="*40)