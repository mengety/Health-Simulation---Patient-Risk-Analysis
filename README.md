# **Health Simulation: Patient Risk Analysis Using Python & NumPy**
<img width="850" height="553" alt="image" src="https://github.com/user-attachments/assets/6694ea24-dbb7-4239-aebd-1f98c9a73a11" />


## **Project Overview**

This project simulates a mini health analytics system.

You create a **synthetic dataset** of 10,000 patients with the following health features:

* **Age** (18–90 years)
* **BMI** (Body Mass Index, average 25, standard deviation 5)
* **Blood Pressure** (average 120, standard deviation 15)
* **Glucose Level** (70–150 mg/dL)

Then, you **classify patients** into **high-risk** and **low-risk** groups based on simple health rules:

* High-risk if BMI > 30 **and** Blood Pressure > 140
* Low-risk otherwise

Finally, you perform **basic statistical analysis**, **data normalization**, and **visualization** of the patient risk categories.

This project demonstrates how to:

* Generate random data using NumPy
* Work with arrays and vectorized operations
* Apply Boolean logic and conditional classification
* Calculate mean, standard deviation, and normalize data
* Use Python dictionaries to store structured data
* Visualize results with matplotlib

---

## **Key Concepts Used**

| Concept                   | How It Was Applied                            |
| ------------------------- | --------------------------------------------- |
| NumPy random generation   | Generate realistic patient data               |
| NumPy arrays              | Store and manipulate patient data efficiently |
| Boolean logic & masking   | Classify high-risk vs low-risk patients       |
| np.where                  | Convert True/False conditions into 1/0        |
| Mean & Standard Deviation | Basic statistics and normalization            |
| Python dictionaries       | Map patient IDs to computed health scores     |
| Matplotlib                | Visualize patient risk distribution           |

---

## **Step-by-Step Tasks**

1. **Random Data Generation**
   Generate 10,000 patient records using NumPy:

   * Ages (integers 18–90)
   * BMI (normal distribution, mean 25, std 5)
   * Blood Pressure (normal distribution, mean 120, std 15)
   * Glucose (uniform distribution, 70–150)

2. **Combine into a Patient Matrix**
   Combine the four features into a 2D array with shape `(10000, 4)`.

3. **Risk Classification**
   Classify each patient:

   * High-risk if BMI > 30 AND Blood Pressure > 140
   * Low-risk otherwise

4. **Statistics & Normalization**

   * Compute column-wise mean and standard deviation
   * Normalize each value: `(value - mean) / std`

5. **Python Dictionary Bridge**

   * Assign unique patient IDs: `P-0001`, `P-0002`, …
   * Compute a simple health score: `BMI + BP + Glucose`
   * Store in a dictionary: `{patient_id: health_score}`

6. **Visualization**

   * Bar chart showing number of high-risk vs low-risk patients

---

## **Sample Output**

* **Total High-Risk Patients:** 174
* **Percentage of High-Risk Patients:** 1.74%
* **Mean BMI:** 25.02
* **Top 5 Glucose Values:** [150.0, 149.8, 149.7, …]
* **Normalized Data (first 3 patients):**

```
[[ 0.34, -0.23, 0.12, -0.45],
 [-1.23, 0.56, -0.34, 0.12],
 [ 0.12, -1.01, 0.78, -0.56]]
```

* **Bar Chart:**
  Shows **Low Risk**  and **High Risk** in blue color with differnet Height.

---

## **How to Run the Project**

1. Install Python 3.x
2. Install required libraries:

   ```bash
   pip install numpy matplotlib
   ```
3. Run the Python script:

   ```bash
   python health_simulation.py
   ```
4. View results in the console and bar chart visualization.

---

## **What i have learned from this project**

* **Practiced NumPy basic to intermidate concepts** — random generation, arrays, vectorization
* **Learned simple health analytics** — risk scoring and classification
* **Understand statistical concepts** — mean, standard deviation, normalization
* **Bridge NumPy with Python dictionaries** — real-world data handling
* **Visualize data with matplotlib** — beginner-friendly data visualization



