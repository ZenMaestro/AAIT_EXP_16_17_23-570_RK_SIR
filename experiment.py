import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import os

# --- Step 1: Define Problem ---
# Problem: Predict student performance (marks) to explore "what-if" scenarios.
# Input: study_hours, attendance, sleep
# Output: marks

print("--- Step 2: Preparing Dataset ---")
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, 'data', 'data.csv')
data = pd.read_csv(data_path)
print(f"Dataset loaded successfully with {len(data)} records.\n")
print(data.head())

# Features (X) and Target (y)
X = data[['study_hours', 'attendance', 'sleep']]
y = data['marks']

# Split into Training and Testing sets (Step 4 requirement)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"\nData split: {len(X_train)} training rows, {len(X_test)} testing rows.")

print("\n--- Step 3 & 4: Training the Model ---")
# Choosing Linear Regression for predicting a continuous number
model = LinearRegression()
model.fit(X_train, y_train)
print("Linear Regression model trained successfully.")

print("\n--- Step 5: Evaluating the Result ---")
# Test prediction on the test set
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R2 Score): {r2:.2f}")

print("\n--- Step 6: Align with UI and Workflow ---")
# Simulating a user interacting with the planned sliders
test_study_hours = 5
test_attendance = 80
test_sleep_hours = 6

sample_input = pd.DataFrame(
    [[test_study_hours, test_attendance, test_sleep_hours]], 
    columns=['study_hours', 'attendance', 'sleep']
)
predicted_mark = model.predict(sample_input)[0]

print("Simulating User Input from Figma Wireframe/UI:")
print(f" > Slider Inputs: {test_study_hours} Study Hours, {test_attendance}% Attendance, {test_sleep_hours} Sleep Hours")
print(f" > UI Display Output: Predicted Marks = {predicted_mark:.2f}")
