"""
Course: Image Processing Technology (IPT) - Lab 02
Student: Qousain Haider | Roll No: 2024-CET-13
Submitted To: Madam Sidra
Topic: Introduction to Python Programming
"""

# Program 1: Student Profile and Age Calculation
name = "Qousain Haider"
roll_no = "2024-CET-13"
semester = 4
birth_year = 2004
age_2026 = 2026 - birth_year

print("--- Student Information ---")
print("Name            :", name)
print("Roll Number     :", roll_no)
print("Semester        :", semester)
print("Submitted To    : Madam Sidra")
print("Approx. Age 2026:", age_2026)

# Program 2: Image File Size Estimation
width = 1920
height = 1080
total_pixels = width * height
size_bytes = total_pixels * 1 # 1 byte per pixel for 8-bit grayscale
size_kb = size_bytes / 1024.0

print("
--- Image Memory Estimation ---")
print("Resolution :", width, "x", height)
print("Pixels     :", total_pixels)
print("File Size  :", size_bytes, "bytes (", round(size_kb, 2), "KB )")

# Lab Tasks 1 - 4
print("
--- Lab Tasks ---")
# Task 1: Arithmetic
a, b = 25.0, 5.0
print("Arithmetic Operations: Sum=", a+b, "Diff=", a-b, "Prod=", a*b, "Div=", a/b)

# Task 2 & 3: Size for 1024x768
w2, h2 = 1024, 768
print("Image 1024x768 Size:", (w2 * h2) / 1024.0, "KB")

# Task 4: Marks
marks = [88.0, 85.0, 92.0]
print("Marks Total:", sum(marks), "| Average:", round(sum(marks)/len(marks), 2), "%")
