import tkinter as tk
from tkinter import messagebox

# Grade points mapping
grade_points = {
    'A': 4.0,
    'B+': 3.5,
    'B': 3.0,
    'C+': 2.5,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}

def calculate_cgpa():
    try:
        total_credits = 0
        weighted_grade_points = 0
        num_courses = int(course_count_entry.get())
        
        for i in range(num_courses):
            course_name = entries[i][0].get()
            credits = int(entries[i][1].get())
            grade = entries[i][2].get().upper()
            
            if grade not in grade_points:
                raise ValueError(f"Invalid grade '{grade}' for course '{course_name}'")

            grade_point = grade_points[grade]
            total_credits += credits
            weighted_grade_points += credits * grade_point
        
        cgpa = weighted_grade_points / total_credits if total_credits != 0 else 0
        cgpa_label.config(text=f"Your CGPA is: {cgpa:.2f}")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def generate_course_inputs():
    for widget in frame_courses.winfo_children():
        widget.destroy()

    try:
        num_courses = int(course_count_entry.get())
        global entries
        entries = []

        for i in range(num_courses):
            course_name_label = tk.Label(frame_courses, text=f"Course {i + 1} Name:")
            course_name_label.grid(row=i, column=0, padx=5, pady=5)
            course_name_entry = tk.Entry(frame_courses)
            course_name_entry.grid(row=i, column=1, padx=5, pady=5)

            credit_label = tk.Label(frame_courses, text="Credits:")
            credit_label.grid(row=i, column=2, padx=5, pady=5)
            credit_entry = tk.Entry(frame_courses)
            credit_entry.grid(row=i, column=3, padx=5, pady=5)

            grade_label = tk.Label(frame_courses, text="Grade (A, B+, B, C+, C, D, F):")
            grade_label.grid(row=i, column=4, padx=5, pady=5)
            grade_entry = tk.Entry(frame_courses)
            grade_entry.grid(row=i, column=5, padx=5, pady=5)

            entries.append([course_name_entry, credit_entry, grade_entry])

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of courses.")

# Set up the main window
root = tk.Tk()
root.title("CGPA Calculator")

# Number of courses input
tk.Label(root, text="Enter number of courses:").pack(pady=10)
course_count_entry = tk.Entry(root)
course_count_entry.pack(pady=10)

# Button to generate course inputs
generate_button = tk.Button(root, text="Generate Course Inputs", command=generate_course_inputs)
generate_button.pack(pady=10)

# Frame to hold course inputs
frame_courses = tk.Frame(root)
frame_courses.pack(pady=10)

# Button to calculate CGPA
calculate_button = tk.Button(root, text="Calculate CGPA", command=calculate_cgpa)
calculate_button.pack(pady=10)

# Label to display the CGPA result
cgpa_label = tk.Label(root, text="Your CGPA is: ", font=("Arial", 14))
cgpa_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
