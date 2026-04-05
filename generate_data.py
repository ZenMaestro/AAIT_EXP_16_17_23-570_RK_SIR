import pandas as pd
import numpy as np

# Set a seed so the dataset is exactly the same every time you run this
np.random.seed(42)
n = 1000

first_names = ['Aarav', 'Neha', 'John', 'Jane', 'Michael', 'Emily', 'Rohan', 'Priya', 'David', 'Sarah', 'Sai', 'Karthik', 'Lakshmi', 'Arjun', 'Sita', 'Rahul', 'Ananya']
last_names = ['Smith', 'Doe', 'Kumar', 'Patel', 'Sharma', 'Reddy', 'Singh', 'Gupta', 'Johnson', 'Williams', 'Brown', 'Rao', 'Iyer']

# Generate 1000 random names
names = [np.random.choice(first_names) + ' ' + np.random.choice(last_names) for _ in range(n)]

# Generate 1000 random-but-realistic values
study_hours = np.random.uniform(0, 10, n)
attendance = np.random.uniform(40, 100, n)
sleep = np.random.uniform(4, 10, n)

# Math trick: make the marks logically depend on the inputs (with a bit of random real-world noise)
marks_raw = (study_hours * 5.5) + (attendance * 0.35) + (sleep * 1.5) + np.random.normal(0, 5, n)

# Keep the marks strictly between 0 and 100
marks = np.clip(marks_raw, 0, 100)

df = pd.DataFrame({
    'student_name': names,
    'study_hours': np.round(study_hours, 1),
    'attendance': np.round(attendance, 1),
    'sleep': np.round(sleep, 1),
    'marks': np.round(marks, 1)
})

# Save to the CSV file
import os
os.makedirs('data', exist_ok=True)
df.to_csv('data/data.csv', index=False)
print("1000 row dataset with NAMES created successfully at data/data.csv!")
