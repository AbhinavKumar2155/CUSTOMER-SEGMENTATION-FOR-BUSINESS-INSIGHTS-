# Customer Segmentation for Business Insights

A hands-on business analytics project that segments insurance customers using **K-Means clustering** in Python and visualizes the findings through interactive **Power BI** dashboards. The goal is to turn raw customer data into actionable business insights — who the customers are, what they buy, and where the business opportunities lie.

## Author

**Abhinav Kumar** — sole author and contributor.

- GitHub: [@AbhinavKumar2155](https://github.com/AbhinavKumar2155)

## Project Overview

The project analyzes a customer-level insurance dataset (demographics, income, coverage, premium, products owned, geography, and communication preferences) to:

- Understand the distribution of coverage amounts and premiums across years, regions, and occupations
- Group customers into meaningful segments using unsupervised learning
- Profile each segment to support targeted marketing and cross-selling decisions

## Repository Contents

| File | Description |
|------|-------------|
| `pro.py` | End-to-end Python analysis: data cleaning, EDA, K-Means clustering, and PCA visualization |
| `STProject.pbix` | Main Power BI dashboard for customer segmentation insights |
| `ca1.pbix`, `ertr.pbix`, `SERF.pbix`, `try.pbix` | Additional Power BI dashboards / working drafts |
| `PostLinks.txt` | Links to the LinkedIn post and related GitHub repository |

## How It Works

1. **Data loading & cleaning** — reads the customer dataset (`STP.xlsx`), checks for missing values and duplicates, and parses dates.
2. **Exploratory analysis** — average coverage by year, region-wise coverage totals, occupation-wise premium trends, correlation heatmap, and pairplots by product ownership.
3. **Feature preparation** — label-encodes categorical features (Gender, Marital Status, Education Level, Occupation) and standardizes all features.
4. **Clustering** — applies **K-Means (k = 4)** on Age, Income, Coverage, Premium, and demographics to assign each customer to a segment.
5. **Dimensionality reduction** — projects the scaled data onto 2 principal components (PCA) to visualize the four customer segments in 2D.
6. **Segment profiling** — summarizes each cluster's average Age, Income, Coverage, and Premium to characterize the segments.

## Tech Stack

- **Python 3** — pandas, NumPy, scikit-learn, Matplotlib, Seaborn
- **Power BI** — interactive dashboards built from the same dataset
- **Jupyter-friendly workflow** — step-by-step exploratory analysis in `pro.py`

## Getting Started

### Prerequisites

- Python 3.8+
- Power BI Desktop (to open the `.pbix` dashboards)

### Install dependencies

```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
```

### Run the analysis

1. Place the dataset file `STP.xlsx` in the project root.
2. Run the Python script:

```bash
python pro.py
```

3. Open `STProject.pbix` in Power BI Desktop to explore the interactive dashboards.

## Key Insights

- The customer base splits into **four distinct segments** with different income, coverage, and premium profiles.
- Coverage amounts and preferred communication channels vary significantly across regions and occupations — useful for regional campaign planning.
- The PCA view shows clear separation between segments, confirming that the clustering captures real structure in the data.

## License

This project is the work of **Abhinav Kumar** and is shared for educational and portfolio purposes. Feel free to explore and learn from it — attribution is appreciated.

---

⭐ Made with dedication by **Abhinav Kumar**. If you find this project useful, consider giving it a star!
