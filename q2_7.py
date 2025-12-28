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

    # Creating the new table (only if it doesn't exist) which contains the given variables
    # Assuring that customer_id is the primary key and is length 9, first_name and last_name are not null,
    # email is not null and unique, and city_id is a foreign key to city
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            customer_id VARCHAR(15) PRIMARY KEY,
            first_name VARCHAR(31) NOT NULL,
            last_name VARCHAR(31) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            city_id INT NOT NULL,
            
            CONSTRAINT CHECK (LENGTH(customer_id) = 9),
            FOREIGN KEY (city_id) REFERENCES city (city_id)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()