"""
Course: Image Processing Technology (IPT) - Lab 01
Student: Qousain Haider | Roll No: 2024-CET-13
Submitted To: Madam Sidra
Topic: Digital Image Fundamentals & Matrix Loading
"""

import cv2
import numpy as np

# 1. Load sample image in grayscale
img = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
    # Use synthetic sample image
    img = np.random.randint(40, 220, (256, 256), dtype=np.uint8)

# 2. Check dimensions and pixel properties
height, width = img.shape
total_pixels = height * width

print("--- Image Properties ---")
print("Image Dimensions :", width, "x", height)
print("Total Pixels     :", total_pixels)
print("Data Type        :", img.dtype)
print("Min / Max Pixel  :", img.min(), "/", img.max())
print("Uncompressed Size:", total_pixels, "bytes (", total_pixels / 1024.0, "KB)")

# 3. Simulate downsampling
downsampled = cv2.resize(img, (width // 2, height // 2), interpolation=cv2.INTER_NEAREST)
print("Downsampled Size :", downsampled.shape)
