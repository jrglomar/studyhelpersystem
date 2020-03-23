import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='1234',
                                        database='studyhelpersystem')
cursor = mydb.cursor(buffered=True)


class TestDb:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def read(self):
        
        self.cursor.execute("SELECT ReminderTypeID, Description  FROM REMINDERTYPE;")
        self.mydb.commit()
        
        x = dict(self.cursor.fetchall())
        for z in x:
            print(x[z])


        
class Validation:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor
    
    def validationUserRegistration(self, username):
        try:
            self.cursor.execute("SELECT * FROM STUDENTS WHERE Username = %s;", username)
            return (self.cursor.fetchone())
        except:
            return False

    def validationReminderType(self, data):
        try:
            self.cursor.execute("SELECT * FROM REMINDERTYPE WHERE Description = %s;", data)
            return (self.cursor.fetchone())
        except:
            return False

class UserDb:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def userLogin(self, data):
        try:
            self.cursor.execute("SELECT * FROM students WHERE Username = %s AND Password = %s;", data)
            return (self.cursor.fetchone())
        except:
            return False

    def userRegistration(self, data, username):
        try:
            username = (username,)
            self.validation = Validation()
            reg = self.validation.validationUserRegistration(username)
            if reg:
                pass
            else:
                try:
                    self.cursor.execute("INSERT INTO STUDENTS(Username,Password) VALUES(%s, %s);", (data))
                    self.mydb.commit()
                except:
                    pass
            return reg
        except:
            return False

    def getStudentID(self, username):
            self.cursor.execute("SELECT StudentID FROM STUDENTS WHERE Username = %s;",
            (username, )
            )

            return (self.cursor.fetchone())

    def newTask(self, data):
            newTask = self.cursor.execute("INSERT INTO REMINDER(ReminderTypeID, Title, Due_Date, Details, StudentID, Subject) VALUES(%s, %s, %s, %s, %s, %s);",
            (data))
            self.mydb.commit()

    def newType(self, data):
        try:
            self.validation = Validation()
            newType = self.validation.validationReminderType(data)
            if newType:
                pass
            else:
                try:
                    self.cursor.execute("INSERT INTO REMINDERTYPE(Description) VALUES(%s);", 
                    (data))
                    self.mydb.commit()
                except:
                    pass
        except:
            return False

class TaskOptionMenu:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def getType(self):
        self.cursor.execute("SELECT ReminderTypeID, Description  FROM REMINDERTYPE;")
        self.mydb.commit()
        
        return (self.cursor.fetchall())

    def getSubject(self, id):
        self.cursor.execute("SELECT Name FROM SUBJECT WHERE StudentID=%s;", (id, ))
        self.mydb.commit()

        return (self.cursor.fetchall())

    def getReminder(self, remId):
        self.cursor.execute("SELECT Description FROM ReminderType WHERE ReminderTypeID = %s;", (remId, ))
        self.mydb.commit()

        return (self.cursor.fetchone())

class DisplayData:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def displayTask(self, StudentID):
        self.cursor.execute("SELECT * FROM REMINDER WHERE StudentID = %s;", 
            (StudentID, )
        )
        x = self.cursor.fetchall()
        self.mydb.commit()

        return x
        
class Subject:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def newSubject(self, data):
        self.cursor.execute("INSERT INTO SUBJECT (Name, Day_Schedule, Description, Start_Time, End_Time, StudentID) VALUES (%s, %s, %s, %s, %s, %s);",
                            (data)
        )
        self.mydb.commit()

    def displaySubject(self, StudentID):
        self.cursor.execute("SELECT * FROM SUBJECT WHERE StudentID = %s;", 
            (StudentID, )
            )
        self.mydb.commit()

        return self.cursor.fetchall()

    def deleteSubject(self, id):
        self.cursor.execute("DELETE FROM SUBJECT WHERE SubjectID = %s;", (id, ))
        self.mydb.commit()

    def updateSubject(self, data):
        self.cursor.execute("UPDATE SUBJECT SET Name=%s, Start_Time=%s, End_Time=%s, Description=%s, Day_Schedule=%s WHERE SubjectID=%s;", (data))
        self.mydb.commit()

class Task:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor
    
    def deleteTask(self, id):
        self.cursor.execute("DELETE FROM REMINDER WHERE ReminderID = %s;", (id, ))
        self.mydb.commit()

    def updateTask(self, data):
        self.cursor.execute("UPDATE REMINDER SET Title=%s, Subject=%s, Details=%s, Due_Date=%s WHERE ReminderID=%s;", (data))
        self.mydb.commit()

class Home:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor
    def getTodaySubject(self, StudentID, DayToday):
        self.cursor.execute("SELECT * FROM Subject WHERE StudentID = %s AND Day_Schedule = %s;", (StudentID, DayToday))
        self.mydb.commit()

        return self.cursor.fetchall()

    def getTodayTask(self, StudentID, DateToday):
        self.cursor.execute("SELECT * FROM Reminder WHERE StudentID = %s AND Due_Date = %s;", (StudentID, DateToday))
        self.mydb.commit()

        return self.cursor.fetchall()

class Progress:
    def __init__(self):
        self.mydb = mydb
        self.cursor = cursor

    def insertStandard(self, data):

        for row in data:
            self.cursor.execute("INSERT INTO GRADINGSYSTEM(SubjectID, Type, Percentage) VALUES(%s, %s, %s);", (row))
        
        self.mydb.commit()

    def insertCustom(self, data):

        self.cursor.execute("INSERT INTO GRADINGSYSTEM(SubjectID, Type, Percentage) VALUES(%s, %s, %s);", (data))
        self.mydb.commit()

    def displayGs(self, SubjectID):

        self.cursor.execute("SELECT GradingSystemID, Type, Percentage FROM GRADINGSYSTEM WHERE SubjectID = %s;", (SubjectID, ))
        self.mydb.commit()

        return self.cursor.fetchall()

    def gsValidation(self, SubjectID):

        self.cursor.execute("SELECT Percentage FROM GRADINGSYSTEM WHERE SubjectID = %s;", (SubjectID, ))
        self.mydb.commit()

        return self.cursor.fetchall()

    def deleteGs(self, GradingSystemID):
        self.cursor.execute("DELETE FROM GRADINGSYSTEM WHERE GradingSystemID = %s;", (GradingSystemID, ))
        self.mydb.commit()
        
    
    def getType(self, subjectID):
        self.cursor.execute("SELECT GradingSystemID, Type  FROM GRADINGSYSTEM WHERE SubjectID = %s;", (subjectID, ))
        self.mydb.commit()
        
        return (self.cursor.fetchall())

    def insertAcademic(self, data):
        self.cursor.execute("INSERT INTO AcademicActivity (SubjectID, GradingSystemID, Title, Score, Max_Score, Result) VALUES(%s,%s,%s,%s,%s,%s);", (data))
        self.mydb.commit()
