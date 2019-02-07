import tkinter
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
timeleft = 30
miss = -1

def startGame(event):
    if timeleft == 30:
        countdown()
    nextColor()

def nextColor():
    global score
    global timeleft
    global miss

    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        else:
            miss += 1
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        label.config(fg = str(colors[1]), text = str(colors[0]))
        scoreLabel.config(text = "Score: " + str(score))
        missLabel.config(text = "Miss: " + str(miss))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time Left: " + str(timeleft))
        timeLabel.after(1000,countdown)

#Driver GUI Code
root = tkinter.Tk()
show = tkinter.Tk()

root.title("SAY THE COLOR GAME")
root.geometry("375x250")

instructions = tkinter.Label(root, text = "Type in the color of the words, and not the color text!", font = ('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press to enter start", font = ("Helvetica", 12))
scoreLabel.pack()

missLabel = tkinter.Label(root, text = "", font = ("Helvetica", 12))
missLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ("Helvetica", 12))
timeLabel.pack()

label = tkinter.Label(root, font = ("Helvetica", 60))
label.pack()

e = tkinter.Entry(root)
root.bind("<Return>", startGame)
e.pack()
e.focus_set()
root.mainloop()
