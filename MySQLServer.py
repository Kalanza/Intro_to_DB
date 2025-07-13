import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without specifying a database)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kalanza@2004"
    )
    mycursor = mydb.cursor()
    
    # Create database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    
    # Close cursor and connection
    mycursor.close()
    mydb.close()
    print("Database connection closed.")
    
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
finally:
    # Ensure connection is closed even if an error occurs
    try:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("Database connection closed.")
    except:
        pass