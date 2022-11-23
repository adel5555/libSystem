import database
class Message():
    def __init__(self,sender_id,reciever_id,message_id,message,message_type):
        self.message_id = message_id
        self.message = message
        self.sender_id = sender_id
        self.reciever_id = reciever_id
        self.message_type = message_type
        self.list_reply = []
    def addReplay(self,user_id,replay_message):
        try:
            replayDataBase = database.DataBase()
            replayDataBase.execute(f"INSERT INTO Replay (message_id,replayer_id,replay_message)VALUES( {self.message_id},{user_id},'{replay_message}');")
            replayDataBase.end()
        except:
            print("sorry error in storing data!!! : try again later  ")

    def allReplays(self):
        try:
            replayDataBase = database.DataBase()
            print("message ID is : {}\tthe message is : {}".format(self.message_id,self.message))
            self.list_reply=list(replayDataBase.execute(f"SELECT replay_message from Replay WHERE message_id = {self.message_id}"))
            print("the replay for this message is: ")
            for i in self.list_reply:
                print("\t{}".format(i[0]))
            replayDataBase.end()
            return self.list_reply
        except:
            return self.list_reply




