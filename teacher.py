
from database import DataBase
from person import Person
from course import Course
from Assignment import Assignment

class Teacher(Person):
    def __init__(self,id,email,full_name,user_name,type_ID,admin_accept):
        super().__init__(id,email,full_name,user_name,type_ID,)
        self.courses_list = []
        self.admin_accept = admin_accept
        pass
    
    def view_solutions(self,courseID,Assignment_id):
         try:
            self.coursesList()
            if (courseID not in self.courses_list):
                return None
            teacherDB = DataBase()
            solutions =  list(teacherDB.execute(f"SELECT user_id,solution FROM solutions WHERE Assignment_id = {Assignment_id}"))
            teacherDB.end()
            return solutions
         except:
            print("sorry some of your information is incorrect!!!  ")    
    
    def coursesList(self):
        try:
            teacherDB = DataBase()
            if (self.type_ID == 2):
                self.courses_list=list(teacherDB.execute(f"SELECT course_ID FROM enrolled_course WHERE user_id = {self.id} AND Account_type = 2 "))
            else:
                self.courses_list=list(teacherDB.execute(f"SELECT course_ID FROM courses WHERE owner_id = {self.id} "))
            self.courses_list = [Cid[0] for Cid in self.courses_list]
            teacherDB.end()
        except:
            print("error in the data that you add it !!! ")
        finally:
            return self.courses_list
        
    def delete_Assignment(self,courseID):
        AssignmentID = int(input("enter Assignmet ID that you want to delete it "))
        if(courseID not in self.courses_list):
            print("this Assignment not in your course")
            return None
        Course(courseID).deleteAssignment(AssignmentID)

    def setGrade(self,courseID):
        AssignmentID = int(input("enter Assignmet ID : "))
        l = Course(courseID).list_of_Assignments()
        if(AssignmentID not in l or courseID not in self.courses_list):
            print("this Assignment id not for this course")
            return None
        solutionID = int (input("enter solutionID"))
        grade = int(input("enter grade"))
        comment = int(input("enter comment"))
        Assignment(AssignmentID).set_grade(solutionID,grade,comment)

        pass



