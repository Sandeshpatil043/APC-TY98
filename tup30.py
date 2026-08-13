patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Sneha", 22, "O+"),
    (104, "Pooja", 28, "A+")
)

# Display all records
print("All Patient Records:")
for patient in patients:
    print(patient)

# Search patient by ID
pid = int(input("\nEnter Patient ID: "))

found = False

for patient in patients:
    if patient[0] == pid:
        print("Patient found:", patient)
        found = True

if not found:
    print("Patient not found")

# Count total patients
print("\nTotal patients:", len(patients))

# Display patients by blood group
blood = input("\nEnter blood group: ")

print("Patients with", blood, "blood group:")

for patient in patients:
    if patient[3] == blood:
        print(patient)