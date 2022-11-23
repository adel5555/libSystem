from database import DataBase
from message import Message

class Person():
    def __init__(self,id,email,full_name,user_name,type_ID):
        self.id = id
        self.email = email
        self.full_name = full_name
        self.user_name = user_name
        self.type_ID = type_ID
        self.list_my_messages=[]
        self.list_recieveMessage=dict()

    def getFullName(self):
        return self.full_name
    
    def getEmail(self):
        return self.email
    
    def getUserName(self):
        return self.user_name
    
    def getFullName(self):
        return self.full_name
    
    def getID(self):
        return self.id
    
    def getType(self):
        return self.type_ID
    
    def viewReceiveMessage(self):
        try:
            personDataBase = DataBase()
            res=list(personDataBase.execute(f"SELECT * from messages WHERE reciever_id = {self.id} AND M_type = 0"))
            new_resulte =dict()
            for i in res:
                if(len(i)>=1):
                    new_resulte[i] = Message(i[0],i[1],i[2],i[3],i[4]).allReplays()
            if(len(res)==0):
                    print("there is no messages ;)")
            self.list_recieveMessage=new_resulte
            personDataBase.end()
        except:
            print("sorry error in storing!!! please try again  ")
        finally:
            return self.list_recieveMessage
    
    def viewMyMessage(self):
        try:
            personDataBase = DataBase()
            res=list(personDataBase.execute(f"SELECT * from messages WHERE user_id = {self.id} AND M_type = 0"))
            new_resulte =dict()
            for i in res:
                if(len(i)>=1):
                    new_resulte[i] = Message(i[0],i[1],i[2],i[3],i[4]).allReplays()
            if(len(res)==0):
                print("there is no recieve messages ;)")
            self.list_my_messages=new_resulte
            personDataBase.end()
        except:
            print("sorry error in storing!!! please try again  ")
        finally:
            return self.list_my_messages
    
    def sendmessage(self):
        reciever_ID = int(input("Enter recever ID : "))
        message = input("Enter the message : ")
        personDB = DataBase()
        personDB.execute(f"INSERT INTO messages (user_id,reciever_id,message,M_type) VALUES({self.id},{reciever_ID},'{message}',0)")
        personDB.end()
        pass
    
    def createpost(self):
        reciever_ID = int(input("Enter courseID : "))
        message = input("Enter the post message : ")
        personDB = DataBase()
        personDB.execute(f"INSERT INTO messages (user_id,reciever_id,message,M_type) VALUES({self.id},{reciever_ID},'{message}',1)")
        personDB.end()
        pass
    
    def addreplay(self):
        message_ID = int(input("enter message ID or post ID : "))
        personDataBase = DataBase()
        res=list(personDataBase.execute(f"SELECT * from messages WHERE message_id = {message_ID}"))
        if(len(res)==0):
            print("this message is not exist !! ")
            return None
        replay_message = input("enter replay Message : ")
        personDataBase.execute(f"INSERT INTO Replay (message_id,replayer_id,replay_message)VALUES({message_ID},{self.id},{replay_message})")
        personDataBase.end()
        pass



# Person(3,1,1,1,1).sendmessage()