from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import time

def scoreboard(): #ventana del scoreboard, lo que se muestra en la retrasmisión
  global ScoreBoardScreen
  ScoreBoardScreen=Toplevel()
  ScoreBoardScreen.resizable(0,0) 
  ScoreBoardScreen.geometry("312x95")
  ScoreBoardScreen.configure(bg='white')
  ScoreBoardScreen.iconbitmap("logo/Barcelona.ico")
  #ScoreBoardScreen.overrideredirect(True) #Eliminamos el title bar

  #FrameAway
  global frameAway
  frameAway=Frame(ScoreBoardScreen,bg="#00417e", padx=10, pady=5)
  frameAway.grid(row=0, column=0, rowspan=2)

  #FrameHome
  global frameHome
  frameHome=Frame(ScoreBoardScreen,bg="#a50032", padx=10, pady=5)
  frameHome.grid(row=2, column=0, rowspan=2)

  #Score
  global RunsAway
  RunsAway=0
  global RunsHome
  RunsHome=0

  Label(frameAway,text=RunsAway, font=("Calibri",12,"bold"), bg='#00417e', fg="white", width=2).grid(row=0, column=2, rowspan=2)
  Label(frameHome,text=RunsHome, font=("Calibri",12,"bold"), bg="#a50032", fg="white", width=2).grid(row=0, column=2, rowspan=2)

  #Bases
  Bases="Cuadro0"
  global imgBases
  imgBases=Image.open("img/" + Bases + ".png")
  imgBases=imgBases.resize((80,54),Image.ANTIALIAS)
  imgBases=ImageTk.PhotoImage(imgBases)
  #Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=5)
  Label(ScoreBoardScreen,image=imgBases, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)

  #Inning
  global innScoreBoardScreen
  innScoreBoardScreen=Image.open("img/Arrow top.png")
  innScoreBoardScreen=innScoreBoardScreen.resize((15,15),Image.ANTIALIAS)
  innScoreBoardScreen=ImageTk.PhotoImage(innScoreBoardScreen)

  actualInn=1

  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=3)
  Label(ScoreBoardScreen,image=innScoreBoardScreen, bg='white').grid(row=0, column=8)
  Label(ScoreBoardScreen,text=actualInn, bg='white').grid(row=0, column=9)

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

