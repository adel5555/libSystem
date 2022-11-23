from database import DataBase
class Assignment:
    def __init__(self,AssignmentID):
        AssignmentDataBase = DataBase()
        obj = []
        try:
            obj = list(AssignmentDataBase.execute(f"SELECT * FROM Assignments WHERE Assignment_id = {AssignmentID}"))
            obj =obj[0]
            self.AssignmentId = obj[0]
            self.courseId = obj[1]
            self.AssignmentQuestions = obj[2]
            self.fullMark=obj[3]
            self.AssignmentDeadLine=obj[4]
        except:
            print("sory this assignments is not exist")
        finally:
            AssignmentDataBase.end()
        pass
    
    
    def deleteAssignment(self):
        AssignmentDataBase = DataBase()
        try:
            AssignmentDataBase.execute(f"DELETE FROM Assignments WHERE Assignment_id = {self.AssignmentId}")
        except:
            print("sory this assignments is not exist")
        finally:
            AssignmentDataBase.end()

    def viewSolutions(self,userID):
        AssignmentDataBase = DataBase()
        res =[]
        try:
            res = list(AssignmentDataBase.execute(f"SELECT T2.fullName,T1.solution,T1.grade from solutions T1,users T2 WHERE T1.Assignment_id = {self.AssignmentId} AND T2.id=T1.user_id AND T1.user_id = {userID}"))
            if(len(res)>0):
                for i in res:
                    if(i[2] is None):
                        print(f"\tAssignment ID : {self.AssignmentId}  Assignment name {self.AssignmentQuestions} {i[0]} solutions on this is:\n\t\t{i[1]}\t no mark from doctor or TA\n ")
                    else:
                        print(f"\tAssignment ID : {self.AssignmentId}  Assignment name {self.AssignmentQuestions} {i[0]} solutions on this is:\n\t\t{i[1]}\t your mark is {i[2]} full mark is {self.fullMark}\n ")
            else:   
                print(f"\tAssignment ID : {self.AssignmentId}  Assignment name {self.AssignmentQuestions} solutions on this is:\n\t\tno solution on this assignments\n ")
        except:
            print("sory this assignments is not exist")
        finally:
            AssignmentDataBase.end()
        return res
    
    def teacherGradeReport(self):
        AssignmentDataBase = DataBase()
        res =[]
        try:
            res = list(AssignmentDataBase.execute(f"SELECT T2.fullName,T1.solution,T1.solution_id from solutions T1,users T2 WHERE T1.Assignment_id = {self.AssignmentId} AND T2.id=T1.user_id  "))
            for i in res:
                print(f"\tstudent with name ,{i[0]} the solution is: \n\t\t {i[1]} ")
        except:
            print("sory this assignments is not exist")
        finally:
            AssignmentDataBase.end()
        return res

    def set_grade(self,solutionID,grade,comment):
        AssignmentDB=DataBase()
        AssignmentDB.execute(f"UPDATE solutions SET grade = '{grade}', comment = '{comment}' WHERE solution_id = {solutionID} ")
        AssignmentDB.end()
        pass
    
    def info(self):
        print("Assignment ID : {}\tAssignment Name : {}".format(self.AssignmentId,self.AssignmentQuestions))

