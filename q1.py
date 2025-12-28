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
    ## PUT YOUR QUERY ##
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()