def selectteam(): #Se abre una nueva ventana para seleccionar equipo. Antes de seleccionar pedira si quieres eliminar todos los datos del marcador
  def confirmteam(): #función del botón confirm team
    #AWAY
    global logoAway
    global logoAwayRez
    if AwayTeam.get()=="Antorcha":
      shortname="ANT"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Astros":
      shortname="AST"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Barcelona":
      shortname="BCN"
      logo="logo/Barcelona.png"
    elif AwayTeam.get()=="Marlins":
      shortname="MAR"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Marlins":
      shortname="MAR"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Miralbueno":
      shortname="MIR"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Navarra":
      shortname="NAV"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Rivas":
      shortname="RIV"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="San Inazio":
      shortname="SnI"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Sant Boi":
      shortname="StB"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Viladecans":
      shortname="VIL"
      logo="logo/Gava.png"
    logoAway=Image.open(logo)
    logoAwayRez=logoAway.resize((25,25),Image.ANTIALIAS)
    logoAwayRez=ImageTk.PhotoImage(logoAwayRez)
    Label(frameAway,image=logoAwayRez, bg="#00417e").grid(row=0, column=0, padx=1, pady=5)
    Label(frameAway,text=shortname, font=("Calibri",12,"bold"), bg="#00417e", fg='white', width=4).grid(row=0, column=1, padx=1,pady=1)

    #HOME
    global logoHome
    global logoHomeRez
    if HomeTeam.get()=="Antorcha":
      shortname="ANT"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Astros":
      shortname="AST"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Barcelona":
      shortname="BCN"
      logo="logo/Barcelona.png"
    elif HomeTeam.get()=="Marlins":
      shortname="MAR"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Marlins":
      shortname="MAR"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Miralbueno":
      shortname="MIR"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Navarra":
      shortname="NAV"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Rivas":
      shortname="RIV"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="San Inazio":
      shortname="SnI"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Sant Boi":
      shortname="StB"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Viladecans":
      shortname="VIL"
      logo="logo/Gava.png"
    
    logoHome=Image.open(logo)
    logoHomeRez=logoHome.resize((25,25),Image.ANTIALIAS)
    logoHomeRez=ImageTk.PhotoImage(logoHomeRez)
    Label(frameHome,image=logoHomeRez, bg='#a50032').grid(row=0, column=0, padx=1, pady=5)
    Label(frameHome,text=shortname, font=("Calibri",12,"bold"), bg='#a50032', fg='white', width=4).grid(row=0, column=1,padx=1,pady=1)

    SelectTeamScreen.destroy()
  
  valor=messagebox.askquestion("Selección equipos","Esta acción pondrá el marcador a cero. Desea continuar?")
  if valor=="yes":
    #Inicializamos todo el marcador
    #Hits
    global HitsAway
    HitsAway=0
    global HitsHome
    HitsHome=0

    #Errors
    global ErrorsAway
    ErrorsAway=0
    global ErrorsHome
    ErrorsHome=0

    #carreras
    RunsAway=0
    RunsHome=0
    Label(frameAway,text=RunsAway, font=("Calibri",12,"bold"), bg='#00417e', fg="white", width=2).grid(row=0, column=2, rowspan=2)
    Label(frameHome,text=RunsHome, font=("Calibri",12,"bold"), bg="#a50032", fg="white", width=2).grid(row=0, column=2, rowspan=2)
    #innings
    global innImg
    innImg=Image.open("img/Arrow top.png")
    innImg=innImg.resize((15,15),Image.ANTIALIAS)
    innImg=ImageTk.PhotoImage(innImg)
    Label(ScoreBoardScreen,image=innImg, bg='white').grid(row=0, column=8)
    Label(ScoreBoardScreen,text=1, bg='white').grid(row=0, column=9)
    topbot.set(0)
    currentInning.set(1)

    #abrimos la ventana para seleccionar equipos
    SelectTeamScreen=Toplevel()
    SelectTeamScreen.resizable(0,0) 
    SelectTeamScreen.geometry("150x150")
    SelectTeamScreen.configure(bg='white')
    SelectTeamScreen.iconbitmap("logo/Barcelona.ico")
    
    AwayTeam=StringVar()
    HomeTeam=StringVar()
    HomeTeam.set("Barcelona")
    Label(SelectTeamScreen,text="Away", bg='white').grid(row=0, column=0, padx=2, pady=5)
    OptionMenu(SelectTeamScreen,AwayTeam,"Antorcha","Astros","Barcelona","Marlins","Miralbueno","Navarra","Rivas","San Inazio","Sant Boi", "Viladecans").grid(row=0,column=1, padx=2, pady=5)
    Label(SelectTeamScreen,text="Home", bg='white').grid(row=1, column=0,padx=2, pady=5)
    OptionMenu(SelectTeamScreen,HomeTeam,"Antorcha","Astros","Barcelona","Marlins","Miralbueno","Navarra","Rivas","San Inazio","Sant Boi", "Viladecans").grid(row=1,column=1, padx=2, pady=5)
    Button(SelectTeamScreen,text="Confirmar equipos", command=confirmteam).grid(row=2,column=0, columnspan=2, padx=2, pady=5)

