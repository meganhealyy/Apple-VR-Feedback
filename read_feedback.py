import sqlite3

def read_database(db_name):
    """
    Connects to the SQLite database and reads its tables and data.

    Parameters:
    db_name (str): The name of the database file to connect to.
    """
    try:
        # Connect to the database
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        # Get all table names in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("Tables in the database:", [table[0] for table in tables])

        # Read data from each table
        for table in tables:
            table_name = table[0]
            print(f"\nData from table '{table_name}':")
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            
            # Print column names
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [column[1] for column in cursor.fetchall()]
            print(f"Columns: {columns}")
            
            # Print rows
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print("An error occurred:", e)
    finally:
        if connection:
            connection.close()

# Call the function
read_database("feedback.db")
