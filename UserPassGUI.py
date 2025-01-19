import tkinter as tk
# Importing Tkinter and naming it ttk
import ttkbootstrap as ttk
# importing Ttkbootstrap and naming ttk

def GetInformation():
    # I created a function so we can call on it when the button is clicked 
    GetUsr = EntryString.get()
    # I am getting the entry string the same one I put inside the textvariable inside username
    
    GetPasswd = PasswordEntry.get()
    # Same thing here I get the entry the user put in and convert it into a string 
    writenames = GetUsr
    GetPasswd = GetPasswd
    # Creating a variable for both inputs 
    with open('UserPasswords.xlsx', 'a') as info:
        info.write("\n" + writenames + "/" + GetPasswd)
        # I created a xlsx file inputing the username and passwords 
        
        
        
        
    
Window = ttk.Window(themename="darkly")
# I made my ttk window using ttk would allow us to work with the many different themes 

Window.geometry('800x800')
# When the window is opened it is automatically sized 800x800
Window.title("Safest Encryption Platform")
# This will be the title that can only be seen on top of the web application

Title_Service = ttk.Label(master=Window, 
                          # I created a label which this would show on the window
                          text="Welcome, Please put UserName and Password", 
                          font="Arial 25 bold")
                          # The font goes like: Font, Size, Typographical Emphasis like bold and underlines 
Title_Service.pack()
# This would pack the title in the middle of the screen 

EntryString = tk.StringVar()
# This is getting the entry and converting it to a string 
# We can also use tk.intVar()

PrivacyFrame = ttk.Frame(master=Window)
# I created another Frame inside the window so I could have all the buttons and entry's together
UserName = ttk.Entry(master=PrivacyFrame, 
                     # I created the first entry to get the username 
                    textvariable=EntryString )
                    # I created used the built in paramenter textvariable in order to convert it into a string 
PasswordEntry = tk.StringVar()
# This converts the password into a string as well
Passwords = ttk.Entry(master=PrivacyFrame, textvariable=PasswordEntry)
# This is the entry for the password

Continue_Button = ttk.Button(master=PrivacyFrame, text="Continue", command=GetInformation)
# I created a button and added a command inside of it which then everytime the button is clicked it would excute the function
PrivacyFrame.pack()
# First I packed the main Frame 
UserName.pack(pady=10)
# under the frame I packed the username entry I made sure to add a small gap using pady()
Passwords.pack(pady=5)
# Same with here except the password entry is under the username entry
Continue_Button.pack(pady=5)
# and lastly the button I packed under the passwords entry 

Window.mainloop()
# In order for us to use the GUI we would have to keep looping through it 
