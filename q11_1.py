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
    # Creating a view that shoes the total sales per shoe. Using regular join instead of join because we only want to
    # display the shoes that have been sold
    cursor.execute("""
        CREATE VIEW total_sales_per_shoe AS
        SELECT shoe.shoe_id shoe_id, shoe.shoe_name shoe_name, SUM(shoe.price) total_revenue
        FROM shoe JOIN order_shoe ON shoe.shoe_id = order_shoe.shoe_id
        GROUP BY shoe.shoe_id;
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()

    # Close the cursor and the connection
    cursor.close()
    mydb.close()