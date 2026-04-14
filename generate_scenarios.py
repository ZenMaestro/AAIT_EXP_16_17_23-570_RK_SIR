import pandas as pd
import numpy as np
import os

np.random.seed(99)
n = 500

first_names = ['Aarav', 'Neha', 'John', 'Jane', 'Michael', 'Emily', 'Rohan', 'Priya', 'David', 'Sarah', 'Sai', 'Karthik', 'Lakshmi', 'Arjun', 'Sita', 'Rahul', 'Ananya']
last_names = ['Smith', 'Doe', 'Kumar', 'Patel', 'Sharma', 'Reddy', 'Singh', 'Gupta', 'Johnson', 'Williams', 'Brown', 'Rao', 'Iyer']

def generate_dataset(filename, study_range, att_range, sleep_range):
    names = [np.random.choice(first_names) + ' ' + np.random.choice(last_names) for _ in range(n)]
    study_hours = np.random.uniform(study_range[0], study_range[1], n)
    attendance = np.random.uniform(att_range[0], att_range[1], n)
    sleep = np.random.uniform(sleep_range[0], sleep_range[1], n)
    
    marks_raw = (study_hours * 5.5) + (attendance * 0.35) + (sleep * 1.5) + np.random.normal(0, 5, n)
    marks = np.clip(marks_raw, 0, 100)
    
    df = pd.DataFrame({
        'student_name': names,
        'study_hours': np.round(study_hours, 1),
        'attendance': np.round(attendance, 1),
        'sleep': np.round(sleep, 1),
        'marks': np.round(marks, 1)
    })
    
    df.to_csv(filename, index=False)
    print(f" [OK] Scenario dataset created: {filename} ({n} rows)")

os.makedirs('data', exist_ok=True)

# Scenario 1: The Overachievers (High study, high attendance, healthy sleep)
generate_dataset('data/data_scenario_overachievers.csv', [7, 10], [80, 100], [6, 9])

# Scenario 2: The Struggling Group (Low study, low attendance, poor sleep)
generate_dataset('data/data_scenario_strugglers.csv', [0, 4], [40, 65], [4, 6])

# Scenario 3: The Burnout Students (Very high study, very low sleep)
generate_dataset('data/data_scenario_burnout.csv', [8, 12], [60, 100], [2, 4.5])

print("\nAwesome! All 3 scenario datasets generated successfully!")
