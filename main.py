from tkinter import *
from db.database import *
import datetime as dt
from tkcalendar import DateEntry
from tkinter.scrolledtext import ScrolledText


homeColor = "#bbe1fa"           # THE HOME SCREEN MAIN COLOR    (LIGHTEST)
headerColor = "#182952"         # THE HEADER FRAME COLOR        (DARKER)
mainColor = "steel blue"           # THE START SCREEN MAIN COLOR   (DARKER)
menuColor = "#1b262c"           # THE MENU FRAME COLOR          (DARKEST)       
buttonColor = "#1b262c"         # THE BUTTON COLOR              (DARKEST) OR (LIGHTEST)

headerFontColor = "#ffffff"     # LIGHTER
labelFontColor = "#ffffff"      # LIGHT
labelDarkFontColor = "#000000"  # DARK
buttonFontColor = "#ffffff"     # LIGHTEST
titleFontColor = "#30e3ca"      # CUSTOM COLOR


date = dt.datetime.now()           # GET DATE NOW
mixed = (date.strftime("%A")
 + ", " + date.strftime("%B") 
 + " " + date.strftime("%d"))      # FOR LABEL TODAY
lastyear = (date.strftime("%Y"))
lastyear = str(int(lastyear)-1) # GET LAST YEAR

### 

studID = 1
username = ""


def initID(page):
        db = UserDb()
        global username
        x = (db.getStudentID(username))
        global studID
        studID = x[0]
        app = App()
        app.show_frame(page)
        app.mainloop()

