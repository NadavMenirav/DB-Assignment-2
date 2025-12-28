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
    # Assuring special_id is the primary key, shoe_id is not null and is a foreign key to shoe.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS upcoming(
            special_id INT PRIMARY KEY,
            shoe_id INT NOT NULL,
            collection_name VARCHAR(31),
            release_date DATETIME,
            FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()