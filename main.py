from tkinter import *
from gtts import gTTS
import tkinter as tk
import customtkinter
from tkinter import ttk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo
from tkinter.font import Font
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import pymysql
from subprocess import call
from gtts import gTTS
import os
import pyttsx3
import speech_recognition as sr
import random
import string
import pygame
from tkinter import PhotoImage, Entry, Button, Label, Canvas, Frame

root = tk.Tk()
root.title("Learning Alphabet")
root.geometry('1000x500')
root.configure(background='white')
root.resizable(False,False)


# Connection String
def connection():
    conn = pymysql.connect(host='localhost', user='root', password='', db='python_abc')
    return conn

#Savedata to database
def Save():
    main()

    #Save data into database
    '''
    username = str(user.get())
    ages = str(age.get())
    if (username == "Name" or username == "") or (ages == "Age" or ages == ""):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO `tbluser`(`NAME`, `AGE`) VALUES ('" + username + "','" + ages + "')")
            messagebox.showinfo("Error", "Welcome to Learning Alphabet")
            conn.commit()
            conn.close()
            main()
        except:
            messagebox.showinfo("Error", "Type name or age")
            return
        '''

#image login declaration
img = PhotoImage(file='images\iconbg.png')
Label(root, image=img, bg='white').place(x=50,y=50)
frame=Frame(root, width=400,height=350,bg="white")
frame.place(x=550, y=110)

heading=Label(frame, text='Learning Alphabet', fg='#71BA51', bg='white', font=('Microsoft YaHei UI', 25, 'bold'))
heading.pack()
heading.place(x=35,y=10)


#####Name-------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    if user.get()=='':
        user.insert(0, 'Name')

user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Name')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


#####Age-------------
def on_enter(e):
    age.delete(0, 'end')

def on_leave(e):
    if age.get()=='':
        age.insert(0,'Age')

age=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
age.place(x=30,y=150)
age.insert(0,'Age')
age.bind('<FocusIn>', on_enter)
age.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

