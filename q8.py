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
    # Returning the average price for each shoe size form highest to lowest.
    # Trying to find a correlation between a shoe price and its size
    cursor.execute("""
        SELECT si.european_number european_size, si.us_number us_size, AVG(sh.price) average_price
        FROM shoe sh
        JOIN shoe_size ss ON sh.shoe_id = ss.shoe_id
        JOIN size si ON ss.size_id = si.size_id
        GROUP BY si.size_id
        ORDER BY average_price DESC;
    """)

    # Fetch and print all results separated by commas
    print(', '.join(str(row) for row in cursor.fetchall()))

    # Close the cursor and the connection
    cursor.close()
    mydb.close()