# Image Processing Technology (IPT) — Laboratory Assignments

**Institution**: The University of Azad Jammu and Kashmir (UAJK)  
**Department**: Department of Software Engineering (Computer Engineering Technology — CET Program)  
**Course**: Image Processing Technology (IPT)  
**Session**: Fall 2024 / 4th–5th Semester  

---

### Student & Submission Details
- **Student Name**: Qousain Haider
- **Roll Number**: `2024-CET-13`
- **Section / Group**: Group B
- **Submitted To**: **Madam Sidra**

---

## Laboratory Index & Course Modules

| Lab # | Topic / Title | Description & Covered Tasks | Deliverables |
| :---: | :--- | :--- | :---: |
| **Lab 01** | **Digital Image Fundamentals & Physical Sensing Models** | • 2D Continuous-to-discrete spatial sampling and amplitude quantization.<br>• Physics of image formation: illumination-reflectance model $f(x,y) = i(x,y) \cdot r(x,y)$.<br>• Raster vs. Vector image format classification across 5 domains.<br>• Python & OpenCV image matrix loading, dimensions checking, and bit-depth quantization. | [`Lab01/`](./Lab01/) |
| **Lab 02** | **Introduction to Python Programming** | • Python interactive input, integer conversion, and arithmetic operations.<br>• Program 1: Student biographical profile and approximate age calculation for 2026.<br>• Program 2: Uncompressed grayscale image file size estimation in Bytes, KB, and MB.<br>• Lab Tasks: Arithmetic calculator, total pixel calculator, memory size estimator, and academic marks average. | [`Lab02/`](./Lab02/) |
| **Lab 03** | **Intro to Python, NumPy & OpenCV** | • Multidimensional array handling and slicing in NumPy.<br>• Task 1: Image loading, shape inspection `(H, W, C)`, and memory diagnostics.<br>• Task 2: RGB spectral channel decomposition (`cv2.split`).<br>• Task 3: Grayscale conversion with photometric weighting ($Y = 0.299R + 0.587G + 0.114B$).<br>• Task 4: Spatial thresholding (Global fixed vs Adaptive Gaussian). | [`Lab03/`](./Lab03/) |
| **Lab 04** | **Image Thresholding & Connected Component Labeling** | • Manual $3 \times 3$ matrix problem from demonstration notes ($T = 120$).<br>• Topological connectivity analysis: 4-connectivity (3 objects) vs 8-connectivity (1 object).<br>• Task 1: Global binary thresholding (`cv2.threshold`).<br>• Task 2: Otsu's optimal between-class variance thresholding (`cv2.THRESH_OTSU`).<br>• Task 3: Local adaptive Gaussian thresholding (`cv2.adaptiveThreshold`).<br>• Task 4: Connected component labeling and counting (`cv2.connectedComponentsWithStats`).<br>• Task 5: Morphological opening and closing noise removal. | [`Lab04/`](./Lab04/) |
| **Lab 05** | **Histogram Processing of Images** | • Task 1: Histogram computation (`cv2.calcHist` vs `np.histogram`) and tonal balance analysis.<br>• Task 2: Linear intensity transformations ($g = \alpha f + \beta$) showing contrast spread ($\alpha$) and brightness shift ($\beta$).<br>• Task 3: Custom percentile contrast stretching `stretch(img, low_pct, high_pct)` testing `(2, 98)` vs `(0, 100)`.<br>• Task 4: From-scratch manual CDF histogram equalization verified against `cv2.equalizeHist()` ($\Delta = 0$).<br>• Task 5: Global equalization vs CLAHE parameter sweeps across clip limits (1, 2, 4).<br>• Task 6: Color image equalization: why independent RGB equalization ruins color vs YCrCb luminance-only equalization.<br>• Task 7: Histogram specification / matching (`skimage.exposure.match_histograms`). | [`Lab05/`](./Lab05/) |

---

## Repository Structure

```
IPT_Lab_Tasks/
├── README.md                                          # Master repository documentation
├── Qousain_Haider_2024-CET-13_IPT_Labs_1_to_5.zip     # Complete 5-Lab assignment package
├── Lab01/
│   ├── README.md
│   ├── Qousain_Haider_2024-CET-13_Lab01_IPT.docx
│   └── lab01_tasks.py
├── Lab02/
│   ├── README.md
│   ├── Qousain_Haider_2024-CET-13_Lab02_IPT.docx
│   └── lab02_tasks.py
├── Lab03/
│   ├── README.md
│   ├── Qousain_Haider_2024-CET-13_Lab03_IPT.docx
│   └── lab03_tasks.py
├── Lab04/
│   ├── README.md
│   ├── Qousain_Haider_2024-CET-13_Lab04_IPT.docx
│   └── lab04_tasks.py
└── Lab05/
    ├── README.md
    ├── Qousain_Haider_2024-CET-13_Lab05_IPT.docx
    └── lab05_tasks.py
```

---

## How to Run the Python Scripts

All Python scripts are written to be clean, self-contained, and beginner-friendly.

```bash
# Clone the repository
git clone https://github.com/syedqousainhaidershah/IPT_Lab_Tasks.git
cd IPT_Lab_Tasks

# Install dependencies
pip install opencv-python numpy matplotlib scikit-image

# Run any lab task
python Lab01/lab01_tasks.py
python Lab02/lab02_tasks.py
python Lab03/lab03_tasks.py
python Lab04/lab04_tasks.py
python Lab05/lab05_tasks.py
```
