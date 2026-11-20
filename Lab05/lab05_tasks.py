"""
Course: Image Processing Technology (IPT) - Lab 05
Student: Qousain Haider | Roll No: 2024-CET-13
Submitted To: Madam Sidra
Topic: Histogram Processing of Images (Tasks 1 to 7)
"""

import cv2
import numpy as np
from skimage.exposure import match_histograms

# Sample test image
img = np.random.normal(55, 18, (200, 200)).clip(0, 255).astype(np.uint8)

# Task 1: Histogram computation
hist_cv = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_np, bins = np.histogram(img.flatten(), bins=256, range=[0, 256])
print("[Task 1] Mean Brightness:", round(np.mean(img), 2), "| Classification: Dark (Low-Key)")

# Task 2: Linear transformation g = alpha * f + beta
v1 = cv2.convertScaleAbs(img, alpha=1.0, beta=40)  # Brightness shift
v2 = cv2.convertScaleAbs(img, alpha=1.5, beta=0)   # Contrast spread
print(f"[Task 2] Original Mean: {np.mean(img):.1f} | Shifted Mean (+40): {np.mean(v1):.1f} | Spread Std: {np.std(v2):.1f}")

# Task 3: Percentile contrast stretching
def stretch(image, low_pct, high_pct):
    p_low = np.percentile(image, low_pct)
    p_high = np.percentile(image, high_pct)
    stretched = (image - p_low) * (255.0 / (p_high - p_low))
    return np.clip(stretched, 0, 255).astype(np.uint8)

res_2_98 = stretch(img, 2, 98)
print("[Task 3] Percentile Stretch (2, 98) Range:", res_2_98.min(), "to", res_2_98.max())

# Task 4: Manual CDF histogram equalization
hist, _ = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_mask = np.ma.masked_equal(cdf, 0)
lut = (cdf_mask - cdf_mask.min()) * 255 / (img.size - cdf_mask.min())
lut = np.ma.filled(lut, 0).astype('uint8')
manual_eq = lut[img]
cv_eq = cv2.equalizeHist(img)
max_diff = np.max(np.abs(manual_eq.astype(int) - cv_eq.astype(int)))
print("[Task 4] Max difference between Manual and OpenCV:", max_diff)

# Task 5: Global vs CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(img)
print("[Task 5] Global Eq Std:", round(np.std(cv_eq), 1), "| CLAHE (2.0) Std:", round(np.std(clahe), 1))

# Task 6: Color image equalization (YCrCb luminance vs RGB)
color_img = np.random.randint(40, 200, (100, 100, 3), dtype=np.uint8)
ycrcb = cv2.cvtColor(color_img, cv2.COLOR_BGR2YCrCb)
ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
color_good = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
print("[Task 6] Color equalization completed in YCrCb color space.")

# Task 7: Histogram matching
ref = np.random.normal(160, 30, (200, 200)).clip(0, 255).astype(np.uint8)
matched = match_histograms(img, ref)
print(f"[Task 7] Matched Output Mean: {np.mean(matched):.1f} (Source: {np.mean(img):.1f}, Ref: {np.mean(ref):.1f})")
