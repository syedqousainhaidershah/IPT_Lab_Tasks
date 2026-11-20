"""
Course: Image Processing Technology (IPT) - Lab 03
Student: Qousain Haider | Roll No: 2024-CET-13
Submitted To: Madam Sidra
Topic: Intro to Python, NumPy & OpenCV
"""

import cv2
import numpy as np

# Task 1: Load and display image
img = cv2.imread('sample.jpg')
if img is None:
    img = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)

h, w, c = img.shape
print(f"[Task 1] Image Dimensions: Height={h}, Width={w}, Channels={c}")
print(f"[Task 1] Data Type: {img.dtype}")

# Task 2: Display RGB components separately
B, G, R = cv2.split(img)
print(f"[Task 2] Channel Means: Blue={np.mean(B):.1f}, Green={np.mean(G):.1f}, Red={np.mean(R):.1f}")

# Task 3: Convert to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"[Task 3] Grayscale Shape: {gray.shape}, Mean Intensity: {np.mean(gray):.1f}")

# Task 4: Thresholding
ret, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
print(f"[Task 4] Applied Global Threshold: {ret}, White Pixels: {np.count_nonzero(thresh)}")
