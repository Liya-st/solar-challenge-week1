## Scripts

This folder contains modular Python scripts for data preprocessing and outlier detection.

### Structure:

* `clean_data.py`: Handles missing values, mistaken data and the like.
* `outlier_detection.py`: Identifies and flags outliers based on statistical methods like IQR analysis.

### Usage:

1. Import the required modules in your main script or notebook:

   ```python
   from scripts.clean_data import clean_data
   from scripts.remove_outliers import remove_outliers_iqr
   ```


