from customerUtility import *
from userUtility import *

def main():
   custObject = customerUtility()
   userObject = userUtility()
   while True:
       print("*************************************WELCOME***********************************");
       print()
       print("1. Insert a new Customer");
       print("2. Insert a new User");
       print("3. Display all Customers");
       print("4. Display all Users");
       print("5. List All the Customers with following details - name and customer id");
       print("6. Find no of Users attached to a customer");
       print("7. List All the Customers whose location is 'Delhi'");
       print("8. List All the Customers whose name start with Alphabet 'H'");
       print("9. List All the Users in sorting order of user count (descending order)");
       print("10. List All the Users with their customer name and location");
       print("11. Find Average user count attached to Customer for location Delhi");
       print("12. Find Total user count attached to Customer for location Delhi");
       print("13. Exit.")
       print()
       try:
          choice = int(input("Enter Your Choice: "))
          if(choice == 1):
              custObject.insert_cust_record()
          elif(choice == 2):
              userObject.insert_user_record()
          elif(choice == 3):
              custObject.view_all_customers()
          elif (choice == 4):
              userObject.view_all_users()
          elif (choice == 5):
              custObject.find_detail()
          elif (choice == 6):
              custObject.list_user_attchedTo_cust()
          elif (choice == 7):
              custObject.customer_location()
          elif (choice == 8):
              custObject.customer_start_with_H()
          elif (choice == 9):
              userObject.user_sorting_order()
          elif (choice == 10):
              custObject.list_user_customer()
          elif (choice == 11):
              custObject.average_user_count()
          elif (choice == 12):
              custObject.total_user_count()
          elif (choice == 13):
              break;
          else:
              print("INVALID INPUT!! TRY AGAIN")
       except Exception as e:
           print(e)
           print("INVALID DETAILS!! TRY AGAIN")

if __name__ == "__main__":
    main()
