import string
from tkinter import *
import tkinter as tk
import random

width=13
height=13

global score
score = 0


def put_word(word,grid):
    # word = random.choice([word, word[::-1]])
    dir = random.choice([[1, 0], [0, 1], [1, 1]])
    x_size = width  if dir[0] == 0 else width - len(word)
    y_size = height if dir[1] == 0 else height - len(word)

    x = random.randrange(0, x_size)
    y = random.randrange(0, y_size)

    print([x, y])

    for i in range(0, len(word)):
        grid[y + dir[1] * i][x + dir[0] * i] = word[i]
    return grid

words = ['FRANCE','RUSSIA','JAPAN','GERMANY','ITALY']

grid = [[random.choice(string.ascii_uppercase) for i in range(0,width)] for j in range(0,height)]

for word in words:
    grid= put_word(word,grid)



def startwin():
    top= Toplevel()
    top.title('GAME')

    head = Label(top,text="Find the hidden countries!!",font=('helvetica',30,'bold','underline'),fg="#3F3F3F").grid()

    for i in range(width):
        lb3 = Label(top, text=' '.join(grid[i]), font=('gothic', 20, 'bold'), fg='#3E3F64').grid()

    text_input = StringVar()

    sc = Label(top, text=('                            SCORE : ' + str(score) + '                             '),bg='#3F3F3F',fg='white',font=('helvetica',13,'bold'))
    sc.grid()

    def btnClick():

        global score
        x = ans.get()
        print(x)

        if x in words:
            score += 10
            sc.config(text=('                      SCORE : ' + str(score) + '                             '))

        else:
            print(score)

        text_input.set("")



    ans = Entry(top, font=('helvetica', 30), bg='#3E3F64', fg='white' ,bd=10, justify='left', textvariable=text_input, insertwidth=6)
    ans.grid()

    check = Button(top,font=('helvetica',8,'bold'),text='CHECK',padx=220,pady=8,bd=4,command= btnClick).grid()

    hint0 = Label(top, font=('helvetica', 15, 'bold'),
                  text=">>>>>> Hints <<<<<<", fg='#3E3F64',anchor="center").grid()
    hint1 = Label(top,font=('helvetica',9,'bold'),text="1. Bonjour! Coffee and cheese, what a speciality here! ",fg='#125E00').grid()
    hint2 = Label(top, font=('helvetica', 9, 'bold'),
                  text="2. My citizen was the first human to travel in the outer space, cool enough :)",fg='#125E00').grid()
    hint3 = Label(top, font=('helvetica', 9, 'bold'),
                  text="3. Kon ni chi wa! Pls do not leave from here without tasting the noodles.",fg='#125E00').grid()
    hint4 = Label(top, font=('helvetica', 9, 'bold'),
                  text="4. Volks Wagen innovation centre <3",fg='#125E00').grid()
    hint5 = Label(top, font=('helvetica', 9, 'bold'),
                  text="5. Lean lean lean Leaning Tower of Pisa on me!",fg='#125E00').grid()


   # score = Label(top,).grid()





h=300
w=350

root=Tk()
root.title('WordSearch')


canvas=tk.Canvas(root,height=h,width=w).grid()

frame=tk.Frame(root,bg='#3E3F64',height=h,width=w)
frame.place(relwidth=1,relheight=1)

lb1=tk.Label(frame,font=('aharoni',35,'bold'),text='  Word-Search',fg='white',bg='#3E3F64',anchor='center').grid(row=1,column=2)

start = tk.Button(frame,font=('helvetica',20,'bold'),text='START',padx=12,pady=8,bd=8,bg='#40AF45',command=lambda:startwin()).grid(row=3,column=2, padx=30, pady=10)

quit = tk.Button(frame,font=('helvetica',20,'bold'),text=' QUIT ',padx=12,pady=8,bd=8,bg='#EE2E2E',command=lambda:root.destroy()).grid(row=5,column=2, padx=30, pady=10)

tk.mainloop()