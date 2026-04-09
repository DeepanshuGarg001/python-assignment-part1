# Assignment — Part 1: Python Basics & Control Flow

## Theme: Student Grade Tracker

A command-line **Student Grade Tracker** that manages student data, computes results, and provides a summary report — all using core Python concepts.

**Total Marks:** 25

---

## Tasks Overview

| Task | Description | Marks |
|------|-------------|-------|
| 1 | Data Parsing & Profile Cleaning | 5 |
| 2 | Marks Analysis (Loops & Conditionals) | 8 |
| 3 | Class Performance Summary | 7 |
| 4 | String Manipulation Utility | 5 |

---

## How to Run

```bash
python3 part1_grade_tracker.py
```

> **Note:** Task 2 includes an interactive while loop that asks for subject names and marks. Type `done` as the subject name to stop adding entries.

---

## Task Details

### Task 1 — Data Parsing & Profile Cleaning
- Cleans raw student data (strips whitespace, converts names to Title Case)
- Converts roll numbers from string to integer
- Splits comma-separated marks string into a list of integers
- Validates that names contain only alphabetic characters
- Prints formatted profile cards for each student
- Prints name in ALL CAPS and lowercase for roll number 103

### Task 2 — Marks Analysis Using Loops & Conditionals
- Prints each subject with marks and a grade label (A+, A, B, C, F)
- Calculates total marks, average, highest and lowest scoring subjects
- Includes a while loop to add new subjects with input validation

### Task 3 — Class Performance Summary
- Computes average marks and assigns Pass/Fail status for each student
- Prints a formatted class report table
- Displays number of passed/failed students, class topper, and class average

### Task 4 — String Manipulation Utility
- Strips leading/trailing whitespace from an essay
- Converts to Title Case
- Counts occurrences of "python" (case-insensitive)
- Replaces "python" with "Python 🐍"
- Splits essay into sentences and prints them numbered

---

## File Structure

```
python-assignment-part1/
├── part1_grade_tracker.py   # Main Python script with all 4 tasks
└── README.md                # This file
```
