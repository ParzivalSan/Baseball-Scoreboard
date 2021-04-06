from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk


def scoreboard():
  global ScoreBoardScreen
  ScoreBoardScreen=Toplevel()
  ScoreBoardScreen.resizable(0,0) 
  ScoreBoardScreen.geometry("300x200")
  ScoreBoardScreen.configure(bg='white')
  #ScoreBoardScreen.overrideredirect(True) #Eliminamos el title bar

  #logoAway
  global logoAway
  logoAway=Image.open("logo/gava.png")
  logoAway=logoAway.resize((25,25),Image.ANTIALIAS)
  logoAway=ImageTk.PhotoImage(logoAway)

  Label(ScoreBoardScreen,image=logoAway, bg='white').grid(row=0, column=0, rowspan=2)
  Label(ScoreBoardScreen,text="GAV", font=("Calibri",12), bg="white").grid(row=0, column=1,rowspan=2, padx=1,pady=1)

  #logoHome
  global logoHome
  logoHome=Image.open("logo/Barcelona.jpg")
  logoHome=logoHome.resize((25,25),Image.ANTIALIAS)
  logoHome=ImageTk.PhotoImage(logoHome)

  Label(ScoreBoardScreen,image=logoHome, bg='white').grid(row=3, column=0, rowspan=2)
  Label(ScoreBoardScreen,text="CBB", font=("Calibri",12), bg='white').grid(row=3, column=1,rowspan=2,padx=1,pady=1)

  #Score
  global RunsAway
  RunsAway=0
  global RunsHome
  RunsHome=0

  Label(ScoreBoardScreen,text=RunsAway, font=("Calibri",12), bg='white').grid(row=0, column=2, rowspan=2)
  Label(ScoreBoardScreen,text=RunsHome, font=("Calibri",12), bg='white').grid(row=3, column=2, rowspan=2)

  #Inning
  global innScoreBoardScreen
  innScoreBoardScreen=Image.open("logo/Arrow top.png")
  innScoreBoardScreen=innScoreBoardScreen.resize((15,15),Image.ANTIALIAS)
  innScoreBoardScreen=ImageTk.PhotoImage(innScoreBoardScreen)

  actualInn=1

  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=3)
  Label(ScoreBoardScreen,image=innScoreBoardScreen, bg='white').grid(row=0, column=4, rowspan=2)
  Label(ScoreBoardScreen,text=actualInn, bg='white').grid(row=2, column=4)

  #Bases
  Bases="Cuadro0"
  global imgBases
  imgBases=Image.open("img/" + Bases + ".jpg")
  imgBases=imgBases.resize((60,60),Image.ANTIALIAS)
  imgBases=ImageTk.PhotoImage(imgBases)
  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=5)
  Label(ScoreBoardScreen,image=imgBases, bg='white').grid(row=0, column=6, rowspan=5)

  #Out/Bola/Strike
  global Out
  Out=0
  global Bola
  Bola=0
  global Strike
  Strike=0

  global imgOut
  imgOut=Image.open("img/Out"+ str(Out) + ".jpg")
  imgOut=imgOut.resize((30,15),Image.ANTIALIAS)
  imgOut=ImageTk.PhotoImage(imgOut)

  global imgBola
  imgBola=Image.open("img/Bola"+ str(Bola) + ".jpg")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)

  global imgStrike
  imgStrike=Image.open("img/Strike"+ str(Strike) + ".jpg")
  imgStrike=imgStrike.resize((30,15),Image.ANTIALIAS)
  imgStrike=ImageTk.PhotoImage(imgStrike)

  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=7)
  Label(ScoreBoardScreen,text="Out", justify="left", font=("Calibri",12), bg='white').grid(row=1, column=8)
  Label(ScoreBoardScreen,image=imgOut, bg='white').grid(row=1, column=9)
  Label(ScoreBoardScreen,text="Bola", justify="left", font=("Calibri",12), bg='white').grid(row=2, column=8)
  Label(ScoreBoardScreen,image=imgBola, bg='white').grid(row=2, column=9)
  Label(ScoreBoardScreen,text="Strike", justify="left" , font=("Calibri",12), bg='white').grid(row=3, column=8)
  Label(ScoreBoardScreen,image=imgStrike, bg='white').grid(row=3, column=9)

  #prueba
  Label(ScoreBoardScreen,text="0 - 0", justify="left", font=("Calibri",12), bg='white').grid(row=5, column=1)

def addOut(): #add or remove Outs
  global Out
  if Out ==2:
    Out=0
  else:
    Out=Out+1
  global imgOut
  imgOut=Image.open("img/Out"+ str(Out) + ".jpg")
  imgOut=imgOut.resize((30,15),Image.ANTIALIAS)
  imgOut=ImageTk.PhotoImage(imgOut)
  Label(ScoreBoardScreen,image=imgOut, bg='white').grid(row=1, column=9)

def addBola(): #add or remove Bola
  global Bola
  if Bola ==3:
    Bola=0
  else:
    Bola=Bola+1

  global imgBola
  imgBola=Image.open("img/Bola"+ str(Bola) + ".jpg")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)
  Label(ScoreBoardScreen,image=imgBola, bg='white').grid(row=2, column=9)

