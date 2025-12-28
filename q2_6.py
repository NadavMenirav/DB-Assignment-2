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
    # Assuring the city_id is hte primary key, the city_name is not null, and country_id is a foreign key to country
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS city (
            city_id INT PRIMARY KEY,
            city_name VARCHAR(63) NOT NULL,
            country_id INT NOT NULL,
            FOREIGN KEY(country_id) REFERENCES country(country_id)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()