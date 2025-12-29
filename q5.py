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
    # Using the ALTER TABLE command to add the pre_order_available column (which is a single bit value which
    # is 0 by default) to the upcoming table
    cursor.execute("""
        ALTER TABLE upcoming
        ADD pre_order_available BIT DEFAULT 0;
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()