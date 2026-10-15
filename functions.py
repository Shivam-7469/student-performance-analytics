import pandas as pd
import numpy as np

def calculate_total_and_average(df):
    # Pandas ka use karke total marks calculate karna
    df['Total_Marks'] = df[['Maths', 'Physics', 'Chemistry']].sum(axis=1)
    
    # NumPy ka use karke average calculate karna
    df['Average'] = np.round(df['Total_Marks'] / 3, 2)
    return df

def assign_grade(average):
    # Conditions ka use karke grade assign karna
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 40:
        return 'D'
    else:
        return 'F'

def check_pass_fail(average):
    # Pass/fail condition
    return 'Pass' if average >= 40 else 'Fail'

def apply_grades_and_status(df):
    grades = []
    statuses = []
    
    # Loop ka istemal karke har student ka data process karna
    for index, row in df.iterrows():
        grades.append(assign_grade(row['Average']))
        statuses.append(check_pass_fail(row['Average']))
        
    df['Grade'] = grades
    df['Status'] = statuses
    return df
