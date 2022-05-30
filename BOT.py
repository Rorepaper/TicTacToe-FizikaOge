from tkinter import *
from time import *
from random import *
from tkinter.ttk import Combobox
from pyglet import *
from pygame import mixer


# Функция перобора выйгрышных комбинаций
def winner(a):
    b = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    game = 0
    for i in range(len(b)):
        count = 0

        for j in range(len(b[i])):
            if a.count(b[i][j]) != 0:
                count += 1
        if count == 3:
            return b[i]


# Функция обновления панели времени каждую секунду
def tick():
    global time1
    time2 = strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clockTime.config(text=time2)
    clockTime.after(200, tick)


def Bot(mode):
    global xod, moves, player, winComb, player2
    corners = [0, 2, 6, 8]
    BotInteger = 0
    if mode == 0:
        if xod < 8:
            random = randint(0, 8)
            while random in moves:
                random = randint(0, 8)
        else:
            random = 0
        return random
    elif mode == 2:
        if 1 < xod < 9:
            for i in range(len(winComb)):
                count = 0
                streakMoves = []
                for j in range(len(winComb[i])):
                    count += 1
                    if winComb[i][j] in player:
                        streakMoves.append(winComb[i][j])
                        if len(streakMoves) > 1:
                            for a in winComb[i]:
                                if a not in streakMoves:
                                    BotInteger = a
                                    if a in player2:
                                        return Bot(0)
                                    else:
                                        streakMoves.append(a)
                                        winComb.pop(i)
                                        streakMoves = []
                                        return BotInteger
            return Bot(0)
        elif xod == 0:
            if 4 not in moves:
                BotInteger = 4
            else:
                if BotInteger not in moves:
                    BotInteger = corners[randint(0, 3)]
            return BotInteger
        else:
            return 0
    elif mode == 1:
        fakeWinComb = winComb[:]
        print(fakeWinComb)
        fakeWinComb.pop(randint(0, len(fakeWinComb) - 1))
        fakeWinComb.pop(randint(0, len(fakeWinComb) - 1))
        print(fakeWinComb)
        if 1 < xod < 9:

            for i in range(len(fakeWinComb)):
                count = 0
                streakMoves = []
                for j in range(len(fakeWinComb[i])):
                    count += 1
                    if fakeWinComb[i][j] in player:
                        streakMoves.append(fakeWinComb[i][j])
                        if len(streakMoves) > 1:
                            for a in fakeWinComb[i]:
                                if a not in streakMoves:
                                    BotInteger = a
                                    if a in player2:
                                        return Bot(0)
                                    else:
                                        streakMoves.append(a)
                                        fakeWinComb.pop(i)
                                        streakMoves = []
                                        return BotInteger
            return Bot(0)
        elif xod == 0:
            if 4 not in moves:
                BotInteger = 4
            else:
                if BotInteger not in moves:
                    BotInteger = corners[randint(0, 3)]
            return BotInteger
        else:
            return 0
    else:
        return 0


def defocus(event):
    event.widget.master.focus_set()

def stop_music():
    global count1
    count1 += 1
    if count1 % 2 != 0:
        mixer.music.pause()
    else:
        mixer.music.unpause()
def stop_sound():
    global count2, soundOn
    count2 += 1
    if count2 % 2 != 0:
        soundOn = False
    else:
        soundOn = True
def Reset():
    global wins1, wins2, games, xod, mode, field
    wins1, wins2, games = 0, 0, 0
    info.config(text=f'Кол-во игр: {games}  Ход №: {xod + 1}  Режим: {mode}  Поле: {field}')
    score.config(text=str(wins1) + ' : ' + str((wins2)))

# Объявление переменных
font.add_file('reef.otf')
soundOn = True
time1 = ''
w = 115
count1 = 0
count2 = 0
xod = 0
games = 0
wins1 = 0
wins2 = 0
ButtonList = []
player1 = []
player = []
player2 = []
moves = []

winComb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
root = Tk()
music = PhotoImage(file=r"note.png")
music = music.subsample(8, 8)
sound = PhotoImage(file=r"sound.png")
sound = sound.subsample(5, 5)
reset = PhotoImage(file=r"reset.png")
reset = reset.subsample(9, 9)
mode = 'Бот'
field = '3x3'

# Построение окна Tkinter
root['bg'] = '#8E9B97'
root.iconphoto(False, PhotoImage(file='ico.png'))
root.title('TicTacToe')
root.wm_attributes('-alpha', 0.97)
root.geometry('400x500')
root.resizable(width=False, height=False)

canvas = Canvas(root)
canvas.place(rely=0.3, relx=0.075, relwidth=0.85, relheight=0.68)

canvas1 = Frame(root, bg='#8E9B97')
canvas1.place(x=50, y=30)

