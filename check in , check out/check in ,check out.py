import tkinter as tk
from tkinter import Message, messagebox
import datetime
from datetime import datetime, timedelta

datetime_object = datetime.now()

class test(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        
        
        self.geometry("400x300")
        self.wm_title("check in , check out")
        
        
        container = tk.Frame(self, height=400,width=600)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (SignIn, Register, mainpage):
            frame = F(container, self)
            
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(SignIn)
    
    def show_frame(self, y):
        frame = self.frames[y]
        frame.tkraise()

    def authorizeUser(self):
        global username
        username = name_entry.get()
        PINNo = pass_entry.get()
        
        global retainUsername
        f = open("Usernames and password.txt","r")
        info = f.read()
        info = info.split()
        if username in info:
            index = info.index(username) + 1
            usr_password = info[index]
            
            if usr_password == PINNo:
                retainUsername = username
                name_entry.delete(0, "end")
                pass_entry.delete(0, "end")
                self.show_frame(mainpage)
                messagebox.showinfo(title="Welcome",message="Welcome, " + username)

            
                    
            else:
                messagebox.showerror(title="error",message="Enter correct password.")
                pass_entry.focus()
                
        else:
            messagebox.showerror(title="error",message="Enter an existing username.")
            name_entry.focus()


class SignIn(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#808080")
        
        

        global name_entry
        global pass_entry
                
    
                

        # sign in label
        label = tk.Label(self, text="Sign In Page",font=('Helvetica', 18, "bold" ))
        label.pack(padx=10, pady=10)
        
        #name label and input
        name_label = tk.Label(self, text = "Username",bg = "#c7d3d4", fg="black")
        name_label.place(x = 40, y = 60)

        name_entry = tk.Entry(self, width = 30)
        name_entry.place(x = 110, y = 60)

        #password label and input
        pass_label = tk.Label(self, text = "Password",bg = "#c7d3d4", fg="black")
        pass_label.place(x = 40, y = 100)

        pass_entry = tk.Entry(self, width = 30)
        pass_entry.place(x = 110, y = 100)

        #submit button
        submit_button = tk.Button(self, text = "Submit", bg = "#c7d3d4", fg="black", command = lambda:controller.authorizeUser())
        submit_button.place(x = 40, y = 150)
        
        
        # register button           
        switch_window_button = tk.Button(self, text="Register instead", command= lambda:controller.show_frame(Register))
        switch_window_button.pack(side="bottom", fill=tk.X)



class Register(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#808080")
        
        global u_name_entry
        global pin_entry
        global open_bal_entry

        # register label
        label = tk.Label(self, text="Register Page",font=('Helvetica', 18, "bold" ))
        label.pack(padx=10, pady=10)
        
        #u_name label and input
        u_name_label = tk.Label(self, text = "Please create a username: ",bg = "#c7d3d4", fg="black")
        u_name_label.place(x = 40, y = 60)

        u_name_entry = tk.Entry(self, width = 30)
        u_name_entry.place(x = 190, y = 60)

        #pin label and input
        pin_label = tk.Label(self, text = "Please create a pin: ",bg = "#c7d3d4", fg="black")
        pin_label.place(x = 40, y = 100)
        
        pin_entry = tk.Entry(self, width = 30)
        pin_entry.place(x = 190, y = 100)
        

        #submit button
        submit_button = tk.Button(self, text = "Submit", command = self.captureData,bg = "#c7d3d4", fg="black")
        submit_button.place(x = 40, y = 170)
        
        # go back button
        switch_window_button = tk.Button(self, text="Go Back", command= lambda:controller.show_frame(SignIn))
        switch_window_button.pack(side="bottom", fill=tk.X)

    def captureData(self):
        username = str(u_name_entry.get())
        PINno = str(pin_entry.get())

        u_name_entry.delete(0, "end")
        pin_entry.delete(0, "end")

        #regexuser = re.search("[A-Za-z0-9] {6,18}", username)
        #regexbalance = re.match("[0-9]", balance)
        #regexpassword = re.match("[0-9]{4,8}", PINno)

        fileobject = open("Usernames and password.txt", "r")
        info = fileobject.read()
        info = info.split()
        fileobject.close()
        if username in info:
            messagebox.showerror(title="error",message="Username already exists.")
            u_name_entry.focus()
        elif username.isalnum() == False or username == "" or len(username) < 6 or len(username) > 18:
            messagebox.showerror(title="error",message="Enter an alphanumeric username, between 6-18 characters.")
            u_name_entry.focus()
        elif PINno.isnumeric() == False or PINno == "" or len(PINno) > 8 or len(PINno) < 4:
            messagebox.showerror(title="error",message="Enter a numeric PIN Number between 4-8 characters.")
            pin_entry.focus()
        
        else:
            fileobject = open ("Usernames and password.txt", "a")
            fileobject.write(username)
            fileobject.write("\n")
            fileobject.write(PINno)
            fileobject.write("\n")
            fileobject.close()
            with open("Check in check out log/" + username + " Check in check out log.txt", "w") as f2:
                f2.close()
            messagebox.showinfo(title="Success",message="Registration successful!.")
        

class mainpage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg= "#808080")
        
        global dep_bal
        global account_bal_label
    
        label = tk.Label(self, text="Welcome" ,font=('Helvetica', 18, "bold" ))
        label.pack(padx=10, pady=10)


        check_in_label = tk.Label(self, text="Click here to check in:", )
        check_in_label.place(x = 40, y = 60)

        check_in_button = tk.Button(self,text="Check in",command=lambda:self.check_in())
        check_in_button.place(x = 190, y = 60)

        check_out_label= tk.Label(self,text="Click here to check out:")
        check_out_label.place(x=40, y= 120)

        check_out_button=tk.Button(self,text="click here", command=lambda:self.check_out())
        check_out_button.place(x=300, y=120)


        switch_window_button = tk.Button(self, text="Logout", command= lambda:controller.show_frame(SignIn))
        switch_window_button.pack(side="bottom", fill=tk.X)


    def check_in(self):
        f2= open("Check in check out log/" + username + " Check in check out log.txt", "r")
        info2 = f2.read()
        f2.seek(0)
        f2.close()        

        f2= open("Check in check out log/" + username + " Check in check out log.txt", "a+")
        if len(info2) > 0 :
                f2.write("\n" + "\n")
        log_string= str("Check in time:"+ str(datetime_object))
        f2.write(str(log_string))
        f2.close()
        messagebox.showinfo(title="Welcome",message="Check in time was " + str(datetime_object) )


    def check_out(self):
        f2= open("Check in check out log/" + username + " Check in check out log.txt", "r")
        info2 = f2.read()
        f2.seek(0)
        f2.close()        

        f2= open("Check in check out log/" + username + " Check in check out log.txt", "a+")
        if len(info2) > 0 :
                f2.write("\n" + "\n")
        log_string= str("Check out time:"+ str(datetime_object))
        f2.write(str(log_string))
        f2.close()
        messagebox.showinfo(title="Welcome",message="Check out time was " + str(datetime_object))
    
    



test().mainloop()

