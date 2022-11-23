from database import  DataBase

class Admin:
    def __init__(self):
        username = input("enter admin user name : ")
        password = input("enter admin password : ")
        self.username = username
        self.password = password

    def check(self):
        if(self.username == "AdMiN" and self.password == "this is the end"):
            return True
        return False
    def acceptUsers(self):
        if(not self.check):
            print("error this admin is not used!!!")
            return None
        adminDB = DataBase()
        unaccepted_users = list(adminDB.execute("SELECT id,email,fullName FROM users WHERE Accept_type = 0"))
        for i in unaccepted_users:
            print("user ID {}\t user Email : {} \tuser Full Name : {}".format(i[0],i[1],i[2]))
        userID = int(input("enter user id that you want to accept enter 0 to back"))
        while(userID!=0):
            adminDB.execute(f"UPDATE users SET Accept_type = 1 WHERE id = {userID} ")
            print("done >> ")
            userID = int(input("enter user id that you want to accept enter 0 to back"))
        adminDB.end()
        return None
            


