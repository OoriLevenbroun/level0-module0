from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    q = simpledialog.askstring(title="question 1:", prompt='Who are Starsky & Hutch?')
    #      // 3.  Use an if statement to check if their answer is correct
    if q == 'Paul Michael Glaser & David Soul':
        score += 5
    else:
        messagebox.showerror(title='WRONG!', message='WRONG!')
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    q2 = simpledialog.askstring(title='question 2', prompt='what is the biggest waterfall in the world?')
    if q2 == 'angel falls':
        score += 3
    else:
        messagebox.showerror(title='WRONG!', message='WRONG!')
    q3 = simpledialog.askstring(title='question 3', prompt='which knight from the round table was worthy enough to see the holy grail and be taken into heven')
    if q3 == 'galahad' or q3 == 'sir galahad':
        score += 5
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title='final score', message=score)
    # Run the window's .mainloop() method