title1 = Label(master=canvas1, bg='#F4EBDB', font='reef 20', text='Крестики')
title1.pack(side=LEFT)

score = Label(master=canvas1, bg='#F4EBDB', font='reef 40')
score.pack(side=LEFT)

title2 = Label(master=canvas1, bg='#F4EBDB', font='reef 20', text='Нолики')
title2.pack(side=LEFT)
info = Label(bg='#F4EBDB', font='reef 12', text=f'Кол-во игр: {games}  Ход №: {xod + 1}  Режим: {mode}  Поле: {field}')
info.place(x=40, y=90)

clockTime = Label(font=('reef', 16))
clockTime.place(x=5, y=5)

combo = Combobox(root, font='reef 12', state="readonly")
combo['values'] = ('Легкий уровень', 'Средний уровень', 'Высокий уровень', 'Два на Два')
combo.bind("<FocusIn>", defocus)
combo.current(3)
combo.place(rely=0.245, relx=0.325, relwidth=0.35, relheight=0.05)
root.option_add('*TCombobox*Listbox.font', 'reef 12')

button_stop = Button(image=music, command=stop_music)
button_stop.place(y=5, x=320, width=35, height=35)

button_sound = Button(image=sound, command=stop_sound)
button_sound.place(y=5, x=360, width=35, height=35)

button_reset = Button(image=reset, command=Reset)
button_reset.place(y=5, x=280, width=35, height=35)

class Btn():
    global w, buttonList

    def __init__(self, x0, y0, idd):
        self.idd = idd
        self.x0 = x0
        self.y0 = y0
        self.Button1 = Button(master=canvas, bg='#F4EBDB', bd=3, font=('Comic Sans MS', 24, 'bold'), text=self.idd + 1)
        self.Button1.place(x=self.x0, y=self.y0, width=w, height=w)
        self.Button1.bind('<Button-1>', self.click)

    def unbind1(self, non):
        self.Button1.unbind('<Button-1>')
        self.Button1.config(text='O', bg='#FFCCBB')

    def restart(self, idd):
        self.idd = idd
        self.Button1.config(text=idd + 1, bg='#F4EBDB')
        self.Button1.bind('<Button-1>', self.click)
        score.config(text=str(wins1) + ' : ' + str((wins2)))

    # Обновление счёта и построение поля
    def show(self):
        global ButtonList
        ButtonList = []
        score.config(text=str(wins1) + ' : ' + str((wins2)))
        idd = 0
        x = 0
        y = 0
        for i in range(3):
            for j in range(3):
                ButtonList.append(Btn(x, y, idd))
                x += w
                idd += 1
            x = 0
            y += w

    # Команда, вызываемая нажатием на кнопку
    def click(self, non):
        global xod, wins1, wins2, moves, player, player1, player2, games, idd, char, ended, mode, field, winComb
        ended = False
        char = "X"
        if combo.current() == 3:
            mode = '2x2'
            xod += 1
            if xod % 2 == 0:
                char = "X"
                self.Button1.config(text=char, bg='#6EB5C0')
                player1.append(self.idd)
                if winner(player1) != None:
                    wins1 += 1
                    ended = True
            elif xod == 9:
                char = 'X'
                self.Button1.config(text=char, bg='#6EB5C0')
                ended = True
            else:
                char = 'O'
                self.Button1.config(text=char, bg='#FFCCBB')
                player2.append(self.idd)
                if winner(player2) != None:
                    wins2 += 1
                    ended = True
            self.Button1.unbind('<Button-1>')
        else:
            mode = 'Бот'
            player1.append(self.idd)
            player.append(self.idd)
            moves.append(self.idd)
            BotMove = Bot(combo.current())
            xod += 2

            player2.append(BotMove)
            moves.append(BotMove)

            self.Button1.unbind('<Button-1>')
            self.Button1.config(text=char)
            ButtonList[BotMove].unbind1('<Button-1>')

            # Выяснение исхода игры
            if xod > 9:
                ended = True
            elif winner(player1) != None:
                wins1 += 1
                ended = True
            elif winner(player2) != None:
                wins2 += 1
                ended = True

        # Обнуление переменных и очистка поля
        if ended == True:
            moves, player, player1, player2, xod, idd, char, ended = [], [], [], [], 0, 0, 'X', False
            winComb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            games += 1

            for g in range(9):
                ButtonList[g].restart(g)

        # Обновление информации
        info.config(text=f'Кол-во игр: {games}  Ход №: {xod + 1}  Режим: {mode}  Поле: {field}')
        if soundOn == True:
            mixer.Sound.play(clickSound)



# Тело программы
tick()
Btn.show(0)
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)
clickSound = mixer.Sound('click.mp3')
root.mainloop()
