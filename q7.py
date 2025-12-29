import mysql.connector

if __name__ == '__main__':
    # Establish the connection to the database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="## PUT THE CORRECT DATABASE HERE IF NEEDED ##",
        port='3307',
    )

    # Create a cursor object to execute queries
    cursor = mydb.cursor()

    # Execute the SQL query
    cursor.execute("""
        ## PUT YOUR QUERY HERE ##
    """)

    # Fetch and print all results separated by commas
    print(', '.join(str(row) for row in cursor.fetchall()))

    # Close the cursor and the connection
    cursor.close()
    mydb.close()