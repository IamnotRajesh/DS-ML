#importing the sql lite
import sqlite3
#creating a connection to the database file 
db_name = "users.db"
conn = sqlite3.connect(db_name)
c = conn.cursor()
print("Opened database successfully")

#creating the table with username and password
def createTable():
    query = "DROP TABLE IF EXISTS login"
    c.execute(query)
    print("table dropped successfully if it existed")
          
    c.execute("CREATE TABLE king(Username VARCHAR Password VARCHAR)")
    c.execute(query)
    conn.commit()

#inserting the value of username and password
# def  insertData():
#     username = input("Enter your username: ")
#     password = input("Enter your password:")
#     c.execute("INSERT INTO login VALUES(?,?)", (username,password))
#     conn.commit()

createTable()
#insertData()
# def viewData(username, password):
#     query = "SELECT * FROM login WHERE  Username=? AND Password=?"
#     c.execute(query ,(username, password))
#     result = c.fetchone()
#     conn.commit()
#     return result

# def signIn():
#     ans = print("Login(Y/N)")
#     if  ans ==  'y' or ans=='Y':
#         username = input("Enter your username: ")
#         password = input("Enter your password:")
#         if  viewData(username, password) is None :
#             print("Invalid Credentials")
#         elif  viewData(username, password):
#             print("Proceed to Login")
#         else:
#             print("Something is wrong")
    
# def updatePass(username, password):
#     oldpass = input("Enter your current password:")
#     newpass = input("Enter your new password")
#     if viewData(username,password) is not None:
#             query ="UPDATE login SET Password=%s WHERE Username=%s"
#             c.execute(query,(newpass, username,))
#             conn.commit()
#     else:
#         print("Your Current Password is Wrong")

# def deleteUser(username):
#     query="DELETE from login where username = ? "
#     c.execute(query,(username,))
#     conn.commit()

# if __name__=="__main__":
#     while True:
       




