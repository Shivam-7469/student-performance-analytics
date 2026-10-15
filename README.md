# STUDENT PERFORMANCE ANALYTICS SYSTEM

**Student Name:** SHIVAM  
**Course:** EWB Courses – Python with AI

---

## 1. Project Objective

The primary objective of the **Student Performance Analytics System** is to develop a Python-based application that processes student academic records and generates meaningful performance insights. The system automates marks calculation, grade assignment, pass/fail identification, and statistical analysis to evaluate individual and overall class performance efficiently.

## 2. Technologies Used

- **Python:** Core programming language used to implement the system's logic and functionality.
- **Pandas:** Used for loading, organizing, manipulating, and analyzing student data.
- **NumPy:** Used for numerical computations and statistical analysis.

## 3. Dataset Description

The project uses a CSV file named `students.csv`, containing academic records for **15 students**. The dataset includes the following fields:

- Student ID
- Student Name
- Department
- Marks in three subjects
- Attendance percentage

This structured dataset serves as the primary input for calculating academic performance metrics and generating analytical results.

## 4. System Implementation

### 4.1 Data Loading

The system uses the Pandas library to read the `students.csv` file and store the records in a DataFrame. This allows the student data to be accessed, processed, and analyzed efficiently.

### 4.2 Data Processing and Calculations

Custom functions are implemented in `functions.py` to perform essential calculations using Pandas and NumPy. These functions calculate the total marks and average marks for each student, reducing manual effort and improving consistency.

### 4.3 Grading and Result Evaluation

A condition-based grading system evaluates students according to their academic performance. The system assigns grades and identifies each student's result status as **Pass or Fail** based on the implemented criteria.

### 4.4 Statistical and Performance Analysis

The system performs multiple analytical operations to evaluate student and class performance, including:

- Calculation of the overall class average.
- Identification of the highest and lowest student performance.
- Subject-wise performance comparison.
- Identification of top-performing students.

These analyses provide a clearer understanding of academic strengths and areas that may require improvement.

## 5. Key Features

- **Automated Marks Calculation:** Calculates total and average marks for individual students.
- **Dynamic Grading System:** Assigns grades based on predefined conditions.
- **Pass/Fail Identification:** Determines student result status automatically.
- **Top Performer Identification:** Highlights students with the strongest academic performance.
- **Subject-Wise Analysis:** Evaluates performance across different subjects.
- **Statistical Insights:** Generates class-level performance summaries using Pandas and NumPy.
- **Structured Data Processing:** Organizes student records for efficient analysis and reporting.

## 6. Results and Final Outcome

The Student Performance Analytics System has been implemented as a Python-based application that processes student records and displays structured statistical results in the terminal.

By combining Python, Pandas, and NumPy, the project demonstrates how programming and data analysis techniques can be applied to academic performance evaluation. It reduces repetitive calculations, improves the organization of student records, and helps identify overall class trends and individual performance levels.

## 7. Conclusion

The project provides practical experience in Python programming, data manipulation, numerical computation, and conditional logic. It demonstrates the application of fundamental data analytics techniques to a real-world academic scenario.

The system can be extended in the future with graphical visualizations, attendance-based insights, automated report generation, and a graphical user interface to make the analysis more interactive and accessible.

---

**Project Title:** Student Performance Analytics System  
**Developed By:** SHIVAM  
**Course:** EWB Courses – Python with AI
