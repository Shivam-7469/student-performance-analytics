import pandas as pd
import numpy as np
import functions as fn

# Reading the CSV file containing student data
try:
    df = pd.read_csv('students.csv')
    print("--- Student Data Successfully Loaded ---\n")
except FileNotFoundError:
    print("Error: students.csv not found.")
    exit()

# data processing using functions from functions.py
df = fn.calculate_total_and_average(df)
df = fn.apply_grades_and_status(df)

# Department-wise Performance Analysis
print("\n--- Department-wise Performance ---")
#groupby() funtion use for department-wise average calculation
# Department ke hisaab se average nikalna
dept_analysis = df.groupby('Department')['Average'].mean()

for dept, avg in dept_analysis.items():
    print(f"{dept}: {avg:.2f}%")
best_dept = dept_analysis.idxmax()
best_avg = dept_analysis.max()
print(f"\n🏆 Best Performing Department: {best_dept} ({best_avg:.2f}%)")
print("\n")




# data analysis and insights
print("=== FINAL PERFORMANCE ANALYSIS ===\n")
print("--- Processed Student Data (First 5 Records) ---")
print(df[['Student_ID', 'Name', 'Total_Marks', 'Average', 'Grade', 'Status']].head()) #beacause .head() is used to display first 5 records
print("\n" , "-"*60, "\n")



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
print(f"TOP PERFORMER(STUDENT): {', '.join(top_students)}")

# Subject-wise Performance
print("\n--------- Subject-wise Averages ---------")
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
print("\n")
print("\n")



# specific student data retrieval
print("--- Search Specific Student ---")
search_id = input("ENTER STUDENT ID TO SEARCH (E.G., 101): ").strip()

if search_id.strip():
    try:
        search_id = int(search_id)
    
        student_info = df[df['Student_ID'] == search_id]
        
        if not student_info.empty:
            print("\n✅ STUDENT DETAILS FOUND:")
            print(student_info[['Student_ID', 'Name', 'Department', 'Total_Marks', 'Average', 'Grade', 'Status']].to_string(index=False))
        else:
            print("\n ❌ ID NOT FOUND")
    except ValueError:
        print("\n ❌ PLEASE ENTER A VALID STUDENT ID (NUMERIC VALUE).")
print("\n" , "*"*80,)
