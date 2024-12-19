import pandas as pd

# Load the CSV file
df = pd.read_csv('engineered_data.csv')

# Remove the HeartDisease column
df_cleaned = df.drop(columns=['HeartDisease'])

# Extract the first 200 rows
df_first_200 = df_cleaned.head(200)

# Save the processed data to a new CSV file
df_first_200.to_csv('heart_data_batch_1.csv', index=False)

print("Successfully processed the data and saved the first 200 rows without the 'HeartDisease' column.")
