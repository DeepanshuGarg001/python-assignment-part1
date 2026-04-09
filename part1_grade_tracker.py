# ============================================================
# Assignment — Part 1: Python Basics & Control Flow
# Theme: Student Grade Tracker
# ============================================================


# ============================================================
# Task 1 — Data Parsing & Profile Cleaning (5 marks)
# ============================================================

# Raw student data with inconsistent spacing, casing, and marks as strings
raw_students = [
    {"name": "  ayesha SHARMA ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",      "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": " Priya Nair ",     "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",      "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",   "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# 1. Clean the data
cleaned_students = []  # list to hold cleaned student dictionaries

for student in raw_students:
    # strip whitespace and convert name to Title Case
    clean_name = student["name"].strip().title()
    # convert roll to integer
    clean_roll = int(student["roll"])
    # split marks_str on ", " and convert each to int
    clean_marks = [int(m.strip()) for m in student["marks_str"].split(",")]

    cleaned_students.append({
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks,
    })

# 2. Validate names — every word must be alphabetic
for s in cleaned_students:
    words = s["name"].split()
    # check that every word is purely alphabetic
    if all(word.isalpha() for word in words):
        validity = "✓ Valid name"
    else:
        validity = "✗ Invalid name"
    print(f"{s['name']} — {validity}")

print()

# 3. Print formatted profile card for each student
for s in cleaned_students:
    print("=" * 30)
    print(f"Student : {s['name']}")
    print(f"Roll No : {s['roll']}")
    print(f"Marks   : {s['marks']}")
    print("=" * 30)

print()

# 4. Print name in ALL CAPS and lowercase for roll number 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"ALL CAPS  : {s['name'].upper()}")
        print(f"lowercase : {s['name'].lower()}")
        break

print()


# ============================================================
# Task 2 — Marks Analysis Using Loops & Conditionals (8 marks)
# ============================================================

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

# 1. Print each subject with marks and grade label using a for loop
print(f"Marks analysis for {student_name}")
print("-" * 40)

for i in range(len(subjects)):
    m = marks[i]
    # determine grade based on marks range
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"{subjects[i]:<12} : {m}  ({grade})")

print()

# 2. Calculate and print summary statistics
total_marks = sum(marks)
average_marks = round(total_marks / len(marks), 2)

# highest scoring subject
max_index = marks.index(max(marks))
highest_subject = subjects[max_index]
highest_marks = marks[max_index]

# lowest scoring subject
min_index = marks.index(min(marks))
lowest_subject = subjects[min_index]
lowest_marks = marks[min_index]

print(f"Total marks          : {total_marks}")
print(f"Average marks        : {average_marks}")
print(f"Highest scoring      : {highest_subject} ({highest_marks})")
print(f"Lowest scoring       : {lowest_subject} ({lowest_marks})")

print()

# 3. While loop — marks-entry system to add new subjects
new_subjects = []  # track newly added subjects and marks

while True:
    subject_input = input("Enter subject name (or 'done' to stop): ")
    if subject_input.lower() == "done":
        break

    marks_input = input(f"Enter marks for {subject_input} (0–100): ")

    # validate the marks input
    try:
        marks_value = int(marks_input)
        if marks_value < 0 or marks_value > 100:
            print("⚠ Invalid marks! Must be between 0 and 100. Entry skipped.")
            continue
    except ValueError:
        print("⚠ Invalid input! Please enter a numeric value. Entry skipped.")
        continue

    # valid entry — add to lists
    subjects.append(subject_input)
    marks.append(marks_value)
    new_subjects.append((subject_input, marks_value))

# print summary after the loop
print(f"\nNew subjects added   : {len(new_subjects)}")
updated_average = round(sum(marks) / len(marks), 2)
print(f"Updated average      : {updated_average}")

print()


# ============================================================
# Task 3 — Class Performance Summary (7 marks)
# ============================================================

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

# 1. Compute average and result status for each student
results = []  # list of (name, average, status)

for name, student_marks in class_data:
    avg = round(sum(student_marks) / len(student_marks), 2)
    status = "Pass" if avg >= 60 else "Fail"
    results.append((name, avg, status))

# 2. Print formatted class report
print(f"{'Name':<18}| {'Average':>7} | Status")
print("-" * 40)

for name, avg, status in results:
    print(f"{name:<18}| {avg:>7.2f} | {status}")

print()

# 3. Summary statistics
passed = sum(1 for _, _, s in results if s == "Pass")
failed = sum(1 for _, _, s in results if s == "Fail")
print(f"Passed             : {passed}")
print(f"Failed             : {failed}")

# class topper
topper = max(results, key=lambda x: x[1])
print(f"Class topper       : {topper[0]} ({topper[1]})")

# class average
class_avg = round(sum(avg for _, avg, _ in results) / len(results), 2)
print(f"Class average      : {class_avg}")

print()


# ============================================================
# Task 4 — String Manipulation Utility (5 marks)
# ============================================================

essay = "   python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning. "

# 1. Strip leading and trailing whitespace
clean_essay = essay.strip()
print(f"1. Stripped essay:\n{clean_essay}")
print()

# 2. Convert to Title Case
clean_essay_title = clean_essay.title()
print(f"2. Title Case:\n{clean_essay_title}")
print()

# 3. Count occurrences of "python" (case-insensitive)
# Since clean_essay is already lowercase, .count("python") works directly
python_count = clean_essay.count("python")
print(f"3. 'python' appears {python_count} time(s)")
print()

# 4. Replace "python" with "Python 🐍"
# clean_essay is lowercase so .replace("python", "Python 🐍") catches all
replaced_essay = clean_essay.replace("python", "Python 🐍")
print(f"4. Replaced essay:\n{replaced_essay}")
print()

# 5. Split into sentences on ". " and print the list
sentences = clean_essay.split(". ")
print(f"5. Sentences list:\n{sentences}")
print()

# 6. Print each sentence numbered, adding "." if missing at end
print("6. Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"   {i}. {sentence}")
