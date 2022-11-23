from teacher import Teacher
from database import DataBase
from course import Course


class TeacherAssistent(Teacher):
    def __init__(self, id, email, full_name, user_name, type_ID, admin_accept):
        super().__init__(id, email, full_name, user_name, type_ID, admin_accept)
        self.list_of_requiests = []
    def TA_create_assignment(self,course_id,Assignment_Question,FullMark,Assignment_dead_line):
        self.coursesList()
        TABD = DataBase()
        TABD.execute(f"INSERT INTO Assignments (course_ID,Assigment_question,FullMark,Assigment_dead_line)VALUES({course_id},'{Assignment_Question}',{FullMark},'{Assignment_dead_line}');")
        TABD.end()

    def TA_Answer_requests(self):
        TeacherAssistentBD = DataBase()
        while(True):
            Teacher_requist = list(TeacherAssistentBD.execute(f"SELECT * from Teacher WHERE user_id = {self.id}"))
            courses = [i[0] for i in Teacher_requist]
            for courseid in courses:
                print(Course(courseid).info())
            courseID = int(input("enter courseID that you want to accept or regict it or enter 0 to break : "))
            if(courseID not in courses):
                break
            TeacherAssistentBD.execute(f"INSERT INTO enrolled_course (course_ID,user_id,Account_type)VALUES({courseID},{self.id},2); ")
            TeacherAssistentBD.execute(f"DELETE FORM Teacher WHERE user_id = {self.id} AND course_id = {courseID}; ")
        TeacherAssistentBD.end()

    
        


        pass
