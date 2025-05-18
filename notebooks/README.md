# Jupyter Notebooks

This directory contains all country-specific notebooks for exploratory data analysis (EDA).

## Naming Convention

- Each notebook should be named as `<country>_eda.ipynb`.
- Use branches like `eda-<country>` for country-specific work.

The notebook files include Exploratory Data analysis code including: 
  * Summary statistics and missing value report
  * Outlier detection and handling
  * Time series analysis
  * Impact of cleaning operations
  * Correlation and relationship analysis
  * Wind and distribution analysis
  * Temperature analysis
  * Bubble chart visualization

### Usage:

1. Ensure your dataset is available at the specified `path` inside the notebook.
2. Run the notebook sequentially to generate:

   * Data cleaning and outlier removal
   * Visualization of key variables
   * Insights on temporal and spatial trends

### Requirements:

* Python 3.8+
* Required libraries:

  * pandas
  * numpy
  * matplotlib
  * seaborn
  * scipy
  * windrose
  * statsmodels