def addOut(): #añade o quita Outs
  global Out
  global incdec
  if incdec.get()==1:
    if Out ==2:
      response=messagebox.askyesno("Nuevo inning", "Está seguro que quiere finalizar el inning?")
      if response==1:
        Out=0
        if topbot.get()==0: #Si estamos en top pasamos a bot
          topbot.set(1)
          inning()
        else: #si estamos en bot pasamos a siguiente imning
          topbot.set(0) 
          nextInning=currentInning.get()+1
          currentInning.set(nextInning)
          inning()

      else:
        Out=2
    else:
      Out=Out+1
  else:
    if Out ==0:
      Out=0
    else:
      Out=Out-1
  global imgOut
  imgOut=Image.open("img/Out"+ str(Out) + ".jpg")
  imgOut=imgOut.resize((30,15),Image.ANTIALIAS)
  imgOut=ImageTk.PhotoImage(imgOut)
  Label(ScoreBoardScreen,image=imgOut, bg='white').grid(row=1, column=9)
  resetStrikeBola()

def resetStrikeBola():#ponemos a 0 las bolas y los strikes 
  global Strike
  global imgStrike
  Strike=0
  imgStrike=Image.open("img/Strike"+ str(Strike) + ".jpg")
  imgStrike=imgStrike.resize((30,15),Image.ANTIALIAS)
  imgStrike=ImageTk.PhotoImage(imgStrike)
  Label(ScoreBoardScreen,image=imgStrike, bg='white').grid(row=3, column=9)
  global Bola
  Bola=0
  global imgBola
  imgBola=Image.open("img/Bola"+ str(Bola) + ".jpg")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)
  Label(ScoreBoardScreen,image=imgBola, bg='white').grid(row=2, column=9)

def addBola(): #añade o quita Bolas
  global Bola
  global incdec
  if incdec.get()==1:
    if Bola ==3:
      resetStrikeBola()
      #comprobaremos las bases para añadir corredores para añadir corredores
      if Primera.get()==0 and Segunda.get()==0:
        Primera.set(1)
      elif Primera.get()==1 and Segunda.get()==0:
        Segunda.set(1)
      elif Primera.get()==1 and Segunda.get()==1 and Tercera.get()==0:
        Tercera.set(1)
      bases()
    else:
      Bola=Bola+1
  else:
    if Bola ==0:
      Bola=0
    else:
      Bola=Bola-1

  global imgBola
  imgBola=Image.open("img/Bola"+ str(Bola) + ".jpg")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)
  Label(ScoreBoardScreen,image=imgBola, bg='white').grid(row=2, column=9)

def addStrike():
  global Strike
  global incdec
  if incdec.get()==1:
    if Strike ==2:
      resetStrikeBola()
      addOut()
    else:
      Strike=Strike+1
  else:
    if Strike==0:
      Strike=0
    else:
      Strike=Strike-1

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
  Label(frameAway,text=RunsAway, font=("Calibri",12,"bold"), bg='#00417e', fg="white", width=2).grid(row=0, column=2, rowspan=2)
  
def addRunHome(): 
  global RunsHome
  global incdec
  if incdec.get()==1:
    RunsHome=RunsHome+1
  else:
    RunsHome=RunsHome-1
  Label(frameHome,text=RunsHome, font=("Calibri",12,"bold"), bg="#a50032", fg="white", width=2).grid(row=0, column=2, rowspan=2)

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
  imgBases=Image.open("img/Cuadro" + Bases + ".png")
  imgBases=imgBases.resize((80,54),Image.ANTIALIAS)
  imgBases=ImageTk.PhotoImage(imgBases)
  Label(ScoreBoardScreen,image=imgBases, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)

def inning():
  global innImg
  if topbot.get()==0:
    innImg=Image.open("img/Arrow top.png")
    innImg=innImg.resize((15,15),Image.ANTIALIAS)
    innImg=ImageTk.PhotoImage(innImg)
  else:
    innImg=Image.open("img/Arrow Bot.png")
    innImg=innImg.resize((15,15),Image.ANTIALIAS)
    innImg=ImageTk.PhotoImage(innImg)

  actualInn=currentInning.get()
  
  Label(ScoreBoardScreen,image=innImg, bg='white').grid(row=0, column=8)
  Label(ScoreBoardScreen,text=actualInn, bg='white').grid(row=0, column=9)

