patient = ("John Kamau", 45, "120/80", 72)  
print("Patient Record:", patient)
print("\nPatient Age:", patient[1])
print("Patient Heart Rate:", patient[3])
print("\nExplanation:")
print("Tuples are immutable, meaning the data cannot be accidentally changed. "
      "This is important in healthcare to preserve the integrity and accuracy of patient records.")
patient_list = list(patient)  
patient_list[3] = 80  
patient = tuple(patient_list)  
print("\nUpdated Patient Record:", patient)
patients = (
    ("John Kamau", 45, "120/80", 80),
    ("Alice Smith", 30, "110/70", 75),
    ("Michael Lee", 55, "130/85", 78),
    ("Sarah Kim", 40, "115/75", 72),
    ("David Brown", 60, "140/90", 70)
)
names = [p[0] for p in patients]  
print("\nList of Patient Names:", names)