def main():
    root.destroy()
    mainabc = tk.Tk()
    mainabc.title("Learning Alphabet")
    mainabc.geometry('1352x652+0+0')
    mainabc.configure(background='pink')

    str1 = StringVar()
    str1.set("Enjoy Learning Alphabet")
    ABC = Frame(mainabc, bg="pink")
    ABC.grid()

    cont = Canvas(ABC, width=180, height=125, bg="white")
    cont.grid(row=3, column=3)
    image1 = PhotoImage(file="images/alphabet1.png")
    image = cont.create_image(100, 70, image=image1)

    # Display Enjoy Learning Alphabet
    txtDISPLAY = Entry(ABC, textvariable=str1, font=('arial', 44, 'bold'), bg="salmon", bd=34, width=39, justify=CENTER)
    txtDISPLAY.grid(row=0, column=0, columnspan=7, pady=1)


    #button Alphabet function
    def Next():
        mainabc.destroy()
        def generate_random_alphabet():
            return random.choice(string.ascii_lowercase)

        def listen():

            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak now...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print( "You said:", text)
                return text
            except sr.UnknownValueError:
                print("Unable to recognize speech")
                return ""
            except sr.RequestError as e:
                print("Speech recognition request error:", str(e))
                return ""

        def speak(text):
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            for voice in voices:
                engine.setProperty('voice', voice.id)
            engine.setProperty("rate", 150)
            engine.setProperty("volume", 1.0)
            voice.name == 'Alex'
            engine.say(text)
            engine.runAndWait()

        def check_pronunciation(target_letter):
            attempts = 3
            for i in range(attempts):
                print(f"Attempt {i + 1}/{attempts}")
                speak(f"Please pronounce the alphabet {target_letter}")
                spoken_text = listen()
                if spoken_text.lower() == target_letter:
                    print("Correct pronunciation!")
                    speak(f"You got a correct pronunciation!")
                    return "Correct pronunciation!"
                else:
                    print("Incorrect pronunciation!")
                    speak(f"You got a incorrect pronunciation!")
                    if i == attempts - 1:
                        return "The attempt is over!"

        def on_rec():
            target_word = entry.get()
            result = check_pronunciation(target_word)
            result_label.config(text=result)

        def on_generate():
            random_alphabet = generate_random_alphabet()
            target_letter = f"Type the alphabet: {random_alphabet}"
            speak(target_letter)

        # Create the main window
        window = tk.Tk()
        window.title("Alphabet Pronunciation ")

        # Set window dimensions
        window_width = 1000
        window_height = 500

        # Get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Calculate the x and y coordinates for centering the window
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set the window's position
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        window.resizable(False,False)

        #image declaration
        filename = PhotoImage(file="images/bgabc.png")
        Label(window, image=filename).pack(padx=0,pady=0)

        # Add label and entry widgets
        label = tk.Label(window, bg="#BA8C63", text="Generate a letter and try to pronounce it", justify=CENTER, font="arial, 25")
        label.place(x=200, y=70)

        #Entry textbox
        def on_enter(e):
            entry.delete(0, 'end')

        def on_leave(e):
            if entry.get() == '':
                entry.insert(0, 'Click button to generate')

        entry = tk.Entry(window, width="40", fg="black", border=0, justify=CENTER, font="arial, 15")
        entry.insert(0, 'Type here the letter')
        entry.pack()
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        entry.place(x=220, y=140)

        # Add submit button
        turn_button = tk.Button(window, text="Next", command=on_rec, bg="#BADA55", fg="white", font="arial, 20",
                                activebackground="Salmon")
        turn_button.pack()
        turn_button.place(x=480, y=200)

        # Add generate button
        generate_button = tk.Button(window, text="Generate", command=on_generate, bg="#32D9CB", fg="white",
                                    font="arial, 20", activebackground="Salmon")
        generate_button.pack()
        generate_button.place(x=330, y=200)

        # Add result label
        result_label = tk.Label(window, text="", font="arial, 25", bg="#a6915c")
        result_label.pack()
        result_label.place(x=150, y=300)

        window.mainloop()


    pygame.init()

    #images files
    

    imageA = PhotoImage(file="images/Apple.png")
    def Alphabet_A():
        str1.set("A for Apple")
        image = cont.create_image(100, 65, image=imageA)
        tts = gTTS('A is For Apple. Can you say. A?', lang='en', tld='as')
        tts.save("audio/Alphabet_A.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_A.mp3")
        sound.play()
        os.remove(Alphabet_A.mp3)

    imageB = PhotoImage(file="images/Basketball.png")
    def Alphabet_B():
        str1.set("B for Ball")
        image = cont.create_image(90, 70, image=imageB)
        tts = gTTS('B is For Ball. Can you say. B?', lang='en', tld='as')
        tts.save("audio/Alphabet_B.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_B.mp3")
        sound.play()
        os.remove(Alphabet_B.mp3)

    imageC = PhotoImage(file="images/Cat.png")
    def Alphabet_C():
        str1.set("C for Cat")
        image = cont.create_image(90, 70, image=imageC)
        tts = gTTS('C is For Cat. Can you say. C?', lang='en', tld='as')
        tts.save("audio/Alphabet_C.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_C.mp3")
        sound.play()
        os.remove(Alphabet_C.mp3)

    imageD = PhotoImage(file="images/Dog.png")
    def Alphabet_D():
        str1.set("D for Dog")
        image = cont.create_image(100, 70, image=imageD)
        tts = gTTS('D is For Dog. Can you say. D?', lang='en', tld='as')
        tts.save("audio/Alphabet_D.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_D.mp3")
        sound.play()
        os.remove(Alphabet_D.mp3)

    imageE = PhotoImage(file="images/Egg.png")
    def Alphabet_E():
        str1.set("E for Egg")
        image = cont.create_image(90, 70, image=imageE)
        tts = gTTS('E is For Egg. Can you say. E?', lang='en', tld='as')
        tts.save("audio/Alphabet_E.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_E.mp3")
        sound.play()
        os.remove(Alphabet_E.mp3)

    imageF = PhotoImage(file="images/Fish.png")
    def Alphabet_F():
        str1.set("F for Fish")
        image = cont.create_image(100, 70, image=imageF)
        tts = gTTS('F is For Fish. Can you say. F?', lang='en', tld='as')
        tts.save("audio/Alphabet_F.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_F.mp3")
        sound.play()
        os.remove(Alphabet_F.mp3)

    imageG = PhotoImage(file="images/Gift.png")
    def Alphabet_G():
        str1.set("G for Gift")
        image = cont.create_image(100, 70, image=imageG)
        tts = gTTS('G is For Gift. Can you say. G?', lang='en', tld='as')
        tts.save("audio/Alphabet_G.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_G.mp3")
        sound.play()
        os.remove(Alphabet_G.mp3)

    imageH = PhotoImage(file="images/Hotdog.png")
    def Alphabet_H():
        str1.set("H for Hotdog")
        image = cont.create_image(100, 70, image=imageH)
        tts = gTTS(' H is For Hotdog. Can you say. H?', lang='en', tld='as')
        tts.save("audio/Alphabet_H.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_H.mp3")
        sound.play()
        os.remove(Alphabet_H.mp3)

    imageI = PhotoImage(file="images/Icecream.png")
    def Alphabet_I():
        str1.set("I for Icecream")
        image = cont.create_image(100, 70, image=imageI)
        tts = gTTS(' I is For Ice cream. Can you say. I ?', lang='en', tld='as')
        tts.save("audio/Alphabet_I.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_I.mp3")
        sound.play()
        os.remove(Alphabet_I.mp3)

    imageJ = PhotoImage(file="images/Juice.png")
    def Alphabet_J():
        str1.set("J for Juice")
        image = cont.create_image(90, 60, image=imageJ)
        tts = gTTS(' J is For Juice . Can you say. J?', lang='en', tld='as')
        tts.save("audio/Alphabet_J.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_J.mp3")
        sound.play()
        os.remove(Alphabet_J.mp3)

    imageK = PhotoImage(file="images/Kite.png")
    def Alphabet_K():
        str1.set("K for Kite")
        image = cont.create_image(80, 70, image=imageK)
        tts = gTTS('K is For Kite. Can you say. K?', lang='en', tld='as')
        tts.save("audio/Alphabet_K.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_K.mp3")
        sound.play()
        os.remove(Alphabet_K.mp3)

    imageL = PhotoImage(file="images/Lion.png")
    def Alphabet_L():
        str1.set("L for Lion")
        image = cont.create_image(90, 70, image=imageL)
        tts = gTTS('L is For Lion. Can you say. L?', lang='en', tld='as')
        tts.save("audio/Alphabet_L.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_L.mp3")
        sound.play()
        os.remove(Alphabet_L.mp3)

    imageM = PhotoImage(file="images/Monkey.png")
    def Alphabet_M():
        str1.set("M for Monkey")
        image = cont.create_image(90, 70, image=imageM)
        tts = gTTS('M is For Monkey. Can you say. M?', lang='en', tld='as')
        tts.save("audio/Alphabet_M.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_M.mp3")
        sound.play()
        os.remove(Alphabet_M.mp3)

    imageN = PhotoImage(file="images/Net.png")
    def Alphabet_N():
        str1.set("N for Net")
        image = cont.create_image(100, 70, image=imageN)
        tts = gTTS('N is For Net. Can you say. N?', lang='en', tld='as')
        tts.save("audio/Alphabet_N.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_N.mp3")
        sound.play()
        os.remove(Alphabet_N.mp3)

    imageO = PhotoImage(file="images/Orange.png")
    def Alphabet_O():
        str1.set("O for Orange")
        image = cont.create_image(100, 60, image=imageO)
        tts = gTTS('O is For Orange. Can you say. O?', lang='en', tld='as')
        tts.save("audio/Alphabet_O.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_O.mp3")
        sound.play()
        os.remove(Alphabet_O.mp3)

    imageP = PhotoImage(file="images/Penguin.png")
    def Alphabet_P():
        str1.set("P for Penguin")
        image = cont.create_image(90, 70, image=imageP)
        tts = gTTS('P is For Penguin. Can you say. P?', lang='en', tld='as')
        tts.save("audio/Alphabet_P.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_P.mp3")
        sound.play()
        os.remove(Alphabet_P.mp3)

    imageQ = PhotoImage(file="images/Queen.png")
    def Alphabet_Q():
        str1.set("Q for Queen")
        image = cont.create_image(95, 70, image=imageQ)
        tts = gTTS('Q is For Queen. Can you say. Q?', lang='en', tld='as')
        tts.save("audio/Alphabet_Q.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_Q.mp3")
        sound.play()
        os.remove(Alphabet_Q.mp3)

    imageR = PhotoImage(file="images/Robot.png")
    def Alphabet_R():
        str1.set("R for Robot")
        image = cont.create_image(90, 70, image=imageR)
        tts = gTTS('R is For Robot. Can you say. R?', lang='en', tld='as')
        tts.save("audio/Alphabet_R.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_R.mp3")
        sound.play()
        os.remove(Alphabet_R.mp3)

    imageS = PhotoImage(file="images/Sun.png")
    def Alphabet_S():
        str1.set("S for Sun")
        image = cont.create_image(100, 70, image=imageS)
        tts = gTTS('S is For Sun. Can you say. S?', lang='en', tld='as')
        tts.save("audio/Alphabet_S.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_S.mp3")
        sound.play()
        os.remove(Alphabet_S.mp3)

    imageT = PhotoImage(file="images/Table.png")
    def Alphabet_T():
        str1.set("T for Table")
        image = cont.create_image(100, 70, image=imageT)
        tts = gTTS('T is For Table. Can you say. T?', lang='en', tld='as')
        tts.save("audio/Alphabet_T.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_T.mp3")
        sound.play()
        os.remove(Alphabet_T.mp3)

    imageU = PhotoImage(file="images/Umbrella.png")
    def Alphabet_U():
        str1.set("U for Umbrella")
        image = cont.create_image(90, 70, image=imageU)
        tts = gTTS('U is For Umbrella. Can you say. U?', lang='en', tld='as')
        tts.save("audio/Alphabet_U.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_U.mp3")
        sound.play()
        os.remove(Alphabet_U.mp3)

    imageV = PhotoImage(file="images/Violin.png")
    def Alphabet_V():
        str1.set("V for Violin")
        image = cont.create_image(90, 55, image=imageV)
        tts = gTTS('V is For Violin. Can you say. V?', lang='en', tld='as')
        tts.save("audio/Alphabet_V.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_V.mp3")
        sound.play()
        os.remove(Alphabet_V.mp3)

    imageW = PhotoImage(file="images/Watch.png")
    def Alphabet_W():
        str1.set("W for Watch")
        image = cont.create_image(100, 70, image=imageW)
        tts = gTTS('W is For Watch. Can you say. W?', lang='en', tld='as')
        tts.save("audio/Alphabet_W.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_W.mp3")
        sound.play()
        os.remove(Alphabet_W.mp3)

    imageX = PhotoImage(file="images/Xylophone.png")
    def Alphabet_X():
        str1.set("X for Xylophone")
        image = cont.create_image(90, 70, image=imageX)
        tts = gTTS('X is For Xylophome. Can you say. X?', lang='en', tld='as')
        tts.save("audio/Alphabet_X.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_X.mp3")
        sound.play()
        os.remove(Alphabet_X.mp3)

    imageY = PhotoImage(file="images/Yoyo.png")
    def Alphabet_Y():
        str1.set("Y for Yoyo")
        image = cont.create_image(90, 70, image=imageY)
        tts = gTTS('Y is For Yoyo. Can you say. Y?', lang='en', tld='as')
        tts.save("audio/lphabet_Y.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_Y.mp3")
        sound.play()
        os.remove(Alphabet_Y.mp3)

    imageZ = PhotoImage(file="images/Zebra.png")
    def Alphabet_Z():
        str1.set("Z for Zebra")
        image = cont.create_image(90, 80, image=imageZ)
        tts = gTTS('Z is For Zebra. Can you say. Z?', lang='en', tld='as')
        tts.save("audio/Alphabet_Z.mp3")
        sound = pygame.mixer.Sound("audio/Alphabet_Z.mp3")
        sound.play()
        os.remove(Alphabet_Z.mp3)

