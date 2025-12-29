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
    # In the top query, we are renaming the shoe_name as name, and hardcoding the value 'Inventory' into source
    # In the bottom query, we are renaming the collection_name as name, and hardcoding the value 'Upcoming Release'
    # into source
    # The UNION of both queries gives us the desired table, a table with a name column, containing both the
    # regular shoes and the upcoming shoes, and a source column, containing where that specific row came from.
    cursor.execute("""
        SELECT shoe.shoe_name name, 'Inventory' AS source
        FROM shoe
        
        UNION
        
        SELECT upcoming.collection_name name, 'Upcoming Release' AS source
        FROM upcoming;
    """)

    # Fetch and print all results separated by commas
    print(', '.join(str(row) for row in cursor.fetchall()))

    # Close the cursor and the connection
    cursor.close()
    mydb.close()