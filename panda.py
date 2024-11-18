import sqlite3
import pandas as pd

# Path to your .db file
db_file = 'feedback.db'  # Your database file

# Connect to the database
conn = sqlite3.connect(db_file)

# List all tables (optional, to identify tables)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", [table[0] for table in tables])

# Read data from the 'feedback' table
table_name = 'feedback'  # Replace with your table name if different
query = f"SELECT * FROM {table_name};"

# Load data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Export the DataFrame to an Excel file
output_file = 'feedback_output.xlsx'  # Update the path and filename as needed
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"Data has been exported to {output_file}")

# Close the database connection
conn.close()
