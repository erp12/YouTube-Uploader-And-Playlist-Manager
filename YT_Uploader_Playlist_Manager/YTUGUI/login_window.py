'''
Created on May 9, 2014

@author: Eddie
'''
import Tkinter as tk

#import YTapiManager.YTapi_interface

class LogInScreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.master.title('LogIn Screen')
    
    def createWidgets(self):
        self.instructions_label = tk.Label(self, text='Enter Your YouTube Account Info\n|======================|')
        self.instructions_label.grid(row=0, column=0, columnspan = 2)
        
        self.username_label = tk.Label(self, text='Username:')
        self.username_label.grid(row=1, column = 0)
        
        self.passoword_label = tk.Label(self, text='Password:')
        self.passoword_label.grid(row = 2, column = 0)
        
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row = 1, column=1)
        
        self.password_entry = tk.Entry(self)
        self.password_entry.grid(row = 2, column=1)
        
        self.login_button = tk.Button(self, text = 'Log In')
        self.login_button.grid(row = 3, column = 0, columnspan = 2)

app = LogInScreen()
app.mainloop()