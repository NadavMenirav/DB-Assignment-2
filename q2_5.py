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
    # Creating the new table (only if it doesn't exist) which contains the given variables
    # Assuring that country_id is the primary key of the table and country_name is not null
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS country (
            country_id INT PRIMARY KEY,
            country_name VARCHAR(63) NOT NULL
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()