subjects = int(input("Enter number of subjects: "))
cgpa = sum(float(input(f"Enter grade for subject {i+1}: ")) for i in range(subjects)) / subjects
print(f"Your CGPA is: {cgpa:.2f}")
