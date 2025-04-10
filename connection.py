
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='Andargachew',
    password='@andarg2329',
    database='dashboard'
)


mycursor = mydb.cursor()
#create a table  named customer in the database
mycursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(255) NOT NULL,
                 email VARCHAR(255) NOT NULL UNIQUE
                 )""")
print("Table created successfully")




#insert some customer data 
# sql= """INSERT INTO customers (name, email) VALUES
# (%s, %s)"""
# val= ("andarg", "andargachewg@gmail.com")
# mycursor.execute(sql, val)
# mydb.commit()

# print(mycursor.rowcount, "record(s) inserted.")

#Read the customer data from the database
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

print("Customer: ")
for row in myresult:
    print(row)

    #update the cutomer's email
    sql = "UPDATE customers SET  email=%s WHERE id=%s"
    val=("whonows@gmail.com", 1)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record(s) updated.")


#Read the updated customer data
mycursor.execute("SELECT * FROM customers WHERE id= 1")
myresult = mycursor.fetchone()
print("Updated: customer: ")
print(myresult)

#Delete a customer
sql = "DELETE FROM customers WHERE id = 2"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted.")

# Close connections
mycursor.close()
mydb.close()

print("Database connection closed")