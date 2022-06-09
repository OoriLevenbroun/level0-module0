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
    q = simpledialog.askstring(title="question 1:", prompt='you measure my life in hours and I serve you by expiring. im quick when Im thin and slow when im fat. The wind is my enemy, who am i.')
    #      // 3.  Use an if statement to check if their answer is correct
    if q == 'A candle' or q == 'candle' or q == 'a candle':
        score += 5
    else:
        messagebox.showerror(title='WRONG!', message='you suck, get a life!')
        score -=5
    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    q2 = simpledialog.askstring(title='question 2', prompt='wht is seen in the midddle of march and april that cant be seen at the beginning or end of either month')
    if q2 == 'r' or q2 == 'R':
        score += 3
    else:
        messagebox.showerror(title='WRONG!', message='WRONG!')
        score -= 3
    q3 = simpledialog.askstring(title='question 3', prompt='what word in the english language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire word signifies a great woman, what is the word?')
    if q3 == 'heroine' or q3 == 'Heroine':
        score += 5
    else:
        messagebox.showerror(title='you suck!', message='you are the worst person to ever exist')
        score -= 5
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    messagebox.showinfo(title='final score', message=score)
    # Run the window's .mainloop() method
