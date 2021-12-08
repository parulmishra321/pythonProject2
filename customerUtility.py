import mysql.connector as connector

class customerUtility:

    def __init__(self):
        self.connection = connector.connect(host='localhost',
                                            port='3306',
                                            user='root',
                                            password= '9211',
                                            database= 'pythonDB')
        query= 'create table if not exists customer(customerId int primary key, customerName varchar(300), customerDescription varchar(500), customerLocation varchar(500))'
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        print("CUSTOMER TABLE DID NOT EXIST. So Created Table CUSTOMER")

    def insert_cust_record(self):
        custId = int(input("Enter Customer ID: "))
        custName = (input("Enter Customer Name: "))
        custDescription = (input("Enter Customer Description: "))
        custLocation = (input("Enter Customer Location: "))

        query = "INSERT INTO customer( customerId , customerName ,customerDescription , customerLocation) values({},'{}','{}','{}')".format(
            custId, custName, custDescription, custLocation)
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        self.connection.commit()
        print("\nNEW CUSTOMER ADDED!!")

    def view_all_customers(self):
        query = "SELECT * FROM customer"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("CUSTOMER ID: ", row[0])
            print("CUSTOMER NAME: ", row[1])
            print("CUSTOMER DESCRIPTION: ", row[2])
            print("CUSTOMER LOCATION: ", row[3])
            print()
            print()

    def find_detail(self):
        query = "SELECT customerId, customerName FROM customer"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("CUSTOMER ID: ", row[0])
            print("CUSTOMER NAME: ", row[1])

    def list_user_attchedTo_cust(self):
        query = "SELECT count(*) FROM customer c join user u on c.customerId = u.customerId"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("No of Users attached to a customer: ", row[0])

    def customer_location(self):
        query = "SELECT customerId, customerName FROM customer WHERE customerLocation='Delhi'"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("CUSTOMER ID: ", row[0])
            print("CUSTOMER NAME: ", row[1])

    def customer_start_with_H(self):
        query = "SELECT customerId, customerName FROM customer WHERE customerName LIKE 'H%'"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("CUSTOMER ID: ", row[0])
            print("CUSTOMER NAME: ", row[1])

    def list_user_customer(self):
        query =  "SELECT userId, userFirstName, userLastName, userMobile, userEmail, customerName, customerLocation FROM customer c JOIN user u ON c.customerId = u.customerId"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("USER ID: ", row[0])
            print("USER FIRST NAME: ", row[1])
            print("USER LAST NAME: ", row[2])
            print("USER MOBILE: ", row[3])
            print("USER EMAIL: ", row[4])
            print("CUSTOMER NAME: ", row[5])
            print("CUSTOMER LOCATION: ", row[6])

    def average_user_count(self):
        query =  "SELECT avg(count) FROM( SELECT COUNT(*) AS Count FROM customer c JOIN user u ON c.customerId = u.customerId WHERE customerLocation='Delhi') as counts"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("Average no of User attached to Customer for location Delhi: ", row[0])

    def total_user_count(self):
        query = "SELECT COUNT(*) FROM customer c JOIN user u ON c.customerId = u.customerId WHERE customerLocation='Delhi'"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("Total no of User attached to Customer for location Delhi: ", row[0])


