import mysql.connector as connector

class userUtility:

    def __init__(self):
        self.connection = connector.connect(host='localhost',
                                            port='3306',
                                            user='root',
                                            password= '9211',
                                            database= 'pythonDB')

        query = 'CREATE TABLE IF NOT EXISTS user(userId int primary key, customerId int, userFirstName varchar(100), userLastName varchar(100), userMobile varchar(12), userEmail varchar(500))'

        mycursor = self.connection.cursor()
        mycursor.execute(query)
        print("USER TABLE DID NOT EXIST. So Created Table USER")

    def insert_user_record(self):
        userId = int(input("Enter User ID: "))
        custId = int(input("Enter Customer ID: "))
        userFirstName = (input("Enter User First Name: "))
        userLastName = (input("Enter User Last Name: "))
        userMobile = (input("Enter User Mobile Number: "))
        userEmail = (input("Enter User Email: "))

        query = "INSERT INTO user(userId, customerId, userFirstName, userLastName, userMobile , userEmail) values({},{},'{}','{}','{}','{}')".format(
            userId, custId, userFirstName, userLastName, userMobile, userEmail)
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        self.connection.commit()
        print("\nNEW USER ADDED!!")

    def view_all_users(self):
        query = "SELECT * FROM user"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("USER ID: ", row[0])
            print("CUSTOMER ID: ", row[1])
            print("USER FIRST NAME: ", row[2])
            print("USER LAST NAME: ", row[3])
            print("USER MOBILE: ", row[4])
            print("USER EMAIL: ", row[5])
            print()
            print()

    def user_sorting_order(self):
        query = "SELECT * FROM user GROUP BY userId ORDER BY userId DESC"
        mycursor = self.connection.cursor()
        mycursor.execute(query)
        for row in mycursor:
            print("USER ID: ", row[0])
            print("CUSTOMER ID: ", row[1])
            print("USER FIRST NAME: ", row[2])
            print("USER LAST NAME: ", row[3])
            print("USER MOBILE: ", row[4])
            print("USER EMAIL: ", row[5])
