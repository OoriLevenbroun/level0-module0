from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    # Make a new window variable, window = Tk()
    
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    randInt =  random.randint(0, 3)
    # 2. Print your variable to the console
    print(randInt)
    # 3. Get the user to enter something that they think is awesome
    awe = simpledialog.askstring(title='what is awesome?', prompt='enter something that you think is awesome')
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if randInt == 0:
            messagebox.showinfo(title='AWESOME!', message=awe + ' is awesome')
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if randInt == 1:
            messagebox.showinfo(title='thats ok', message=awe + ' is ok')
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if randInt == 2:
        messagebox.showinfo(title='BORING!', message=awe + ' is BORING!')
    # 7. If your variable is  3
    if randInt == 3:
        messagebox.showinfo(title='error', message=awe + ' does not exist')
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
