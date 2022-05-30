from tkinter import *
from random import *

def wrong():
    result(False)


def correct():
    result(True)


def check():
    global quests
    question2.config(text='='.join(quests[number][1:]))


def result(bol):
    global corrects, number, quests, res
    if bol:
        corrects += 1
        res.append(corrects)
    number += 1
    if number == len(quests):
        print(*res)
        exit()
    question1.config(text=quests[number][0])
    question.config(text=f'Вопрос номер: {number}  Правильных: {corrects}')


corrects = 0
number = 0
file = open('fiz.txt', encoding='utf-8')
quests = []
for col in file:
    quests.append(col)
shuffle(quests)
qu = []
for que in range(len(quests)):
    a = quests[que].split('=')
    if len(a) != 1:
        qu.append(a)

quests = qu
res = []
root = Tk()
# Построение окна Tkinter
root['bg'] = '#8E9B97'
root.iconphoto(False, PhotoImage(file='ico.png'))
root.title('ФИЗИКА ОГЭ')
root.wm_attributes('-alpha', 0.97)
root.geometry('400x400')
root.resizable(width=False, height=False)

title1 = Label(bg='#F9EBDC', font='reef 20 bold', text='ТЕСТ ОГЭ ПО ФИЗИКЕ')
title1.place(relx=0.22, y=30)

question = Label(bg='#F4EBDB', font='reef 16', text=f'Вопрос номер: 0  Правильных: 0')
question.place(y=70, relw=1)

question1 = Label(bg='#F4EBDB', font='reef 24', text='нажми начать')
question1.place(rely=0.28, relw=1)

button_check = Button(bg='#696969', command=check, text='Проверить', font='reef 20 bold')
button_check.place(rely=0.40, relx=0.335, h=35)

question2 = Label(bg='#F4EBDB', font='reef 16', text='нажми начать')
question2.place(rely=0.50, relw=1)

button_wr = Button(bg='#8B0000', command=wrong, text='X', font='reef 30 bold')
button_wr.place(y=320, relx=0.25, h=35)

button_cr = Button(bg='#00FA9A', command=correct, text='0', font='reef 30 bold')
button_cr.place(y=320, relx=0.65, h=35)

root.mainloop()
