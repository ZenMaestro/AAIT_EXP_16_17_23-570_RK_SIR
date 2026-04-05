# AAIT (III–II) – EXP-16 & EXP-17 Capstone
## AI What-If Scenario Simulator

**Author:** ZenMaestro
**Domain:** Machine Learning / Predictive Modeling

### About The Project
This repository contains the complete "AI What-If Scenario Simulator" built for an academic laboratory experiment (EXP-16 and EXP-17). The goal of this project is to create an interactive "Digital Twin" for students—allowing them to predict their final marks based on three vital inputs: **Study Hours**, **Attendance**, and **Sleep**.

### Key Features
- **1,000-Row Custom Dataset:** Created using a programmatic generator script to mimic realistic student performance correlations.
- **Scikit-Learn Linear Regression:** The core machine learning model that maps continuous inputs to a continuous output (marks).
- **High Accuracy:** Evaluated using Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-Squared ($R^2$) Score metrics.
- **Interactive Runtime Simulation:** A dynamic `while` loop interface built specifically for academic presentation workflows, allowing live demonstrations without the need for complex web-hosting.

### Tech Stack
- **Python 3.x**
- **Pandas** (Data loading and matrix manipulation)
- **Scikit-Learn** (Model building, Test/Train splitting, Metrics)
- **Matplotlib** (Visualizing Actual vs. Predicted accuracy)
- **Jupyter Notebooks** (Interactive documented execution)

### File Structure
- `data/data.csv`: The 1,000-record dataset containing student histories.
- `generate_data.py`: The script used to mathematically generate the dataset.
- `AAIT_EXP_16_WhatIfSimulator_Student.ipynb`: The main laboratory submission notebook containing Markdown formatting and sequential evaluation steps.
- `AAIT_EXP_16_WhatIfSimulator_Interactive.ipynb`: The final runtime presentation loop for the live Capstone demo.

### How to Run
1. Make sure Python is installed.
2. Install requirements using `pip install pandas scikit-learn matplotlib numpy`.
3. Select any Jupyter IDE (VS Code, JupyterLab) or Google Colab.
4. Execute `AAIT_EXP_16_WhatIfSimulator_Interactive.ipynb` block by block.
5. In the final block, enter your name and study habits when prompted to receive a personalized mark prediction!
