# SpaceX Launch Records Analysis and Dashboard

This repository contains a comprehensive analysis of SpaceX's launch records, leveraging data science techniques to generate insights and build an interactive dashboard. The project is part of the **IBM Data Science Capstone** from Coursera and showcases the application of Python, SQL, and machine learning for business analysis and decision-making.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Data Sources](#data-sources)
3. [Key Insights](#key-insights)
4. [How to Run](#how-to-run)
5. [Appendix](#appendix)
6. [License](#license)

---

## **Overview**
SpaceX has revolutionized space exploration by reusing rockets, significantly reducing launch costs. The purpose of this project is to:
- Analyze SpaceX's historical launch data.
- Build predictive models to classify launch outcomes.
- Create an interactive dashboard to visualize key metrics and trends.

### **Goals**
- Understand launch site performance.
- Analyze payload and booster configurations' impact on launch success.
- Build machine learning models to predict rocket landing success.

---

## **Data Sources**
The dataset used in this project is sourced from the SpaceX API and includes:
- Launch dates and sites.
- Payload details (mass, type, orbit).
- Booster configurations and versions.
- Launch success and rocket landing outcomes.

---

---

## **Key Insights**
1. **Launch Success by Site:** 
   - Kennedy Space Center (KSC LC-39A) has the highest success rate.
2. **Payload and Launch Success:**
   - Payloads between 3,000–5,000 kg have a higher success rate.
3. **Booster Performance:**
   - The Falcon 9 B5 booster version shows the highest reliability.
4. **Machine Learning Results:**
   - Predictive models achieved a 92% accuracy in classifying successful rocket landings.
5. **Dashboard Features:**
   - An interactive dashboard visualizes launch trends, success rates, and payload impacts.

---

## **How to Run**

### **1. Prerequisites**
- Install Python 3.8+.
- Required Python libraries:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`
  - `dash`, `plotly`, `sklearn`

### **2. Clone the Repository**
```bash
git clone https://github.com/Zeyad-Medhat/Applied-Data-Science-Capstone.git
cd Applied-Data-Science-Capstone
```
## Appendix

- **Data Preprocessing:** See `notebooks/1-EDA-and-Preprocessing.ipynb`.
- **SQL Queries:** SQL queries for data exploration are included in `notebooks/2-SQL-Queries.ipynb`.
- **Machine Learning:** Detailed ML modeling is in `notebooks/3-ML-Modeling.ipynb`.
- **Dashboard Code:** The dashboard source code is in `dashboard/app.py`.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.



