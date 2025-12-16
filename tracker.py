import pandas as pd

data = pd.read_csv("sample_training_data.csv")

completion_rate = (data['Status'] == 'Completed').mean() * 100
overdue = data[data['Status'] == 'Pending']

print("Training Completion Rate:", round(completion_rate, 2), "%")
print("Overdue Learners:")
print(overdue[['Employee Name', 'Manager']])
