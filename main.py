from tkinter import *
from db.database import *
import datetime as dt
from tkcalendar import DateEntry
from tkinter.scrolledtext import ScrolledText



homeColor = "#79bac1"           # THE HOME SCREEN MAIN COLOR    (LIGHTEST)
headerColor = "#142850"         # THE HEADER FRAME COLOR        (DARKER)
mainColor = "#27496d"           # THE START SCREEN MAIN COLOR   (DARKER)
menuColor = "#21243d"           # THE MENU FRAME COLOR          (DARKEST)       
buttonColor = "#21243d"         # THE BUTTON COLOR              (DARKEST) OR (LIGHTEST)

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

        self.show_frame("LoginScreen")

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
                command=lambda: controller.show_frame("HomeScreen")).place(x=180, y=550, width=150)

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


        datetoday = StringVar()
        datetoday.set(mixed)

        Label(self.headerFrame, text="Today", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
        self.DayToday = Label(self.headerFrame, textvariable=datetoday, bg=headerColor, fg=headerFontColor, font=("Calibri 13")).place(x=170, y=75)

        Label(self.headerFrame, text="Tasks", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=470, y=40)
        self.createTaskButton = Button(self.headerFrame, text="New Task +", bg=buttonColor, fg=buttonFontColor, font=("Calibri 12"),
            command=self.newTask.newTask).place(x=470, y=80, width=90, height=30)
        
        Label(self.headerFrame, text="Exams", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=750, y=40)

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
        Button(self.menuFrame, image=self.menuSettings, bg = menuColor, relief = FLAT).place(x=0, y=650, width=150)

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

            Label(self.headerFrame, text="Tasks", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
            self.createTaskButton = Button(self.headerFrame, text="New Task +", bg=buttonColor, fg=buttonFontColor, font=("Calibri 12"),
                command=self.newTask).place(x=170, y=80, width=90, height=30)

    # New Task Screen
    def newTask(self):
            self.root = Tk()
            self.root.geometry("600x510+500+200")
            self.root.title("Create new task")
            
            
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
            self.subjVar = StringVar(self.root)
            self.typeVar = StringVar(self.root)

            # Subject OptionMenu (Dropdown)
            Label(self.newTaskFrame, text = "Subject", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=20, y=20)
            self.Subject = OptionMenu(self.newTaskFrame, self.subjVar, "Subject1", "Subject2", "Subject3")
            self.Subject["highlightthickness"]=0
            self.Subject.place(x=25, y=45)
            
            # Due Date
            Label(self.newTaskFrame, text = "Due Date", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=20, y=80)
            self.DueDate = DateEntry(self.newTaskFrame, date_pattern = "y-mm-dd", foreground = labelDarkFontColor, background = "steel blue")
            self.DueDate.place(x=25, y=105, height = 25)

            # Type OptionMenu (Dropdown)
            Label(self.newTaskFrame, text = "Type", bg = homeColor, fg = labelDarkFontColor, font = ("Calibri 10")).place(x=340, y=80)
            self.Type = OptionMenu(self.newTaskFrame, self.typeVar, "Assignment", "Exam", "Quiz")
            self.Type["highlightthickness"]=0
            self.Type.place(x=345, y=105)

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
            
    # Validation for new Task    
    def save(self):
        self.db = UserDb()
        Type = self.typeVar.get()
        Title = self.Title.get()
        DueDate = self.DueDate.get()
        Details = self.Details.get('1.0', END)

        data = (Type, Title, DueDate, Details,
        )

        if self.DueDate.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.subjVar.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.Title.get() == "":
                self.newTaskAlert.set("Please fill up the blanks")
        elif self.Details.get(('1.0'), END) == "":
                self.newTaskAlert.set("Please fill up the blanks")
        else:
                self.db.newTask(data)
                self.root.destroy()
    
    def cancel(self):
        self.root.destroy()

class ScheduleScreen(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            self.defaultFrame = HomeScreen.imagesUsed(self)
            self.defaultFrame = HomeScreen.homeFrame(self)
            self.defaultFrame = HomeScreen.headerFrame(self)
            self.defaultFrame = HomeScreen.menuFrame(self)
            
            Label(self.headerFrame, text="Schedule", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=170, y=40)
            Label(self.headerFrame, text = lastyear + "-" + (str(date.strftime("%Y"))), bg = headerColor, fg="white", font=("Calibri 13")).place(x=170, y=75)

            Label(self.headerFrame, text="Manage Subject", bg=headerColor, fg=headerFontColor, font=("Calibri 20 bold")).place(x=620, y=40)
            self.createTaskButton = Button(self.headerFrame, text="New Subject +", bg=buttonColor, fg=buttonFontColor, font=("Calibri 12"),
            command=self.newSubject).place(x=620, y=80, width=120, height=30)

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

            self.newSubjectAlert = StringVar()

            # Content of Header Frame
            Label(self.newSubjectHeader, text = "New Subject", bg=headerColor, fg=buttonFontColor, font = ("Calibri 24 bold")).place(x=20, y=20)

            # Content of Middle Frame
            self.subjVar = StringVar(self.root)
            self.typeVar = StringVar(self.root)

            # Cancel and Save (Button)
            Button(self.newTaskFrame, command = self.cancel, text = "Cancel", bg = buttonColor, fg = buttonFontColor, font =("Calibri 11")).place(x=25, y=379)
            Button(self.newTaskFrame, command = self.save, text = "Save", width = 5, bg = buttonColor, fg = buttonFontColor, font =("Calibri 11")).place(x=525, y=379)

            # Alert Message 
            Label(self.newTaskFrame, textvariable=self.newTaskAlert, bg=homeColor, fg="red", font = ("Calibri 9")).place(x=300, y=400)



          
class ProgressScreen(Frame):
    def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            self.controller = controller
            self.defaultFrame = HomeScreen.imagesUsed(self)
            self.defaultFrame = HomeScreen.homeFrame(self)
            self.defaultFrame = HomeScreen.headerFrame(self)
            self.defaultFrame = HomeScreen.menuFrame(self)



if __name__ == "__main__":
    app = App()
    app.mainloop()