def hit():
  global hitgif
  global HitsAway
  global HitsHome
  if incdec.get()==1: #Función de incrementar 
    for i in range(2): #Animación de hit     
      for j in range (16):
        hitgif=Image.open("img/Hit/hit"+str(j)+".png")
        hitgif=ImageTk.PhotoImage(hitgif)
        Label(ScoreBoardScreen,image=hitgif, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)
        ScoreBoardScreen.update()
        time.sleep(0.05)

      if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
        imgBases=logoAway.resize((80,80),Image.ANTIALIAS)
      else:
        imgBases=logoHome.resize((80,80),Image.ANTIALIAS)
      imgBases=ImageTk.PhotoImage(imgBases, format="gif -index 0")
      Label(ScoreBoardScreen,image=imgBases, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(0.5)

    #Muestra el número de hits en el partido

    if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      HitsAway=HitsAway+1
      Label(ScoreBoardScreen,text="Hits:", bg='white', font=("Calibri",12)).grid(row=1, column=4, columnspan=2)
      Label(ScoreBoardScreen,text=HitsAway, bg='white', font=("Calibri",12)).grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)
    else:
      HitsHome=HitsHome+1
      Label(ScoreBoardScreen,text="Hits:", bg='white', font=("Calibri",12)).grid(row=1, column=4, columnspan=2)
      Label(ScoreBoardScreen,text=HitsHome, bg='white', font=("Calibri",12)).grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)
  
    bases() #actualizamos las bases
  else: #Función de decrementar
    if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      if HitsAway==0:
        HitsAway=0
      else:
        HitsAway=HitsAway-1
    else:
      if HitsHome==0:
        HitsHome=0
      else:
        HitsHome=HitsHome-1
def error():
  global errorgif
  global img1
  global img2
  global ErrorsAway
  global ErrorsHome
  if incdec.get()==1: #Función de incrementar
    
    for j in range (7):
        errorgif=Image.open("img/Error/error"+str(j)+".png")
        errorgif=ImageTk.PhotoImage(errorgif)
        Label(ScoreBoardScreen,image=errorgif, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)
        ScoreBoardScreen.update()
        time.sleep(0.1)

    img1=Image.open("img/error.png")
    img1=img1.resize((80,80),Image.ANTIALIAS)
    img1=ImageTk.PhotoImage(img1)

    img2=Image.open("img/error2.png")
    img2=img2.resize((80,80),Image.ANTIALIAS)
    img2=ImageTk.PhotoImage(img2)
    
    for i in range(2): #Animación de Error
      Label(ScoreBoardScreen,image=img1, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(0.15)
      Label(ScoreBoardScreen,image=img2, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(0.3)

      if topbot.get()==1: #el error mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
        imgBases=logoAway.resize((80,80),Image.ANTIALIAS)
      else:
        imgBases=logoHome.resize((80,80),Image.ANTIALIAS)
      imgBases=ImageTk.PhotoImage(imgBases, format="gif -index 0")
      Label(ScoreBoardScreen,image=imgBases, bg='white').grid(row=0, column=4, rowspan=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(0.5)

    #Muestra el número de errors en el partido

    if topbot.get()==1: #el error mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      ErrorsAway=ErrorsAway+1
      Label(ScoreBoardScreen,text="Errores:", bg='white', font=("Calibri",12)).grid(row=1, column=4, columnspan=2)
      Label(ScoreBoardScreen,text=ErrorsAway, bg='white', font=("Calibri",12)).grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)
    else:
      ErrorsHome=ErrorsHome+1
      Label(ScoreBoardScreen,text="Errores:", bg='white', font=("Calibri",12)).grid(row=1, column=4, columnspan=2)
      Label(ScoreBoardScreen,text=ErrorsHome, bg='white', font=("Calibri",12)).grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)

    bases() #actualizamos las bases

  else: #Función de decrementar
    if topbot.get()==1: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      if ErrorsAway==0:
        ErrorsAway=0
      else:
        ErrorsAway=ErrorsAway-1
    else:
      if ErrorsHome==0:
        ErrorsHome=0
      else:
        ErrorsHome=ErrorsHome-1

#funciones del menu bar de la root:
def exitMsg(): #Código del botón del Menu File->Exit
    valor=messagebox.askquestion("Exit","Está seguro que quiere cerrar?")
    if valor=="yes":
        ScoreBoardScreen.destroy()
        root.destroy()

def aboutMsg():
  messagebox.showinfo("About","Creado para el CB Barcelona")

root=Tk()
root.title("CBS Barcelona Scoreboard")
root.iconbitmap("logo/Barcelona.ico")
root.resizable(0,0) #Ancho, Alto (1 se puede 0 no se puede)
root.geometry("350x400")

#Menu Bar
barraMenu=Menu(root)
root.config(menu=barraMenu)

fileMenu=Menu(barraMenu,tearoff=0)
fileMenu.add_command(label="Seleccionar equipos", command=selectteam)
fileMenu.add_command(label="About", command=aboutMsg)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exitMsg)
barraMenu.add_cascade(label="File",menu=fileMenu)

