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
    # Creating the table that connects the company_order table and the customer table
    # Assuring that both columns form the primary key and each one is a foreign key to their respected table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS order_customer (
            order_id INT,
            customer_id VARCHAR(15),
            
            PRIMARY KEY(customer_id, order_id),
            FOREIGN KEY (order_id) REFERENCES company_order(order_id),
            FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
        )
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()