#row1
    btnA = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Aa", bg="#FF9999", command=Alphabet_A).grid(row=1,column=0)
    btnB = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Bb", bg="#78C9EC", command=Alphabet_B).grid(row=1,column=1)
    btnC = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Cc", bg="#FEEAA8", command=Alphabet_C).grid(row=1,column=2)
    btnD = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Dd", bg="#17B090", command=Alphabet_D).grid(row=1,column=3)
    btnE = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Ee", bg="#F89538", command=Alphabet_E).grid(row=1,column=4)
    btnF = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Ff", bg="#C9C1FE",command=Alphabet_F).grid(row=1,column=5)
    btnG = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Gg", bg="#BADA55", command=Alphabet_G).grid(row=1,column=6)


    # row2
    btnH = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Hh", bg="#BADA55", command=Alphabet_H).grid(row=2,column=0)
    btnI = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Ii", bg="#C9C1FE",command=Alphabet_I).grid(row=2,column=1)
    btnJ = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Jj", bg="#F89538",command=Alphabet_J).grid(row=2,column=2)
    btnK = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Kk", bg="#32D9CB",command=Alphabet_K).grid(row=2,column=3)
    btnL = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Ll", bg="#FEEAA8",command=Alphabet_L).grid(row=2,column=4)
    btnM = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Mm", bg="#78C9EC",command=Alphabet_M).grid(row=2,column=5)
    btnN = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Nn", bg="#FF9999",command=Alphabet_N).grid(row=2,column=6)

    #row3
    btnO = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Oo", bg="#FF9999",command=Alphabet_O).grid(row=3, column=0)
    btnP = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Pp", bg="#78C9EC",command=Alphabet_P).grid(row=3, column=1)
    btnQ = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Qq", bg="#FEEAA8",command=Alphabet_Q).grid(row=3, column=2)
    btnR = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Rr", bg="#F89538",command=Alphabet_R).grid(row=3, column=4)
    btns = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Ss", bg="#C9C1FE",command=Alphabet_S).grid(row=3, column=5)
    btnT = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Tt", bg="#BADA55",command=Alphabet_T).grid(row=3, column=6)

    # row4
    btnU = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Uu", bg="#78C9EC",command=Alphabet_U).grid(row=4, column=0)
    btnV = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Vv", bg="#BADA55",command=Alphabet_V).grid(row=4, column=1)
    btnW = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Ww", bg="#C9C1FE",command=Alphabet_W).grid(row=4, column=2)
    btnX = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Xx", bg="#F89538",command=Alphabet_X).grid(row=4, column=3)
    btnY = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Yy", bg="#32D9CB",command=Alphabet_Y).grid(row=4, column=4)
    btnZ = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Zz", bg="#FEEAA8",command=Alphabet_Z).grid(row=4, column=5)
    btnDone = Button(ABC, pady=1, bd=4, font=('arial', 21, 'bold'), width=10, height=3, text="Next", bg="#E91818",command=Next).grid(row=4, column=6)


    mainabc.mainloop()

#####BTNENTER-------------
Button(frame,width=39,pady=7,text='Enter',bg='#71BA51',fg='white',border=0, command=Save).place(x=35,y=204)

root.mainloop()