#Hero image
img=Image.open("logo/Hero.png")
img=img.resize((350,90),Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
Label(root,image=img, bg='white').grid(row=0, column=0, columnspan=4)

#Botones Strike/Bola/Out
Button(root,text="Strike", command=addStrike, width=7).grid(row=1,column=0, padx=5, pady=10)
Button(root,text="Bola", command=addBola , width=7).grid(row=1,column=1, padx=5, pady=10)
Button(root,text="Out", command=addOut, width=7).grid(row=1,column=2, padx=5, pady=10)

#botones hit/error
Button(root,text="Hit", command=hit, width=7).grid(row=2,column=0, padx=5, pady=15)
Button(root,text="Error", command=error, width=7).grid(row=2,column=1, padx=5, pady=15)

#Botones Carreras
Button(root,text="Run Away", command=addRunAway, width=7).grid(row=3,column=0, padx=5, pady=10)
Button(root,text="Run Local", command=addRunHome, width=7).grid(row=3,column=1, padx=5, pady=10)

#Corredores en las bases
Primera=IntVar()
Segunda=IntVar()
Tercera=IntVar()

Checkbutton(root,text="Primera", variable=Primera).grid(row=4,column=0, padx=5, pady=10)
Checkbutton(root,text="Segunda", variable=Segunda).grid(row=4,column=1, padx=5, pady=10)
Checkbutton(root,text="Tercera", variable=Tercera).grid(row=4,column=2, padx=5, pady=10)
Button(root,text="Update Bases", command=bases).grid(row=4,column=3, padx=2, pady=10)

ttk.Separator(root,orient='horizontal').grid(row=5,column=0, sticky="ew", columnspan=4)

#inning
currentInning=IntVar()
currentInning.set(1)
OptionMenu(root,currentInning,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20).grid(row=6,column=0, padx=5, pady=10)

topbot=IntVar() #0 en caso de Away, 1 en caso de Home
Radiobutton(root, text="Top", variable=topbot, value=0).grid(row=6,column=1, padx=2, pady=10) 
Radiobutton(root, text="Bot", variable=topbot, value=1).grid(row=6,column=2, padx=2, pady=10)
Button(root,text="Update Inning", command=inning).grid(row=6,column=3, padx=2, pady=10)

#Botores para incrementar o reducir
incdec=IntVar()
incdec.set(1) #Marcamos Increment por defecto al ejecutar
Radiobutton(root, text="Increment", variable=incdec, value=1).grid(row=7,column=0, padx=2, pady=10)
Radiobutton(root, text="Descent", variable=incdec, value=0).grid(row=7,column=1, padx=2, pady=10)

#Lanzamos pantalla del ScoreBoard
ScoreBoardScreen=""
frameAway=""
frameHome=""
root.after(10, scoreboard)
root.mainloop()