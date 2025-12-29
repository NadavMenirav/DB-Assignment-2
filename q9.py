import mysql.connector

if __name__ == '__main__':
    # Establish the connection to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port='3307',
    )

    # Create a cursor object to execute queries
    cursor = mydb.cursor()

    # Execute the SQL query
    cursor.execute("""
        SELECT sh.shoe_name shoe_name, COUNT(si.size_id) amount_sizes_available
        FROM shoe sh 
        LEFT JOIN shoe_size ss ON sh.shoe_id = ss.shoe_id
        LEFT JOIN size si ON ss.size_id = si.size_id
        GROUP BY sh.shoe_id
    """)

    # Fetch and print all results separated by commas
    print(', '.join(str(row) for row in cursor.fetchall()))

    # Close the cursor and the connection
    cursor.close()
    mydb.close()