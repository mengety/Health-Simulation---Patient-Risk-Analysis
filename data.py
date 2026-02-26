import numpy as np
import matplotlib.pyplot as plt

# ---------------------- Random Number Generator ----------------------
rng = np.random.default_rng(42)  # Reproducible randomness

# ---------------------- Generate Patient Features ----------------------
num_patients = 10000

ages = rng.integers(18, 91, size=num_patients)                # Age: 18–90
bmi = rng.normal(25, 5, size=num_patients)                   # BMI: mean=25, std=5
bp = rng.normal(120, 15, size=num_patients)                  # Blood Pressure: mean=120, std=15
glucose = rng.uniform(70, 151, size=num_patients)            # Glucose: 70–150 mg/dL

# ---------------------- Combine Features ----------------------
patient_matrix = np.column_stack([ages, bmi, bp, glucose])    # Shape: (10000, 4)

# ---------------------- Risk Classification ----------------------
is_high_risk = np.logical_and(bmi > 30, bp > 140)            # High risk if BMI>30 and BP>140
risk_classifier = np.where(is_high_risk, 1, 0)              # Convert boolean to 0/1

# ---------------------- Statistics ----------------------
mean_values = np.mean(patient_matrix, axis=0)               # Column-wise mean
std_values = np.std(patient_matrix, axis=0)                 # Column-wise standard deviation

# ---------------------- Normalization ----------------------
normalized_matrix = (patient_matrix - mean_values) / std_values  # Z-score normalization

# ---------------------- Patient IDs & Health Scores ----------------------
patient_ids = [f"P-{i:04d}" for i in range(1, num_patients+1)]  # Unique IDs: P-0001 ...
health_scores = bmi + bp + glucose                              # Simple health score
patient_dict = dict(zip(patient_ids, health_scores))            # Combine IDs and scores

# ---------------------- Summary Metrics ----------------------
total_patients = num_patients
num_high_risk = np.sum(risk_classifier)
num_low_risk = total_patients - num_high_risk
percentage_high_risk = (num_high_risk / total_patients) * 100
average_bmi = np.mean(bmi)
top_5_glucose = np.sort(glucose)[-5:]                          # Top 5 glucose values
first_3_normalized = normalized_matrix[:3]                     # First 3 normalized patient rows

# ---------------------- Visualization ----------------------
labels = ["Low Risk", "High Risk"]
values = [num_low_risk, num_high_risk]

plt.bar(labels, values)
plt.xlabel("Risk Category")
plt.ylabel("Number of Patients")
plt.title("Patient Risk Distribution")
plt.show()
