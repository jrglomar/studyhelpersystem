import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='1234',
                                        database='studyhelper')
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

    def getSubject(self):
        self.cursor.execute("SELECT Name FROM SUBJECT;")
        self.mydb.commit()

        return (self.cursor.fetchall())
    

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