def defaultReso(parent):        # DEFAULT RESO TO CENTER SCREEN
    root = parent
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x = int(width/2 - 1000/2)
    y = int(height/2 - 760/2)
    reso = "1000x700+" + str(x) + "+" + str(y)

    return reso

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        reso = defaultReso(self)

        # Window Config
        self.title('Study Helper')
        self.geometry(reso)
        self.resizable(width=False, height=False)
        container = Frame(self)
        container.place(x=0, y=0, width=1000, height=700)

        self.frames = {}
        for F in (LoginScreen, RegistrationScreen, HomeScreen,
        ScheduleScreen, TaskScreen, ProgressScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.place(x=0, y=0, width=1000, height=1000)
            frame.configure(bg=mainColor)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class LoginScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.homeFrame()
        self.logAlert = StringVar()
        
        # Logo
        logo = PhotoImage(file = "images\logo.png")
        Logo = Label(self.homeFrame, image=logo, bg=mainColor, fg=labelFontColor)
        Logo.image = logo
        Logo.place(x=0, y=90, width=500)

        # ACCOUNT LOGIN LABEL
        Label(self.homeFrame, text="Account Login", bg=mainColor, fg=buttonFontColor, font=("Calibri 15 bold")).place(x=0, y=420, width=500)

        # USERNAME AND PASSWORD ENTRIES
        Label(self.homeFrame, text="Username", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=58, y=460, width=300)
        self.userLoginEntry = Entry(self.homeFrame)
        self.userLoginEntry.place(x=180, y=480, width = 150)
        Label(self.homeFrame, text="Password", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=55, y=500, width=300)
        self.passLoginEntry = Entry(self.homeFrame, show="*")
        self.passLoginEntry.place(x=180, y=520, width = 150)

        # LOGIN BUTTON
        Button(self.homeFrame, text="Login", bg=buttonColor, fg=buttonFontColor, font=("Calibri 10"), relief = FLAT,
                command=self.userLogin).place(x=180, y=550, width=150)

        # ALERT LABEL
        Label(self.homeFrame, textvariable=self.logAlert, bg=mainColor, fg="red", font = ("Calibri 9")).place(x=0, y=580, width=500)

        # TO REGISTRATION SCREEN
        Label(self.homeFrame, text="Don't have an account yet?", bg=mainColor, fg=labelFontColor, font =("Calibri 9")).place(x=122, y=650, width=200)
        Button(self.homeFrame, text="Click here", bg=mainColor, fg=titleFontColor, font = ("Calibri 9"), relief=FLAT,
                command=lambda: controller.show_frame("RegistrationScreen")).place(x=300, y=648, width=55)
    
    def homeFrame(self):
        self.homeFrame = Frame(self)
        self.homeFrame.place(x=250, y=0, width=500, height=700)
        self.homeFrame.configure(bg=mainColor)

    def userLogin(self):
        self.db = UserDb()
        data = (self.userLoginEntry.get(), self.passLoginEntry.get())

        if self.userLoginEntry.get() == "":
                self.logAlert.set("Enter Username First")
        elif self.passLoginEntry.get() == "":
                self.logAlert.set("Enter Password First")
                
        else:
                test = self.db.userLogin(data)
                if test:
                        global username
                        username = self.userLoginEntry.get()
                        self.controller.destroy()
                        initID("HomeScreen")
                        
                else:
                        self.logAlert.set("Wrong username/password")
      
class RegistrationScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.homeFrame()
        self.regAlert = StringVar()
        
        # Logo
        logo = PhotoImage(file = "images\logo.png")
        Logo = Label(self.homeFrame, image=logo, bg=mainColor, fg=labelFontColor)
        Logo.image = logo
        Logo.place(x=0, y=90, width=500)

        # ACCOUNT LOGIN LABEL
        Label(self.homeFrame, text="Account Registration", bg=mainColor, fg=buttonFontColor, font=("Calibri 15 bold")).place(x=0, y=420, width=500)

        # USERNAME AND PASSWORD ENTRIES
        Label(self.homeFrame, text="Username", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=58, y=460, width=300)
        self.regUserEntry = Entry(self.homeFrame)
        self.regUserEntry.place(x=180, y=480, width = 150)

        Label(self.homeFrame, text="Password", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=55, y=500, width=300)
        self.regPassEntry = Entry(self.homeFrame, show="*")
        self.regPassEntry.place(x=180, y=520, width = 150)

        Label(self.homeFrame, text="Re-type Password", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=77, y=540, width=300)
        self.regPass2Entry = Entry(self.homeFrame, show="*")
        self.regPass2Entry.place(x=180, y=560, width = 150)

        # REGISTER BUTTON
        Button(self.homeFrame, text="Register", bg=buttonColor, fg=buttonFontColor, font=("Calibri 10"), relief = FLAT,
                command=self.regValidation).place(x=180, y=590, width=150)

        # ALERT LABEL
        Label(self.homeFrame, textvariable=self.regAlert, bg=mainColor, fg="red", font = ("Calibri 9")).place(x=0, y=620, width=500)

        # TO LOGIN SCREEN
        Label(self.homeFrame, text="Already have an account?", bg=mainColor, fg=labelFontColor, font =("Calibri 9")).place(x=122, y=650, width=200)
        Button(self.homeFrame, text="Click here", bg=mainColor, fg=titleFontColor, font = ("Calibri 9"), relief=FLAT,
                command=lambda: controller.show_frame("LoginScreen")).place(x=300, y=648, width=55)

    def homeFrame(self):
        self.homeFrame = Frame(self)
        self.homeFrame.place(x=250, y=0, width=500, height=700)
        self.homeFrame.configure(bg=mainColor)

    def regValidation(self):
        self.db = UserDb()
        data = (self.regUserEntry.get(), self.regPassEntry.get())
        if self.regUserEntry.get() == "":
                self.regAlert.set("Enter Username First.")

        elif self.regPassEntry.get() == "":
                self.regAlert.set("Enter Password First.")
                
        elif self.regPass2Entry.get() == "":
                self.regAlert.set("Enter Password First.")

        elif len(self.regUserEntry.get()) < 6:
                self.regAlert.set("Invalid Username. Minimum of 6 character.s")

        elif len(self.regPassEntry.get()) < 6:
                self.regAlert.set("Invalid Password. Minimum of 6 characters.")      

        elif self.regUserEntry.get().isalnum():     
                if(self.regPassEntry.get() == self.regPass2Entry.get()):  
                    test = self.db.userRegistration(data, self.regUserEntry.get())
                    if not test:
                            self.controller.show_frame("LoginScreen")
                    else:
                            self.regAlert.set("Username already exist.")
                else:
                    self.regAlert.set("Password do not match.")
        else:
                self.regAlert.set("Invalid username. Use alphanumeric only.")

class HomeScreen(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                self.controller = controller
                self.imagesUsed()
                self.homeFrame()
                self.headerFrame()
                self.menuFrame()
                self.newTask = TaskScreen(self, controller)
                
                self.display = TaskScreen(self, controller)
                self.display.displaytask()


                datetoday = StringVar()
                datetoday.set(mixed)

                self.todaySchedule = Frame(self.homeFrame)
                self.todaySchedule.place(x=160, y=160)
                self.todaySchedule.configure(bg=homeColor)

                self.todayTask = Frame(self.homeFrame)
                self.todayTask.place(x=620, y=160)
                self.todayTask.configure(bg=homeColor)

                self.displayTodaySubject()
                self.displayTodayTask()

                Label(self.headerFrame, text="Today", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
                self.DayToday = Label(self.headerFrame, textvariable=datetoday, bg=headerColor, fg=headerFontColor, font=("Calibri 13")).place(x=170, y=75)
                self.Schedule = Label(self.headerFrame, text="Classes Today", fg=headerFontColor, bg=headerColor, font=("Calibri 13 bold")).place(x=170, y=120)

                Label(self.headerFrame, text="Tasks", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=625, y=40)
                self.createTaskButton = Button(self.headerFrame, text="New Task +", bg=buttonColor, fg=buttonFontColor, font=("Calibri 12"),
                command=self.newTask.newTask).place(x=625, y=80, width=90, height=30)
                self.Schedule = Label(self.headerFrame, text="Due Date Today", fg=headerFontColor, bg=headerColor, font=("Calibri 13 bold")).place(x=625, y=120)

        def displayTodaySubject(self):
                self.displayToday = Home()
                x = self.displayToday.getTodaySubject(studID, date.strftime("%A"))
                self.subjectToday = []
                data = []
                for row in x:
                        data.append(row)

                self.SubjectID = []
                self.StudentID = []
                self.SubjectName = []
                self.Start_Time = []
                self.End_Time = []
                self.Day_Schedule = []
                self.Description = []
                i = 0
                for d in data:
                        self.SubjectID.append(d[0])
                        self.StudentID.append(d[1])
                        self.SubjectName.append(d[2])
                        self.Start_Time.append(d[3])
                        self.End_Time.append(d[4])
                        self.Day_Schedule.append(d[5])
                        self.Description.append(d[6])

                column = 1
                row = 0
                btn = []
                ext = []

                for i in range(0, len(x), 1):
                        if row == 5:
                                column += 1
                                row = 0
                        if row < 5:
                                self.todayScheduleFrame = Frame(self.todaySchedule, relief=RAISED, borderwidth=5)
                                self.todayScheduleFrame.grid(row=row, column=column, padx=10, pady=10)
                                self.todayScheduleFrame.configure(width=400, height=85, bg=mainColor)
                                
                                Label(self.todayScheduleFrame, text=("Subject: " + self.SubjectName[i]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=5, width=385)
                                Label(self.todayScheduleFrame, text=("Day: " + self.Day_Schedule[i]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=25, width=385)
                                btn.append(Button(self.todayScheduleFrame, command=lambda c=i: self.viewSubject(c), text="View", bg=buttonColor, fg=buttonFontColor))
                                btn[i].place(x=175, y=45, width=50)
                                
                                row += 1

        def deleteSubject(self, x):
                self.delete = Subject()
                self.details.destroy()
                self.controller.destroy()
                initID("HomeScreen")

        def viewSubject(self, x):
                self.details = Tk()
                self.details.title("Details")
                self.details.geometry("+600+200")
                self.details.config(bg=homeColor)

                Label(self.details, text="Subject:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.SubjectUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.SubjectUpdate.insert(END, self.SubjectName[x])
                self.SubjectUpdate.pack(anchor=W)
                Label(self.details, text="Start Time:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.StartUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.StartUpdate.insert(END, self.Start_Time[x])
                self.StartUpdate.pack(anchor=W)
                Label(self.details, text="End Time:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.EndUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.EndUpdate.insert(END, self.End_Time[x])
                self.EndUpdate.pack(anchor=W)
                Label(self.details, text = "Description:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.DescriptionUpdate = ScrolledText(self.details, font=("Cambria 10"), width=50, height=10)
                self.DescriptionUpdate.insert(END, self.Description[x])
                self.DescriptionUpdate.pack(anchor=W)
                Label(self.details, text = "Day of Subject:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.DayUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.DayUpdate.insert(END, self.Day_Schedule[x])
                self.DayUpdate.pack(anchor=W)

                Label(self.details, text="", bg=homeColor, font = ("Calibri 2")).pack()
                Button(self.details, command= lambda: self.updateSubject(self.SubjectID[x]), text="Update", bg="navy", fg=buttonFontColor).pack(side=RIGHT)
                Button(self.details, command=lambda: self.deleteSubject(self.SubjectID[x]), text="Delete", bg="maroon", fg=buttonFontColor).pack(side=LEFT)
                
                self.details.mainloop()

        def updateSubject(self, SubjectID):
                data = (self.SubjectUpdate.get(), self.StartUpdate.get(), self.EndUpdate.get(), self.DescriptionUpdate.get(('1.0', END)), self.DayUpdate.get(), SubjectID)
                self.update = Subject()
                self.update.updateSubject(data)
                self.details.destroy()
                self.controller.destroy()
                initID("SubjectScreen")

        def displayTodayTask(self):
                self.displayTask = Home()
                x = self.displayTask.getTodayTask(studID, str(date.strftime("%Y")) + "-" + str(date.strftime("%m")) + "-" + str(date.strftime("%d")))
                self.ReminderID = []
                self.StudentID = []
                self.ReminderTypeID = []
                self.Title = []
                self.Due_Date = []
                self.Details = []
                self.Subject = []
                data = []
                for row in x:
                        data.append(row)


                for d in data:
                        self.ReminderID.append(d[0])
                        self.StudentID.append(d[1])
                        self.ReminderTypeID.append(d[2])
                        self.Title.append(d[3])
                        self.Due_Date.append(d[4])
                        self.Details.append(d[5])
                        self.Subject.append(d[6])
                column = 1
                row = 0
                btn = []
                ext = []
                

                for i in range(0, len(x), 1):
                        if row == 4:
                                column += 1
                                row = 0
                        if row < 4:
                                self.todayTaskSchedule = Frame(self.todayTask, relief=RAISED, borderwidth=5)
                                self.todayTaskSchedule.grid(row=row, column=column, padx=10, pady=10)
                                self.todayTaskSchedule.configure(width=150, height=110, bg=mainColor)
                                
                                self.rem = TaskOptionMenu()
                                self.remindertype = self.rem.getReminder(self.ReminderTypeID[i])

                                Label(self.todayTaskSchedule, text=("Title: " + self.Title[i]), font =("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=7, y=5, width=130)
                                Label(self.todayTaskSchedule, text=("Type: " + self.remindertype[0]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=7, y=25, width=130)
                                Label(self.todayTaskSchedule, text=("Due Date: " + str(self.Due_Date[i])), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=45, width=130)
                                btn.append(Button(self.todayTaskSchedule, command=lambda c=i: self.viewTask(c), text="View", bg=buttonColor, fg=buttonFontColor))
                                btn[i].place(x=50, y=65, width=50)
                                row += 1

        def viewTask(self, x):
                self.details = Tk()
                self.details.title("Details")
                self.details.geometry("+600+200")
                self.details.config(bg=homeColor)

                Label(self.details, text="Title:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.titleUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.titleUpdate.insert(END, str(self.Title[x]))
                self.titleUpdate.pack(anchor=W)
                Label(self.details, text="Subject:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.subjectUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.subjectUpdate.insert(END, self.Subject[x])
                self.subjectUpdate.pack(anchor=W)
                Label(self.details, text = "Details:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.detailUpdate = ScrolledText(self.details, font=("Cambria 10"), width=50, height=10)
                self.detailUpdate.insert(END, self.Details[x])
                self.detailUpdate.pack(anchor=W)
                Label(self.details, text = "Due Date:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.dueDateUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.dueDateUpdate.insert(END, self.Due_Date[x])
                self.dueDateUpdate.pack(anchor=W)

                Label(self.details, text="", bg=homeColor, font = ("Calibri 2")).pack()
                Button(self.details, command= lambda: self.updateTask(self.ReminderID[x]), text="Update", bg="navy", fg=buttonFontColor).pack(side=LEFT)
                Button(self.details, command= lambda: self.deleteTask(self.ReminderID[x]), text="Delete", bg="maroon", fg=buttonFontColor).pack(side=RIGHT)
                
                self.details.mainloop()

        def updateTask(self, taskID):
                data = (self.titleUpdate.get(), self.subjectUpdate.get(), self.detailUpdate.get("1.0", END), self.dueDateUpdate.get(), taskID)
                self.update = Task()
                self.update.updateTask(data)
                self.details.destroy()
                self.controller.destroy()
                initID("HomeScreen")

        def deleteTask(self, x):
                self.delete = Task()
                self.delete.deleteTask(x)
                self.details.destroy()
                self.controller.destroy()
                initID("HomeScreen")

        def homeFrame(self):
                self.homeFrame = Frame(self)
                self.homeFrame.place(x=0, y=0, width=1000, height=700)
                self.homeFrame.configure(bg=homeColor)

        def headerFrame(self):
                self.headerFrame = Frame(self)
                self.headerFrame.place(x=0, y=0, width=1000, height=150)
                self.headerFrame.configure(bg=headerColor)

        def menuFrame(self):
                self.menuFrame = Frame(self)
                self.menuFrame.place(x=0, y=0, width = 150, height = 700)
                self.menuFrame.configure(bg=menuColor)

                Label(self.menuFrame, image=self.menuLogo, bg = menuColor).place(x=0, y=0, width=150, height=150)
                Button(self.menuFrame, image=self.menuHome, bg = menuColor, relief = FLAT,
                        command=lambda: self.controller.show_frame("HomeScreen")).place(x=0, y=150, width=150)
                Button(self.menuFrame, image=self.menuTask, bg = menuColor, relief = FLAT,
                        command=lambda: self.controller.show_frame("TaskScreen")).place(x=0, y=190, width=150)
                Button(self.menuFrame, image=self.menuSubject, bg = menuColor, relief = FLAT, 
                        command=lambda: self.controller.show_frame("ScheduleScreen")).place(x=0, y=230, width=150)
                Button(self.menuFrame, image=self.menuProgress, bg = menuColor, relief = FLAT,
                        command=lambda: self.controller.show_frame("ProgressScreen")).place(x=0, y=270, width=150)
                Button(self.menuFrame, image=self.menuSettings, bg = menuColor, relief = FLAT,
                        command=lambda: self.controller.show_frame("LoginScreen")).place(x=0, y=650, width=150)

        def imagesUsed(self):
                self.menuLogo = PhotoImage(file="images\menulogo.png")
                self.menuHome = PhotoImage(file="images\menuhome.png")
                self.menuTask = PhotoImage(file="images\menutask.png")
                self.menuSubject = PhotoImage(file="images\menusubject.png")
                self.menuProgress = PhotoImage(file="images\menuprogress.png")
                self.menuSettings = PhotoImage(file="images\menusettings.png")

class TaskScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.defaultFrame = HomeScreen.imagesUsed(self)
        self.defaultFrame = HomeScreen.homeFrame(self)
        self.defaultFrame = HomeScreen.headerFrame(self)
        self.defaultFrame = HomeScreen.menuFrame(self)

        self.taskScreenFrame = Frame(self)
        self.taskScreenFrame.place(x=170, y=170)
        self.taskScreenFrame.configure(bg=homeColor)
        
        self.displaytask()    

        Label(self.headerFrame, text="Tasks", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
        self.createTaskButton = Button(self.headerFrame, text="New Task +", bg=buttonColor, fg=buttonFontColor, font=("Calibri 12"),
                command=self.newTask).place(x=170       , y=80, width=90, height=30)
        self.Schedule = Label(self.headerFrame, text="List of tasks", fg=headerFontColor, bg=headerColor, font=("Calibri 13 bold")).place(x=170, y=120)
        
    def displaytask(self):
        self.display = DisplayData()
        x = self.display.displayTask(studID)
        data = []
        for row in x:
                data.append(row)

        self.TaskID = []
        self.StudentID = []
        self.ReminderTypeID = []
        self.Title = []
        self.Date = []
        self.Detail = []
        self.Subject = []
        i = 0
        for d in data:
                self.TaskID.append(d[0])
                self.StudentID.append(d[1])
                self.ReminderTypeID.append(d[2])
                self.Title.append(d[3])
                self.Date.append(d[4])
                self.Detail.append(d[5])
                self.Subject.append(d[6])

        column = 1
        row = 0
        btn = []
        ext = []


        for i in range(0, len(x), 1):
                if row == 5:
                        column += 1
                        row = 0
                if row < 5:
                        self.listFrame = Frame(self.taskScreenFrame, relief=RAISED, borderwidth=5)
                        self.listFrame.grid(row=row, column=column, padx=10, pady=10)
                        self.listFrame.configure(width=250, height=110, bg=mainColor)

                        self.rem = TaskOptionMenu()
                        self.remindertype = self.rem.getReminder(self.ReminderTypeID[i])

                        Label(self.listFrame, text=("Title: " + self.Title[i]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=7, y=5, width=230)
                        Label(self.listFrame, text=("Type: " + self.remindertype[0]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=7, y=25, width=230)
                        Label(self.listFrame, text=("Due Date: " + str(self.Date[i])), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=45, width=230)
                        btn.append(Button(self.listFrame, command=lambda c=i: self.viewTask(c), text="View", bg=buttonColor, fg=buttonFontColor))
                        btn[i].place(x=100, y=65, width=50)
                        
                        row += 1

    def deleteTask(self, x):
                self.delete = Task()
                self.delete.deleteTask(x)
                self.details.destroy()
                self.controller.destroy()
                initID("TaskScreen")

    def viewTask(self, x):
                self.details = Tk()
                self.details.title("Details")
                self.details.geometry("+600+200")
                self.details.config(bg=homeColor)

                Label(self.details, text="Title:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.titleUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.titleUpdate.insert(END, str(self.Title[x]))
                self.titleUpdate.pack(anchor=W)
                Label(self.details, text="Subject:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.subjectUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.subjectUpdate.insert(END, self.Subject[x])
                self.subjectUpdate.pack(anchor=W)
                Label(self.details, text = "Details:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.detailUpdate = ScrolledText(self.details, font=("Cambria 10"), width=50, height=10)
                self.detailUpdate.insert(END, self.Detail[x])
                self.detailUpdate.pack(anchor=W)
                Label(self.details, text = "Due Date:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.dueDateUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.dueDateUpdate.insert(END, self.Date[x])
                self.dueDateUpdate.pack(anchor=W)

                Label(self.details, text="", bg=homeColor, font = ("Calibri 2")).pack()
                Button(self.details, command= lambda: self.updateTask(self.TaskID[x]), text="Update", bg="navy", fg=buttonFontColor).pack(side=LEFT)
                Button(self.details, command= lambda: self.deleteTask(self.TaskID[x]), text="Delete", bg="maroon", fg=buttonFontColor).pack(side=RIGHT)
                
                self.details.mainloop()

    def updateTask(self, taskID):
                data = (self.titleUpdate.get(), self.subjectUpdate.get(), self.detailUpdate.get("1.0", END), self.dueDateUpdate.get(), taskID)
                self.update = Task()
                self.update.updateTask(data)
                self.details.destroy()
                self.controller.destroy()
                initID("TaskScreen")
            
    # New Task Screen
    def newTask(self):
            self.root = Tk()
            self.root.geometry("600x510+500+200")
            self.root.title("Create new task")
            self.root.resizable(width=False, height=False)
            
            self.newTaskFrame = Frame(self.root)
            self.newTaskFrame.place(x=0, y=80, width=600, height=430)
            self.newTaskFrame.configure(bg=homeColor)

            self.newTaskHeader = Frame(self.root)
            self.newTaskHeader.place(x=0, y=0, width=600, height=90)
            self.newTaskHeader.configure(bg=headerColor)

            self.newTaskAlert = StringVar()

            # Content of Header Frame
            Label(self.newTaskHeader, text = "New Task", bg=headerColor, fg=buttonFontColor, font = ("Calibri 24 bold")).place(x=20, y=10)
            Label(self.newTaskHeader, text = str(date.strftime("%Y")), bg = headerColor, fg="white", font=("Calibri 12 bold")).place(x=20, y=45)

            # Content of Middle Frame
            self.db = TaskOptionMenu()
            self.subjVar = StringVar(self.root)
            self.typeVar = StringVar(self.root)
            self.remindertype = ["", ]
            self.gettype = dict(self.db.getType())
            for x in self.gettype.values():
                self.remindertype.append(x)
            
            self.subjects = ["",]
            self.getsubject = (self.db.getSubject(studID))
            for y in self.getsubject:
                self.subjects.append(y[0])
   
            # Subject OptionMenu (Dropdown)
            Label(self.newTaskFrame, text = "Subject", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=20, y=20)
            self.Subject = OptionMenu(self.newTaskFrame, self.subjVar, *self.subjects)
            self.Subject["highlightthickness"]=0
            self.Subject.place(x=25, y=45)
            
            # Due Date
            Label(self.newTaskFrame, text = "Due Date", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=20, y=80)
            self.DueDate = DateEntry(self.newTaskFrame, date_pattern = "y-mm-dd", foreground = labelDarkFontColor, background = "steel blue")
            self.DueDate.place(x=25, y=105, height = 25)

            # Type OptionMenu (Dropdown)
            Label(self.newTaskFrame, text = "Type", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=340, y=80)
            self.Type = OptionMenu(self.newTaskFrame, self.typeVar, *self.remindertype)
            self.Type["highlightthickness"]=0
            self.Type.place(x=345, y=105)
            self.newTypeButton = Button(self.newTaskFrame, command = self.newType, text = "+", bg=buttonColor, fg=buttonFontColor).place(x=370, y=83, width=18, height=18)

            # Title (Entry)
            Label(self.newTaskFrame, text = "Title", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=20, y=140)
            self.Title = Entry(self.newTaskFrame, font = ("Calibri 10"))
            self.Title.place(x=25, y=165, width = 415, height = 28)
            
            # Details (Entry)
            Label(self.newTaskFrame, text = "Detail", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=20, y=200)
            self.Details = ScrolledText(self.newTaskFrame, font = ("Calibri 10"))
            self.Details.place(x=25, y=225, height = 140, width = 550)

            # Cancel and Save (Button)
            Button(self.newTaskFrame, command = self.cancel, text = "Cancel", bg = buttonColor, fg = buttonFontColor, font =("Calibri 11")).place(x=25, y=379)
            Button(self.newTaskFrame, command = self.save, text = "Save", width = 5, bg = buttonColor, fg = buttonFontColor, font =("Calibri 11")).place(x=525, y=379)

            # Alert Message 
            Label(self.newTaskFrame, textvariable=self.newTaskAlert, bg=homeColor, fg="red", font = ("Calibri 9")).place(x=300, y=400)
            
    def newType(self):
        self.typewindow = Tk()
        self.typewindow.geometry("300x100+700+300")
        self.typewindow.title("Create reminder type")
        self.typewindow.resizable(width=False, height=False)

        self.newTypeFrame = Frame(self.typewindow)
        self.newTypeFrame.place(x=0, y=0, width=300, height=100)
        
        self.newTypeEntry = StringVar()

        Label(self.newTypeFrame, text="Enter reminder type").place(x=0, y=20, width=300)
        self.newTypeEntry = Entry(self.newTypeFrame)
        self.newTypeEntry.place(x=90, y=40, width=120)
        Btn = Button(self.newTypeFrame, command=self.typeSave, bg=buttonColor, fg=buttonFontColor, text="Save").place(x=115, y=65, width=70)

    def typeSave(self):
            description = self.newTypeEntry.get()
            data = (description, )
            if self.newTypeEntry.get() == "":
                Label(self.newTypeFrame, text="Please fill the blank", fg = "red", font=("Calibri 8")).place(x=0, y=5, width=300)
            else:
                db = UserDb()
                test = db.newType(data)
                if not test:
                        self.root.destroy()
                        self.typewindow.destroy()
                        self.newTask()
                else:
                        Label(self.newTypeFrame, text="Type of reminder already exist", fg = "red", font=("Calibri 8")).place(x=0, y=5, width=300)
                
    # Validation for new Task    
    def save(self):
        self.db = UserDb()
        Subject = self.subjVar.get()
        Type = self.get_key(self.typeVar.get())
        Title = self.Title.get()
        DueDate = self.DueDate.get()
        Details = self.Details.get('1.0', END)


        data = (Type, Title, DueDate, Details, studID, Subject,
        )

        if self.DueDate.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.subjVar.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.Title.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.Details.get(('1.0'), END) == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.typeVar.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        else:
                self.db.newTask(data)
                self.root.destroy()
                self.controller.destroy()
                initID("TaskScreen")
    
    def cancel(self):
        self.root.destroy()

    def get_key(self, var): 
        for key, value in self.gettype.items(): 
            if var == value: 
                return key 
  
        return "key doesn't exist"

class ScheduleScreen(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            self.defaultFrame = HomeScreen.imagesUsed(self)
            self.defaultFrame = HomeScreen.homeFrame(self)
            self.defaultFrame = HomeScreen.headerFrame(self)
            self.defaultFrame = HomeScreen.menuFrame(self)

            self.scheduleScreenFrame = Frame(self)
            self.scheduleScreenFrame.place(x=150, y=150)
            self.scheduleScreenFrame.configure(bg=homeColor)
            
            self.displaySubject()

            Label(self.headerFrame, text="Schedule", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
            Label(self.headerFrame, text = lastyear + "-" + (str(date.strftime("%Y"))), bg = headerColor, fg="white", font=("Calibri 13")).place(x=170, y=75)

            Label(self.headerFrame, text="Manage Subject", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=620, y=40)
            self.createTaskButton = Button(self.headerFrame, text="New Subject +", bg=buttonColor, fg=buttonFontColor, font=("Calibri 12"),
            command=self.newSubject).place(x=620, y=80, width=120, height=30)

        def displaySubject(self):
                self.subjectDb = Subject()
                x = self.subjectDb.displaySubject(studID)
                data = []
                for row in x:
                        data.append(row)

                self.SubjectID = []
                self.StudentID = []
                self.SubjectName = []
                self.Start_Time = []
                self.End_Time = []
                self.Day_Schedule = []
                self.Description = []
                i = 0
                for d in data:
                        self.SubjectID.append(d[0])
                        self.StudentID.append(d[1])
                        self.SubjectName.append(d[2])
                        self.Start_Time.append(d[3])
                        self.End_Time.append(d[4])
                        self.Day_Schedule.append(d[5])
                        self.Description.append(d[6])

                column = 1
                row = 0
                btn = []
                ext = []

                for i in range(0, len(x), 1):
                        if row == 5:
                                column += 1
                                row = 0
                        if row < 5:
                                self.subjFrame = Frame(self.scheduleScreenFrame, relief=RAISED, borderwidth=5)
                                self.subjFrame.grid(row=row, column=column, padx=10, pady=10)
                                self.subjFrame.configure(width=400, height=85, bg=mainColor)
                                
                                Label(self.subjFrame, text=("Subject: " + self.SubjectName[i]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=5, width=385)
                                Label(self.subjFrame, text=("Day: " + self.Day_Schedule[i]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=25, width=385)
                                btn.append(Button(self.subjFrame, command=lambda c=i: self.viewSubject(c), text="View", bg=buttonColor, fg=buttonFontColor))
                                btn[i].place(x=175, y=45, width=50)
                                row += 1

        def deleteSubject(self, x):
                self.delete = Subject()
                self.delete.deleteSubject(x)
                self.details.destroy()
                self.controller.destroy()
                initID("ScheduleScreen")

        def viewSubject(self, x):
                self.details = Tk()
                self.details.title("Details")
                self.details.geometry("+600+200")
                self.details.config(bg=homeColor)

                Label(self.details, text="Subject:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.SubjectUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.SubjectUpdate.insert(END, self.SubjectName[x])
                self.SubjectUpdate.pack(anchor=W)
                Label(self.details, text="Start Time:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.StartUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.StartUpdate.insert(END, self.Start_Time[x])
                self.StartUpdate.pack(anchor=W)
                Label(self.details, text="End Time:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.EndUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.EndUpdate.insert(END, self.End_Time[x])
                self.EndUpdate.pack(anchor=W)
                Label(self.details, text = "Description:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.DescriptionUpdate = ScrolledText(self.details, font=("Cambria 10"), width=50, height=10)
                self.DescriptionUpdate.insert(END, self.Description[x])
                self.DescriptionUpdate.pack(anchor=W)
                Label(self.details, text = "Day of Subject:", font = ("Cambria 12 bold"), bg=homeColor).pack(anchor=W)
                self.DayUpdate = Entry(self.details, font=("Cambria 10"), width=50)
                self.DayUpdate.insert(END, self.Day_Schedule[x])
                self.DayUpdate.pack(anchor=W)

                Label(self.details, text="", bg=homeColor, font = ("Calibri 2")).pack()
                Button(self.details, command= lambda: self.updateSubject(self.SubjectID[x]), text="Update", bg="navy", fg=buttonFontColor).pack(side=LEFT)
                Button(self.details, command=lambda: self.deleteSubject(self.SubjectID[x]), text="Delete", bg="maroon", fg=buttonFontColor).pack(side=RIGHT)
                
                self.details.mainloop()

        def updateSubject(self, SubjectID):
                data = (self.SubjectUpdate.get(), self.StartUpdate.get(), self.EndUpdate.get(), self.DescriptionUpdate.get('1.0', END), self.DayUpdate.get(), SubjectID)
                self.update = Subject()
                self.update.updateSubject(data)
                self.details.destroy()
                self.controller.destroy()
                initID("ScheduleScreen")


        def newSubject(self):
            self.root = Tk()
            self.root.geometry("600x510+500+200")
            self.root.title("Create new subject")
            
            self.newSubjectFrame = Frame(self.root)
            self.newSubjectFrame.place(x=0, y=80, width=600, height=430)
            self.newSubjectFrame.configure(bg=homeColor)

            self.newSubjectHeader = Frame(self.root)
            self.newSubjectHeader.place(x=0, y=0, width=600, height=90)
            self.newSubjectHeader.configure(bg=headerColor)

            self.newSubjectAlert = StringVar(self.root)
            self.day = StringVar(self.root)
            self.subjectInfoEntries()

            # Content of Header Frame
            Label(self.newSubjectHeader, text = "New Subject", bg=headerColor, fg=buttonFontColor, font = ("Calibri 24 bold")).place(x=20, y=20)

            # Content of Middle Frame
            self.subjVar = StringVar(self.root)
            self.typeVar = StringVar(self.root)

            Label(self.newSubjectFrame, text= "Please fill all the blanks", bg = homeColor, fg = labelDarkFontColor, font =("Calibri 11")).place(x=24, y=20)
            
            # SubjectName (Entry)
            Label(self.newSubjectFrame, text = "Subject Name", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=25, y=55)
            self.SubjectName = Entry(self.newSubjectFrame, font = ("Calibri 10"))
            self.SubjectName.place(x=25, y=80, width = 415, height = 28)

            Label(self.newSubjectFrame, text="Day", bg=homeColor, fg=labelDarkFontColor, font= ("Calibri 10")).place(x=25, y=190)
            self.selectDay = OptionMenu(self.newSubjectFrame, self.day, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
            self.selectDay["highlightthickness"]=0
            self.selectDay.place(x=27, y=215)

            Label(self.newSubjectFrame, text="Details", bg=homeColor, fg=labelDarkFontColor, font = ("Calibri 10")).place(x=24, y=260)
            self.Details = ScrolledText(self.newSubjectFrame, font = ("Calibri 10"))
            self.Details.place(x=27, y=285, height = 70, width = 550)

            # Cancel and Save (Button)
            Button(self.newSubjectFrame, text = "Cancel", bg = buttonColor, fg = buttonFontColor, font =("Calibri 11")).place(x=25, y=379)
            Button(self.newSubjectFrame, command = self.save, text = "Save", width = 5, bg = buttonColor, fg = buttonFontColor, font =("Calibri 11")).place(x=525, y=379)

        def subjectInfoEntries(self):
                Label(self.newSubjectFrame, text="Start Time", bg=homeColor, fg=labelDarkFontColor, font =("Calibri 10")).place(x=25, y=125)
                self.starthour = Spinbox(self.newSubjectFrame, values=("12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
                self.starthour.place(x=25, y=150, width=35)
                self.startminute = Spinbox(self.newSubjectFrame, values=("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"
                ))
                self.startminute.place(x=65, y=150, width=35)
                self.startday = Spinbox(self.newSubjectFrame, values=("am", "pm"))
                self.startday.place(x=105, y=150, width=40)

                Label(self.newSubjectFrame, text="End Time", bg=homeColor, fg=labelDarkFontColor, font =("Calibri 10")).place(x=275, y=125)
                self.endhour = Spinbox(self.newSubjectFrame, values=("12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
                self.endhour.place(x=275, y=150, width=35)
                self.endminute = Spinbox(self.newSubjectFrame, values=("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                "51", "52", "53", "54", "55", "56", "57", "58", "59", "60"
                ))
                self.endminute.place(x=315, y=150, width=35)
                self.endday = Spinbox(self.newSubjectFrame, values=("pm", "am"))
                self.endday.place(x=355, y=150, width=40)

        def save(self):
                if self.SubjectName.get() == "" or self.day.get() == "":
                        Label(self.newSubjectFrame, text="Please fill all the blanks", bg=homeColor, fg="red", font=("Calibri 10")).place(x=200, y=400, width=200)
                elif self.day.get() == "" or self.Details.get('1.0', END) == "":
                        Label(self.newSubjectFrame, text="Please fill all the blanks", bg=homeColor, fg="red", font=("Calibri 10")).place(x=200, y=400, width=200)
                else:
                        data = self.validation()
                        self.db = Subject()
                        self.db.newSubject(data)
                        self.root.destroy()
                        self.controller.destroy()
                        initID("ScheduleScreen")

        def validation(self):
                Subject = self.SubjectName.get()
                Day = self.day.get()
                Details = self.Details.get('1.0', END)

                if self.startday.get() == "pm" and self.starthour.get() != "12":
                        starthour = int(self.starthour.get()) + 12
                        self.startTime = str(starthour) + ":" + self.startminute.get() + ":00"
                else:
                        self.startTime = self.starthour.get() + ":" + self.startminute.get() + ":00"

                if self.endday.get() == "pm" and self.endhour.get() != "12":
                        endhour = int(self.endhour.get()) + 12
                        self.endTime = str(endhour) + ":" + self.endminute.get() + ":00"
                else:
                        self.endTime = self.endhour.get() + ":" + self.endminute.get() + ":00"

                data = (Subject, Day, Details, self.startTime, self.endTime, studID)

                return data
               
class ProgressScreen(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                self.controller = controller
                self.defaultFrame = HomeScreen.imagesUsed(self)
                self.defaultFrame = HomeScreen.homeFrame(self)
                self.defaultFrame = HomeScreen.headerFrame(self)
                self.defaultFrame = HomeScreen.menuFrame(self)

                self.scheduleScreenFrame = Frame(self)
                self.scheduleScreenFrame.place(x=150, y=150)
                self.scheduleScreenFrame.configure(bg=homeColor)

                self.displaySubject()

                Label(self.headerFrame, text="Schedule", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
                Label(self.headerFrame, text = lastyear + "-" + (str(date.strftime("%Y"))), bg = headerColor, fg="white", font=("Calibri 13")).place(x=170, y=75)

                Label(self.headerFrame, text="Manage Subject", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=620, y=40)


        def displaySubject(self):
                self.subjectDb = Subject()
                x = self.subjectDb.displaySubject(studID)
                data = []
                for row in x:
                        data.append(row)

                self.SubjectID = []
                self.StudentID = []
                self.SubjectName = []
                self.Start_Time = []
                self.End_Time = []
                self.Day_Schedule = []
                self.Description = []
                i = 0
                for d in data:
                        self.SubjectID.append(d[0])
                        self.StudentID.append(d[1])
                        self.SubjectName.append(d[2])
                        self.Start_Time.append(d[3])
                        self.End_Time.append(d[4])
                        self.Day_Schedule.append(d[5])
                        self.Description.append(d[6])

                column = 1
                row = 0
                btn = []
                ext = []

                for i in range(0, len(x), 1):
                        if row == 6:
                                column += 1
                                row = 0
                        if row < 6:
                                self.subjFrame = Frame(self.scheduleScreenFrame, relief=RAISED, borderwidth=5)
                                self.subjFrame.grid(row=row, column=column, padx=10, pady=10)
                                self.subjFrame.configure(width=400, height=65, bg=mainColor)
                                
                                Label(self.subjFrame, text=("Subject: " + self.SubjectName[i]), font=("Calibri 10"), fg=labelFontColor, bg=mainColor).place(x=5, y=5, width=385)
                                btn.append(Button(self.subjFrame, 
                                command=lambda c=i: self.manageGradingSystem(self.SubjectID[c]), 
                                text="Manage Subject Progress", bg=buttonColor, fg=buttonFontColor))
                                btn[i].place(x=100, y=25, width=200)
                                row += 1

        def manageGradingSystem(self, subjectID):
                self.gScreen = Tk()
                self.gScreen.geometry("300x120+680+250")
                self.gScreen.title("Manage Subject Progress")
                self.gScreen.config(bg=homeColor)

                self.acadOption = ["Standard", "Custom"]
                self.acadTypeVar = StringVar(self.gScreen)

                Label(self.gScreen, text="SELECT GRADING SYSTEM", bg=homeColor, font=("Calibri 16 bold")).pack(anchor=CENTER, pady=10)
                self.academicType = OptionMenu(self.gScreen, self.acadTypeVar, *self.acadOption)
                self.academicType["highlightthickness"]=0
                self.academicType.pack(anchor=CENTER, pady=0)
                Button(self.gScreen, command=lambda: self.gradingSystem(subjectID), text="Ok", bg=buttonColor, fg=buttonFontColor).pack(anchor=CENTER, pady=10)
        
        def gradingSystem(self, subjectID):
                acadType = self.acadTypeVar.get()

                if acadType == "Standard":
                        self.gScreen.destroy()
                        self.newStandardScreen(subjectID)

                elif acadType == "Custom":
                        self.gScreen.destroy()
                        self.newCustomScreen(subjectID)

        def newStandardScreen(self, subjectID):
                self.sScreen = Tk()
                self.sScreen.geometry("700x600+450+120")
                self.sScreen.title("Standard Grading System")
                self.sScreen.config(bg=homeColor)


                self.sScreenTopFrame = Frame(self.sScreen)
                self.sScreenTopFrame.place(x=0, y=0, width=700, height=100)

                self.sScreenEntryFrame = Frame(self.sScreen)
                self.sScreenEntryFrame.place(x=100, y=150, width=500, height=400)

                self.dataGs = Frame(self.sScreenEntryFrame)
                self.dataGs.place(x=170, y=80, width=180)

                
                self.gradingSystem = Progress()
                # VALIDATION 
                self.createValidation(subjectID)

                Label(self.sScreenTopFrame, text="Create your grading system for this subject", bg=homeColor, font=("Calibri 20 bold")).pack(pady=30)
                Label(self.sScreenEntryFrame, text="", height=2).grid(row=0)

                Label(self.sScreenEntryFrame, text="Type", font=("Calibri 12")).grid(row=0, column=0, padx=20)
                self.entry1 = Entry(self.sScreenEntryFrame, font=("Calibri 12"))
                self.entry1.grid(row=0, column=1)
                Label(self.sScreenEntryFrame, text="Percentage", font=("Calibri 12")).grid(row=0, column=2, padx=20)
                self.percentage1 = Entry(self.sScreenEntryFrame, width=5, font=("Calibri 12"))
                self.percentage1.grid(row=0, column=3)
                Label(self.sScreenEntryFrame, text="%", font=("Calibri 12")).grid(row=0, column=4)
                Button(self.sScreenEntryFrame, text="Add", bg=buttonColor, fg=buttonFontColor, font = ("Calibri 10")).grid(row=0, column=5, padx=20)

                self.displayGsList = self.gradingSystem.displayGs(subjectID)
                data = []
                for row in self.displayGsList:
                        data.append(row)

                self.GradingSystemID = []
                self.Type = []
                self.Percentage = []

                i = 0
                for d in data:
                        self.GradingSystemID.append(d[0])
                        self.Type.append(d[1])
                        self.Percentage.append(d[2])


                btn = []
                for i in range(0, len(self.displayGsList), 1):
                        Label(self.dataGs, text=(self.Type[i])).grid(row=i, column=0)
                        Label(self.dataGs, text=str(self.Percentage[i]) + "%").grid(row=i, column=1)
                        btn.append(Button(self.dataGs, command=lambda c=i: self.deleteGs(self.GradingSystemID[c], subjectID), text="Delete", bg="red", fg=buttonFontColor))
                        btn[i].grid(row=i, column=2)


        def deleteGs(self, GradingSystemID, subjectID):
                self.gradingSystem.deleteGs(GradingSystemID)
                self.sScreen.destroy()
                self.newStandardScreen(subjectID)
               
        def createValidation(self, subjectID):
                percentage = self.gradingSystem.gsValidation(subjectID)
                sum = 0
                for numbers in percentage:
                        sum += numbers[0]

                if sum >= 100:
                        print('asd')
                else:
                        data = [(subjectID, "Assignment", "10"),
                                (subjectID, "Attendance", "10"),
                                (subjectID, "Recitation", "10"),
                                (subjectID, "Quiz", "20"),
                                (subjectID, "Project", "25"),
                                (subjectID, "Exam", "25")]

                        self.gradingSystem.insertStandard(data)

                
        def newCustomScreen(self):
                self.cScreen = Tk()
                self.cScreen.geometry("700x600+450+120")
                self.cScreen.title("Custom Grading System")
                self.cScreen.config(bg=homeColor)


if __name__ == "__main__":
    app = App()
    app.show_frame("LoginScreen")
    app.mainloop()
