from tkinter import *

mainColor = "#222831"
secondaryColor = "#00adb5"
buttonColor = "#00adb5"

labelFontColor = "#eeeeee"
titleFontColor = "#30e3ca"
buttonFontColor = "#ffffff"


def defaultReso(parent):
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
        for F in (LoginScreen, RegistrationScreen, HomeScreen):
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
        
        # Logo
        logo = PhotoImage(file = "images\logo.png")
        Logo = Label(self.homeFrame, image=logo, bg=mainColor, fg=labelFontColor)
        Logo.image = logo
        Logo.place(x=0, y=90, width=500)

        # ACCOUNT LOGIN LABEL
        Label(self.homeFrame, text="Account Login", bg=mainColor, fg=buttonFontColor, font=("Calibri 15 bold")).place(x=0, y=420, width=500)

        # USERNAME AND PASSWORD ENTRIES
        Label(self.homeFrame, text="Username", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=58, y=460, width=300)
        userLoginEntry = Entry(self.homeFrame).place(x=180, y=480, width = 150)
        Label(self.homeFrame, text="Password", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=55, y=500, width=300)
        passLoginEntry = Entry(self.homeFrame, show="*").place(x=180, y=520, width = 150)

        # LOGIN BUTTON
        Button(self.homeFrame, text="Login", bg=buttonColor, fg=buttonFontColor, font=("Calibri 10"), relief = FLAT,
                command=lambda: controller.show_frame("HomeScreen")).place(x=180, y=550, width=150)

        # TO REGISTRATION SCREEN
        Label(self.homeFrame, text="Don't have an account yet?", bg=mainColor, fg=labelFontColor, font =("Calibri 9")).place(x=122, y=630, width=200)
        Button(self.homeFrame, text="Click here", bg=mainColor, fg=titleFontColor, font = ("Calibri 9"), relief=FLAT,
                command=lambda: controller.show_frame("RegistrationScreen")).place(x=300, y=628, width=55)

    def homeFrame(self):
        self.homeFrame = Frame(self)
        self.homeFrame.place(x=250, y=0, width=500, height=700)
        self.homeFrame.configure(bg=mainColor)

class RegistrationScreen(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.homeFrame()
        
        # Logo
        logo = PhotoImage(file = "images\logo.png")
        Logo = Label(self.homeFrame, image=logo, bg=mainColor, fg=labelFontColor)
        Logo.image = logo
        Logo.place(x=0, y=90, width=500)

        # ACCOUNT LOGIN LABEL
        Label(self.homeFrame, text="Account Registration", bg=mainColor, fg=buttonFontColor, font=("Calibri 15 bold")).place(x=0, y=420, width=500)

        # USERNAME AND PASSWORD ENTRIES
        Label(self.homeFrame, text="Username", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=58, y=460, width=300)
        userLoginEntry = Entry(self.homeFrame).place(x=180, y=480, width = 150)
        Label(self.homeFrame, text="Password", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=55, y=500, width=300)
        passLoginEntry = Entry(self.homeFrame, show="*").place(x=180, y=520, width = 150)
        Label(self.homeFrame, text="Re-type Password", bg=mainColor, fg=labelFontColor, font=("Calibri 9")).place(x=77, y=540, width=300)
        pass2LoginEntry = Entry(self.homeFrame, show="*").place(x=180, y=560, width = 150)

        # REGISTER BUTTON
        Button(self.homeFrame, text="Register", bg=buttonColor, fg=buttonFontColor, font=("Calibri 10"), relief = FLAT,
                ).place(x=180, y=590, width=150)

        # TO LOGIN SCREEN
        Label(self.homeFrame, text="Already have an account?", bg=mainColor, fg=labelFontColor, font =("Calibri 9")).place(x=122, y=630, width=200)
        Button(self.homeFrame, text="Click here", bg=mainColor, fg=titleFontColor, font = ("Calibri 9"), relief=FLAT,
                command=lambda: controller.show_frame("LoginScreen")).place(x=300, y=628, width=55)

    def homeFrame(self):
        self.homeFrame = Frame(self)
        self.homeFrame.place(x=250, y=0, width=500, height=700)
        self.homeFrame.configure(bg=mainColor)

class HomeScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.headerFrame()

    
    def headerFrame(self):
        self.headerFrame = Frame(self)
        self.headerFrame.place(x=0, y=0, width=1000, height=150)
        self.headerFrame.configure(bg=secondaryColor)


if __name__ == "__main__":
    app = App()
    app.mainloop()
