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
    # For each customer, we return their first name, last name, and the total amount of money he spent (can be zero)
    # Using LEFT JOIN for the case where a customer has not made any purchases and coalesce to return 0 in that case
    cursor.execute("""
        SELECT c.first_name first_name, c.last_name last_name, COALESCE(SUM(s.price), 0) total_amount_spent
        FROM customer c
         LEFT JOIN order_customer oc ON c.customer_id = oc.customer_id 
         LEFT JOIN order_shoe os ON oc.order_id = os.order_id 
         LEFT JOIN shoe s ON os.shoe_id = s.shoe_id
        GROUP BY c.customer_id;
    """)

    # Fetch and print all results separated by commas
    print(', '.join(str(row) for row in cursor.fetchall()))

    # Close the cursor and the connection
    cursor.close()
    mydb.close()