def addStrike():
  global Strike
  if Strike ==2:
    Strike=0
  else:
    Strike=Strike+1

  global imgStrike
  imgStrike=Image.open("img/Strike"+ str(Strike) + ".jpg")
  imgStrike=imgStrike.resize((30,15),Image.ANTIALIAS)
  imgStrike=ImageTk.PhotoImage(imgStrike)
  Label(ScoreBoardScreen,image=imgStrike, bg='white').grid(row=3, column=9)

def addRunAway():
  global RunsAway
  global incdec
  if incdec.get()==1:
    RunsAway=RunsAway+1
  else:
    RunsAway=RunsAway-1
  Label(ScoreBoardScreen,text=RunsAway, font=("Calibri",12), bg='white').grid(row=0, column=2, rowspan=2)
  
def addRunHome(): 
  global RunsHome
  global incdec
  if incdec.get()==1:
    RunsHome=RunsHome+1
  else:
    RunsHome=RunsHome-1
  Label(ScoreBoardScreen,text=RunsHome, font=("Calibri",12), bg='white').grid(row=3, column=2, rowspan=2)

def bases(): #Actualizamos las bases
  global imgBases
  global Primera
  global Segunda
  global Tercera
  Bases=""
  if Primera.get()==1:
    Bases="1"
  if Segunda.get()==1:
    Bases=Bases+"2"
  if Tercera.get()==1:
    Bases=Bases+"3"
  if Bases=="":
    Bases="0"
  imgBases=Image.open("img/Cuadro" + Bases + ".jpg")
  imgBases=imgBases.resize((60,60),Image.ANTIALIAS)
  imgBases=ImageTk.PhotoImage(imgBases)
  Label(ScoreBoardScreen,image=imgBases, bg='white').grid(row=0, column=6, rowspan=5)

def inning():
  global innBot
  global innTop
  innTop=""
  innBot=""
  Label(ScoreBoardScreen,image=innTop, bg='white').grid(row=0, column=4, rowspan=2)
  if topbot.get()==0:
    innTop=Image.open("logo/Arrow top.png")
    innTop=innTop.resize((15,15),Image.ANTIALIAS)
    innTop=ImageTk.PhotoImage(innTop)
    innBot=""
  else:
    innBot=Image.open("logo/Arrow Bot.png")
    innBot=innBot.resize((15,15),Image.ANTIALIAS)
    innBot=ImageTk.PhotoImage(innBot)
    innTop=""

  actualInn=currentInning.get()
  
  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=3)
  Label(ScoreBoardScreen,image=innTop, bg='white').grid(row=0, column=4, rowspan=2)
  Label(ScoreBoardScreen,text=actualInn, bg='white').grid(row=2, column=4)
  Label(ScoreBoardScreen,image=innBot, bg='white').grid(row=3, column=4, rowspan=2)

root=Tk()
root.title("CB Barcelona Scoreboard")
#root.iconbitmap("logo/Barcelona.jpg")
root.resizable(0,0) #Ancho, Alto (1 se puede 0 no se puede)
root.geometry("350x300")

#Lanzamos pantalla del ScoreBoard
ScoreBoardScreen=""
scoreboard()

#Botones Strike/Bola/Out
Button(root,text="Strike", command=addStrike).grid(row=0,column=0, padx=2, pady=5)
Button(root,text="Bola", command=addBola).grid(row=0,column=1, padx=2, pady=5)
Button(root,text="Out", command=addOut).grid(row=0,column=2, padx=2, pady=5)

#Botones Carreras
Button(root,text="Run Away", command=addRunAway).grid(row=1,column=0, padx=2, pady=5, columnspan=2)
Button(root,text="Run Local", command=addRunHome).grid(row=1,column=2, padx=2, pady=5, columnspan=2)

#Corredores en las bases
Primera=IntVar()
Segunda=IntVar()
Tercera=IntVar()

Checkbutton(root,text="Primera", variable=Primera).grid(row=2,column=0, padx=2, pady=5)
Checkbutton(root,text="Segunda", variable=Segunda).grid(row=2,column=1, padx=2, pady=5)
Checkbutton(root,text="Tercera", variable=Tercera).grid(row=2,column=2, padx=2, pady=5)
Button(root,text="Update Bases", command=bases).grid(row=2,column=3, padx=2, pady=5)

#inning
currentInning=IntVar()
currentInning.set(1)
OptionMenu(root,currentInning,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20).grid(row=3,column=0, padx=2, pady=5)

topbot=IntVar()
Radiobutton(root, text="Top", variable=topbot, value=0).grid(row=3,column=1, padx=2, pady=5)
Radiobutton(root, text="Bot", variable=topbot, value=1).grid(row=3,column=2, padx=2, pady=5)
Button(root,text="Update Inning", command=inning).grid(row=3,column=3, padx=2, pady=5)

#Botores para incrementar o reducir
incdec=IntVar()
incdec.set(1) #Marcamos Increment por defecto al ejecutar
Radiobutton(root, text="Increment", variable=incdec, value=1).grid(row=4,column=0, padx=2, pady=5)
Radiobutton(root, text="Descent", variable=incdec, value=0).grid(row=4,column=1, padx=2, pady=5)

root.mainloop()