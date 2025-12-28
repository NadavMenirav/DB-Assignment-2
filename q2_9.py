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
    # Assuring that both the order_id and shoe_id are the primary keys and are foreign keys
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_shoe (
            order_id INT,
            shoe_id INT,
            
            PRIMARY KEY(order_id, shoe_id),
            FOREIGN KEY (order_id) REFERENCES company_order(order_id),
            FOREIGN KEY (shoe_id) REFERENCES shoe(shoe_id)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()