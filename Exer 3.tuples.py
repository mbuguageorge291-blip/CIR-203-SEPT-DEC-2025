
patient = ("John Doe", 45, "120/80", 72)

print("Age:", patient[1])
print("Heart Rate:", patient[3])


patient_list = list(patient)
patient_list[3] = 75 
updated_patient = tuple(patient_list)
print("Updated Patient Record:", updated_patient)


patients = (
    ("Alice Smith", 30, "110/70", 68),
    ("Bob Johnson", 52, "130/85", 80),
    ("Carol White", 40, "125/78", 74),
    ("David Brown", 60, "140/90", 82),
    ("Eva Green", 35, "118/76", 70)
)

names = [patient[0] for patient in patients]
print("Patient Names:", names)
