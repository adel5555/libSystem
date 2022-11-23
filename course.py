from database import DataBase
from Assignment import Assignment
import datetime
class Course:
    
    def __init__(self,id):
        self.id = id
        courseDB = DataBase()
        course_info = list(courseDB.execute(f"SELECT * FROM courses WHERE course_id = {self.id}"))
        self.course_name=course_info[0][1]
        self.course_owner_id = course_info[0][2]
        self.course_password = course_info[0][3]
        self.course_dead_line = course_info[0][4]
        self.list_registered_student = []
        self.list_enrolled_TA = []
        self.list_of_required_courses_Id = set()
        self.list_of_Assignmet = []
        self.list_course_message = []
    
    def __list_to__(id,flag_if_student_or_TA):
        list_emp = []
        try:
            courseBD = DataBase()
            list_emp = [i[0] for i in list(courseBD.execute(f"SELECT user_id FROM enrolled_course WHERE course_id = {id} and Account_type = {flag_if_student_or_TA}"))]
            courseBD.end()
        except:
            print("error no register course:   ")
            pass
        finally:
            return list_emp
    
    def list_registered_student_ID(self):
         self.list_registered_student = Course.__list_to__(self.id,1)  
         return self.list_registered_student
    
    def list_enrolled_TA_method(self):
         self.list_enrolled_TA = Course.__list_to__(self.id,2)  
         return self.list_enrolled_TA
    
    def list_of_required_course(self):
        list_emp = []
        try:
            courseBD = DataBase()
            list_emp = [i[0] for i in list(courseBD.execute(f"SELECT requied_id FROM requirment WHERE course_id = {self.id}"))]
            courseBD.end()
        except:
            print("error no register course:   ")
            pass
        finally:
            self.list_of_required_courses_Id=list_emp
            return self.list_of_required_courses_Id
    
    def set_requierment(self):
        try:
            addAllReaquirments=[]
            requ = int(input("enter reqiered course ID or add 0 to back :"))
            while(requ != 0):
                addAllReaquirments.append(requ)
                requ = int(input("enter reqiered course IDor add 0 to back :"))
                
            courseBD = DataBase()
            for requier in addAllReaquirments:
                courseBD.execute(f"INSERT INTO requirment (course_id,requied_id)VALUES({self.id},{requier});")
            courseBD.end()
        except:
            print("error no course with this name or you add this requirment befor:   ")

    def addAssignmet(self):
        try:
            courseBD = DataBase()
            while(True):
                AssignmentQuestions = input("enter Assignment question : ")
                fullMark = input("enter fullMark for this Assignment : ")
                AssignmentDeadLine = input('Enter course dead_line in YYYY-MM-DD format')
                year, month, day = map(int, AssignmentDeadLine.split('-'))
                date1 = datetime.date(year, month, day)
                courseBD.execute(f"INSERT INTO Assignments(course_ID,Assigment_question,FullMark, Assigment_dead_line)VALUES({self.id},'{AssignmentQuestions}',{fullMark},'{AssignmentDeadLine}');")
                option = input("add more ?? etner 1 to add new assignment on this course other ways enter 0 : ")
                if(option!="1"):
                    break
            

            courseBD.end()
        except:
            print("error no course with this name or you add this requirment befor:   ")

    def list_of_Assignments(self):
        courseDB = DataBase()
        self.list_of_Assignmet = list(courseDB.execute(f"SELECT Assignment_id from Assignments WHERE course_ID = {self.id}"))
        self.list_of_Assignmet = [id[0] for id in self.list_of_Assignmet]
        courseDB.end()
        return self.list_of_Assignmet

    def list_course_messages(self):
        pass

    def viewSolutions(self,userId):
        self.list_of_Assignments()
        print(self.course_name + ", the id for this course is " + str(self.id) + ", the number of assignments is " + str(len(self.list_of_Assignmet))+":")
        for i in self.list_of_Assignmet:
            Assignment(i).viewSolutions(userId)
    
    def DoctorGradeReport(self):
        self.list_of_Assignments()
        print(self.course_name + ", the id for this course is " + str(self.id) + ", the number of assignments is " + str(len(self.list_of_Assignmet))+":")
        for i in self.list_of_Assignmet:
            Assignment(i).teacherGradeReport()
        
    def info(self):
        return "Course ID : " + str(self.id) + "   course Name is : " + self.course_name 
    
    def deleteCourse(self):
        CourseDb = DataBase()
        CourseDb.execute(f"DELETE FROM courses WHERE course_id = {self.id}")
    
    def deleteAssignment(self,AssignmentID):
        self.list_of_Assignments()
        if(AssignmentID not in self.list_of_Assignmet):
            print("sorry this assignmet not in this course")
            return None
        Assignment(AssignmentID).deleteAssignment()
        
    def courseWithAssignments(self):
        self.list_of_Assignments()
        print(self.info())
        for i in self.list_of_Assignmet:
            Assignment(i).info()


# c=Course(1)
# c.viewSolutions(1)