from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Ask the user for their name and save it to a variable
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    name = simpledialog.askstring(title= 'Greeter', prompt="what is your name")
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo(message= "hello " + name + ", I will be watching you")
    messagebox.showinfo(message='and just so you know ' + name + ', I am never gonna give you up, never gonna let you down, never gonna turn around and HURT YOU!')
    # Print your message to the console using the print() function
    print('hello' + name)
    # Show an error message using messagebox.showerror()
    messagebox.showerror(title = 'error', message = 'viruse detected')
    sos = simpledialog.askinteger(title='the only way to stop the virus is to enter the password', prompt='enter password')
    if sos == 123:
        messagebox.showinfo(title='good job', message='you saved humanity')
    else:
        messagebox.showerror(title='wrong', message='humanity will now suffer becuse of you')
    # Run the window's .mainloop() method
    window.mainloop()
    pass
