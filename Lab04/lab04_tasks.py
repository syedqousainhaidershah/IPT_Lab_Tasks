"""
Course: Image Processing Technology (IPT) - Lab 04
Student: Qousain Haider | Roll No: 2024-CET-13
Submitted To: Madam Sidra
Topic: Image Thresholding & Connected Component Labeling
"""

import cv2
import numpy as np

# Part 1: Matrix Problem from Demonstration Notes
# Input 3x3 matrix I with threshold T = 120
I = np.array([[150,  45,  12],
              [ 70, 180,  62],
              [ 30,  85, 210]], dtype=np.uint8)

# Binary thresholding
ret, G = cv2.threshold(I, 120, 255, cv2.THRESH_BINARY)
print("--- Part 1: Matrix Problem ---")
print("Input Matrix I:
", I)
print("Binary Matrix G (T=120):
", G)

# Connected components comparison
n4, lbls4, stats4, c4 = cv2.connectedComponentsWithStats(G, connectivity=4)
n8, lbls8, stats8, c8 = cv2.connectedComponentsWithStats(G, connectivity=8)

print("4-Connected Components (excluding background):", n4 - 1)
print("8-Connected Components (excluding background):", n8 - 1)
print("Observation: Diagonal 1s are isolated in 4-way (3 objects), but connected in 8-way (1 object).")

# Part 2: Practical Tasks
print("
--- Part 2: Practical Tasks ---")
# Otsu automatic thresholding
otsu_val, otsu_img = cv2.threshold(I, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("Otsu Auto Threshold:", otsu_val)

# Morphological noise removal
kernel = np.ones((3, 3), np.uint8)
clean = cv2.morphologyEx(G, cv2.MORPH_OPEN, kernel)
final = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel)
print("Morphological noise cleaning completed.")
