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
    # Assuring the shoe_id and shoe_size are the actual foreign keys that we want them to be
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shoe_size (
            shoe_id INT,
            shoe_size INT,
            PRIMARY KEY(shoe_id, shoe_size),
            FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id),
            FOREIGN KEY (shoe_size) REFERENCES size(size_id)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()