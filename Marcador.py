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
  ScoreBoardScreen.geometry("314x124+50+50")
  ScoreBoardScreen.title("CBS Barcelona Scoreboard")
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
  global RunsAwayLabel
  global RunsHomeLabel
  RunsAwayLabel=Label(frameAway,text=RunsAway, font=("Calibri",12,"bold"), bg='#00417e', fg="white", width=2)
  RunsAwayLabel.grid(row=0, column=2, rowspan=2)
  RunsHomeLabel=Label(frameHome,text=RunsHome, font=("Calibri",12,"bold"), bg="#a50032", fg="white", width=2)
  RunsHomeLabel.grid(row=0, column=2, rowspan=2)

  #At bat
  global atbatLabel
  atbatLabel=Label(ScoreBoardScreen,text="A/B: 1º #26 Víctor Cuevas", font=("Calibri",12,"bold"), bg='#00417e',width=28, fg="white", anchor='w')
  atbatLabel.grid(row=5, column=0, columnspan=7)

  #Bases
  global BasesLabel
  Bases="Cuadro0"
  global imgBases
  imgBases=Image.open("img/" + Bases + ".png")
  imgBases=imgBases.resize((80,54),Image.ANTIALIAS)
  imgBases=ImageTk.PhotoImage(imgBases)
  #Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=5)
  BasesLabel=Label(ScoreBoardScreen,image=imgBases, bg='white')
  BasesLabel.grid(row=0, column=4, rowspan=4, columnspan=2)

  #Inning
  global innScoreBoardScreen
  global topbotInnLabel
  global actualInnLabel
  innScoreBoardScreen=Image.open("img/Arrow top.png")
  innScoreBoardScreen=innScoreBoardScreen.resize((15,15),Image.ANTIALIAS)
  innScoreBoardScreen=ImageTk.PhotoImage(innScoreBoardScreen)

  actualInn=1

  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=3)
  topbotInnLabel=Label(ScoreBoardScreen,image=innScoreBoardScreen, bg='white')
  topbotInnLabel.grid(row=0, column=7)
  actualInnLabel=Label(ScoreBoardScreen,text=actualInn, bg='white')
  actualInnLabel.grid(row=0, column=8)

  #Out/Bola/Strike
  global imgOutLabel
  global imgBolaLabel
  global imgStrikeLabel
  global Out
  Out=0
  global Bola
  Bola=0
  global Strike
  Strike=0

  global imgOut
  imgOut=Image.open("img/Out"+ str(Out) + ".png")
  imgOut=imgOut.resize((30,15),Image.ANTIALIAS)
  imgOut=ImageTk.PhotoImage(imgOut)

  global imgBola
  imgBola=Image.open("img/Bola"+ str(Bola) + ".png")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)

  global imgStrike
  imgStrike=Image.open("img/Strike"+ str(Strike) + ".png")
  imgStrike=imgStrike.resize((30,15),Image.ANTIALIAS)
  imgStrike=ImageTk.PhotoImage(imgStrike)

  Label(ScoreBoardScreen,text="   ", bg='white').grid(row=1, column=6)
  Label(ScoreBoardScreen,text="Out", justify="left", font=("Calibri",12), bg='white').grid(row=1, column=7)
  imgOutLabel=Label(ScoreBoardScreen,image=imgOut, bg='white')
  imgOutLabel.grid(row=1, column=8)
  Label(ScoreBoardScreen,text="Bola", justify="left", font=("Calibri",12), bg='white').grid(row=2, column=7)
  imgBolaLabel=Label(ScoreBoardScreen,image=imgBola, bg='white')
  imgBolaLabel.grid(row=2, column=8)
  Label(ScoreBoardScreen,text="Strike", justify="left" , font=("Calibri",12), bg='white').grid(row=3, column=7)
  imgStrikeLabel=Label(ScoreBoardScreen,image=imgStrike, bg='white')
  imgStrikeLabel.grid(row=3, column=8)

  ScoreBoardScreen.protocol("WM_DELETE_WINDOW", on_closing)

def selectteam(): #Se abre una nueva ventana para seleccionar equipo. Antes de seleccionar pedira si quieres eliminar todos los datos del marcador
  def confirmteam(): #función del botón confirm team
    #AWAY
    global logoAway
    global logoAwayRez
    global awayTeamName
    global homeTeamName
    if AwayTeam.get()=="Antorcha":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Antorcha"
      shortname="ANT"
      logo="logo/Antorcha.png"
    elif AwayTeam.get()=="Astros":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CB Astros Valencia"
      shortname="AST"
      logo="logo/astros.png"
    elif AwayTeam.get()=="Barcelona":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Barcelona"
      shortname="BCN"
      logo="logo/Barcelona.png"
    elif AwayTeam.get()=="Gava":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Gava"
      shortname="GAV"
      logo="logo/Gava.png"
    elif AwayTeam.get()=="Marlins":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="Tenerife Marlins PC"
      shortname="MAR"
      logo="logo/marlins.png"
    elif AwayTeam.get()=="Miralbueno":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Miralbueno"
      shortname="MIR"
      logo="logo/miralbueno.png"
    elif AwayTeam.get()=="Navarra":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="Béisbol Navarra"
      shortname="NAV"
      logo="logo/Navarra.png"
    elif AwayTeam.get()=="Rivas":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Rivas"
      shortname="RIV"
      logo="logo/Rivas.png"
    elif AwayTeam.get()=="San Inazio":
      awayTeamName=AwayTeam.get()
      awayTeamLongName=HomeTeam.get()
      shortname="SnI"
      logo="logo/san_inazio.png"
    elif AwayTeam.get()=="Sant Boi":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Sant Boi"
      shortname="StB"
      logo="logo/santboi.png"
    elif AwayTeam.get()=="Toros":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CBS Toros"
      shortname="TOR"
      logo="logo/toros.png"
    elif AwayTeam.get()=="Viladecans":
      awayTeamName=AwayTeam.get()
      awayTeamLongName="CB Viladecans"
      shortname="VIL"
      logo="logo/viladecans.png"
    logoAway=Image.open(logo)
    logoAwayRez=logoAway.resize((25,25),Image.ANTIALIAS)
    logoAwayRez=ImageTk.PhotoImage(logoAwayRez)
    Label(frameAway,image=logoAwayRez, bg="#00417e").grid(row=0, column=0, padx=1, pady=5)
    Label(frameAway,text=shortname, font=("Calibri",12,"bold"), bg="#00417e", fg='white', width=4).grid(row=0, column=1, padx=1,pady=1)
    
    #HOME
    global logoHome
    global logoHomeRez
    if HomeTeam.get()=="Antorcha":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Antorcha"
      shortname="ANT"
      logo="logo/Antorcha.png"
    elif HomeTeam.get()=="Astros":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CB Astros Valencia"
      shortname="AST"
      logo="logo/astros.png"
    elif HomeTeam.get()=="Barcelona":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Barcelona"
      shortname="BCN"
      logo="logo/Barcelona.png"
    elif HomeTeam.get()=="Gava":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Gava"
      shortname="GAV"
      logo="logo/Gava.png"
    elif HomeTeam.get()=="Marlins":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="Tenerife Marlins PC"
      shortname="MAR"
      logo="logo/marlins.png"
    elif HomeTeam.get()=="Miralbueno":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Miralbueno"
      shortname="MIR"
      logo="logo/miralbueno.png"
    elif HomeTeam.get()=="Navarra":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="Béisbol Navarra"
      shortname="NAV"
      logo="logo/Navarra.png"
    elif HomeTeam.get()=="Rivas":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Rivas"
      shortname="RIV"
      logo="logo/Rivas.png"
    elif HomeTeam.get()=="San Inazio":
      homeTeamName=HomeTeam.get()
      homeTeamLongName=HomeTeam.get()
      shortname="SnI"
      logo="logo/san_inazio.png"
    elif HomeTeam.get()=="Sant Boi":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Viladecans"
      shortname="StB"
      logo="logo/santboi.png"
    elif HomeTeam.get()=="Toros":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CBS Toros"
      shortname="TOR"
      logo="logo/toros.png"
    elif HomeTeam.get()=="Viladecans":
      homeTeamName=HomeTeam.get()
      homeTeamLongName="CB Viladecans"
      shortname="VIL"
      logo="logo/viladecans.png"
    logoHome=Image.open(logo)
    logoHomeRez=logoHome.resize((25,25),Image.ANTIALIAS)
    logoHomeRez=ImageTk.PhotoImage(logoHomeRez)
    Label(frameHome,image=logoHomeRez, bg='#a50032').grid(row=0, column=0, padx=1, pady=5)
    Label(frameHome,text=shortname, font=("Calibri",12,"bold"), bg='#a50032', fg='white', width=4).grid(row=0, column=1,padx=1,pady=1)

    marcadorInningsAwayTeam.config(text=awayTeamLongName)
    marcadorInningsHomeTeam.config(text=homeTeamLongName)

    updateHitterOverview()
    SelectTeamScreen.destroy()

  
  valor=messagebox.askquestion("Selección equipos","Esta acción pondrá el marcador a cero. Desea continuar?")
  if valor=="yes":
    #Inicializamos todo el marcador
    #Hits
    global HitsAway
    HitsAway=0
    global HitsHome
    HitsHome=0
    #at bat
    global atbatAway
    atbatAway=0
    global atbatHome
    atbatHome=0
    #At Bat
    textatbat="A/B: " + str(atbatAway+1) +"º #"+ str(AwayNum[atbatAway]) + " "+ AwayName[atbatAway]
    atbatLabel.config(text = textatbat)

    #Errors
    global ErrorsAway
    ErrorsAway=0
    global ErrorsHome
    ErrorsHome=0

    #carreras
    RunsAway=0
    RunsHome=0
    RunsAwayLabel.config(text=str(RunsAway))
    RunsHomeLabel.config(text=str(RunsHome))
    #innings
    global innImg
    innImg=Image.open("img/Arrow top.png")
    innImg=innImg.resize((15,15),Image.ANTIALIAS)
    innImg=ImageTk.PhotoImage(innImg)
    topbot.set(0)
    currentInning.set(1)
    actualInnLabel.config(text=1)
    topbotInnLabel.config(image=innImg)

    #strike/bolas/outs
    global imgOut
    imgOut=Image.open("img/Out0.png")
    imgOut=imgOut.resize((30,15),Image.ANTIALIAS)
    imgOut=ImageTk.PhotoImage(imgOut)
    imgOutLabel.config(image=imgOut)
    resetStrikeBola()

    #abrimos la ventana para seleccionar equipos
    SelectTeamScreen=Toplevel()
    SelectTeamScreen.resizable(0,0) 
    SelectTeamScreen.geometry("150x150+400+200")
    SelectTeamScreen.configure(bg='white')
    SelectTeamScreen.iconbitmap("logo/Barcelona.ico")
    
    AwayTeam=StringVar()
    HomeTeam=StringVar()
    HomeTeam.set("Barcelona")
    Label(SelectTeamScreen,text="Away", bg='white').grid(row=0, column=0, padx=2, pady=5)
    OptionMenu(SelectTeamScreen,AwayTeam,"Antorcha","Astros","Barcelona","Gava","Marlins","Miralbueno","Navarra","Rivas","San Inazio","Sant Boi", "Toros", "Viladecans").grid(row=0,column=1, padx=2, pady=5)
    Label(SelectTeamScreen,text="Home", bg='white').grid(row=1, column=0,padx=2, pady=5)
    OptionMenu(SelectTeamScreen,HomeTeam,"Antorcha","Astros","Barcelona","Marlins","Miralbueno","Navarra","Rivas","San Inazio","Sant Boi", "Viladecans").grid(row=1,column=1, padx=2, pady=5)
    Button(SelectTeamScreen,text="Confirmar equipos", command=confirmteam).grid(row=2,column=0, columnspan=2, padx=2, pady=5)
    
def lineUp(): #Te deja añadir lineUp de los equipos
  def confirmlineup():
    i=0
    for entries in EntryAwayNumlist:
      AwayNum[i]=entries.get()
      i=i+1
    i=0
    for entries in EntryAwayNamlist:
      AwayName[i]=entries.get()
      i=i+1
    i=0
    for entries in EntryHomeNumlist:
      HomeNum[i]=entries.get()
      i=i+1
    i=0
    for entries in EntryHomeNamlist:
      HomeName[i]=entries.get()
      i=i+1

    #Actualizamos el current at Bat del equipo
    if topbot.get()==0:
      textatbat="A/B: " + str(atbatAway+1) +"º #"+ str(AwayNum[atbatAway]) + " "+ AwayName[atbatAway]
      atbatLabel.config(text = textatbat)
    else:
      textatbat="A/B: " + str(atbatHome+1) +"º #"+ str(HomeNum[atbatHome]) + " "+ HomeName[atbatHome]
      atbatLabel.config(text = textatbat)
    updateHitterOverview()
    LineUpScreen.destroy()

  #abrimos la ventana para seleccionar LineUp
  LineUpScreen=Toplevel()
  LineUpScreen.resizable(0,0) 
  LineUpScreen.geometry("350x400+400+200")
  LineUpScreen.configure(bg='white')
  LineUpScreen.iconbitmap("logo/Barcelona.ico")

  Label(LineUpScreen,text="Away",bg="white").grid(row=0,column=1, columnspan=2, padx=2, pady=5)
  Label(LineUpScreen,text="Num",bg="white").grid(row=1,column=1, pady=5)
  Label(LineUpScreen,text="Nombre",bg="white").grid(row=1,column=2, pady=5)
  Label(LineUpScreen,text="      ",bg="white").grid(row=1,column=3, pady=5)
  Label(LineUpScreen,text="Home",bg="white").grid(row=0,column=4, columnspan=2, padx=2, pady=5)
  Label(LineUpScreen,text="Num",bg="white").grid(row=1,column=4, pady=5)
  Label(LineUpScreen,text="Nombre",bg="white").grid(row=1,column=5, pady=5)
  
  EntryAwayNumlist=[]
  EntryAwayNamlist=[]
  EntryHomeNumlist=[]
  EntryHomeNamlist=[]
  for i in range(9):
    Label(LineUpScreen,text=i+1,bg="white").grid(row=i+2,column=0, pady=5)
    #Away numbers
    EntryAwayNum=Entry(LineUpScreen, bg="white", width=2)
    EntryAwayNum.delete(0,"end")
    EntryAwayNum.insert(0, AwayNum[i])
    EntryAwayNum.grid(row=i+2,column=1, pady=5)
    EntryAwayNumlist.append(EntryAwayNum)
    #Away names
    EntryAwayNam=Entry(LineUpScreen, bg="white", width=15)
    EntryAwayNam.delete(0,"end")
    EntryAwayNam.insert(0, AwayName[i])
    EntryAwayNam.grid(row=i+2,column=2, pady=5)
    EntryAwayNamlist.append(EntryAwayNam)
    #Home numbers
    EntryHomeNum=Entry(LineUpScreen, bg="white", width=2)
    EntryHomeNum.delete(0,"end")
    EntryHomeNum.insert(0, HomeNum[i])
    EntryHomeNum.grid(row=i+2,column=4, pady=5)
    EntryHomeNumlist.append(EntryHomeNum)
    #Home names
    EntryHomeNam=Entry(LineUpScreen, bg="white", width=15)
    EntryHomeNam.delete(0,"end")
    EntryHomeNam.insert(0, HomeName[i])
    EntryHomeNam.grid(row=i+2,column=5, pady=5)
    EntryHomeNamlist.append(EntryHomeNam)

  Button(LineUpScreen,text="Confirmar line up", command=confirmlineup).grid(row=13,column=0, columnspan=5, padx=2, pady=5)

def hitterOverview(): #se te abre ventana con la imagen del bateador
  global hitterOverviewScreen
  hitterOverviewScreen=Toplevel()
  hitterOverviewScreen.resizable(0,0) 
  hitterOverviewScreen.title("CBSB - Bateador")
  hitterOverviewScreen.geometry("900x172+50+490")
  hitterOverviewScreen.configure(bg='white')
  hitterOverviewScreen.iconbitmap("logo/Barcelona.ico")

  global imgHitter
  imgHitter=Image.open("logo/Barcelona/29.png")
  imgHitter=imgHitter.resize((900,172),Image.ANTIALIAS)
  imgHitter=ImageTk.PhotoImage(imgHitter)

  global imgHitterLabel
  imgHitterLabel=Label(hitterOverviewScreen,image=imgHitter, bg='white')
  imgHitterLabel.grid(row=0, column=0)

  hitterOverviewScreen.protocol("WM_DELETE_WINDOW", on_closing)

def updateHitterOverview(): #actualiza la ventana con la imagen del bateador
  global imgHitter
  try:
    if topbot.get()==0:
      dorsal=AwayNum[atbatAway]
      imgHitter=Image.open("logo/" + awayTeamName+"/"+ str(dorsal)+".png")
    else:
      dorsal=HomeNum[atbatHome]
      imgHitter=Image.open("logo/" + homeTeamName+"/"+ str(dorsal)+".png")

    imgHitter=imgHitter.resize((900,172),Image.ANTIALIAS)
    imgHitter=ImageTk.PhotoImage(imgHitter)
    imgHitterLabel.config(image=imgHitter)
  
  except:
    imgHitterLabel.config(image="")

def marcadorInnings(): #abre la ventana del marcador por innings
  global marcadorInningsScreen
  marcadorInningsScreen=Toplevel()
  marcadorInningsScreen.resizable(0,0) 
  marcadorInningsScreen.title("CBSB - Marcador innings")
  marcadorInningsScreen.geometry("500x70+50+700")
  marcadorInningsScreen.configure(bg='white')
  marcadorInningsScreen.iconbitmap("logo/Barcelona.ico")

  for i in range(9):
    Label(marcadorInningsScreen,text=str(i+1), bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3).grid(row=0, column=i+1)
  Label(marcadorInningsScreen,text="R", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3).grid(row=0, column=10)
  Label(marcadorInningsScreen,text="H", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3).grid(row=0, column=11)
  Label(marcadorInningsScreen,text="E", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3).grid(row=0, column=12)

  global marcadorInningsAwayTeam
  marcadorInningsAwayTeam=Label(marcadorInningsScreen,text="Team Away", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=20)
  marcadorInningsAwayTeam.grid(row=1, column=0)
  global marcadorInningsHomeTeam
  marcadorInningsHomeTeam=Label(marcadorInningsScreen,text="Team Home", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=20)
  marcadorInningsHomeTeam.grid(row=2, column=0)

  global marcadorInningsAwayRuns
  marcadorInningsAwayRuns=Label(marcadorInningsScreen,text="0", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3)
  marcadorInningsAwayRuns.grid(row=1, column=10)
  global marcadorInningsAwayHits
  marcadorInningsAwayHits=Label(marcadorInningsScreen,text="0", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3)
  marcadorInningsAwayHits.grid(row=1, column=11)
  global marcadorInningsAwayError
  marcadorInningsAwayError=Label(marcadorInningsScreen,text="0", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3)
  marcadorInningsAwayError.grid(row=1, column=12)

  global marcadorInningsHomeRuns
  marcadorInningsHomeRuns=Label(marcadorInningsScreen,text="0", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3)
  marcadorInningsHomeRuns.grid(row=2, column=10)
  global marcadorInningsHomeHits
  marcadorInningsHomeHits=Label(marcadorInningsScreen,text="0", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3)
  marcadorInningsHomeHits.grid(row=2, column=11)
  global marcadorInningsHomeError
  marcadorInningsHomeError=Label(marcadorInningsScreen,text="0", bg='white', font=("Calibri",12,"bold"), borderwidth=1, relief="solid", width=3)
  marcadorInningsHomeError.grid(row=2, column=12)

  global marcadorInningsAway1
  marcadorInningsAway1=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway1.grid(row=1, column=1)
  global marcadorInningsAway2
  marcadorInningsAway2=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway2.grid(row=1, column=2)
  global marcadorInningsAway3
  marcadorInningsAway3=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway3.grid(row=1, column=3)
  global marcadorInningsAway4
  marcadorInningsAway4=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway4.grid(row=1, column=4)
  global marcadorInningsAway5
  marcadorInningsAway5=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway5.grid(row=1, column=5)
  global marcadorInningsAway6
  marcadorInningsAway6=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway6.grid(row=1, column=6)
  global marcadorInningsAway7
  marcadorInningsAway7=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway7.grid(row=1, column=7)
  global marcadorInningsAway8
  marcadorInningsAway8=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway8.grid(row=1, column=8)
  global marcadorInningsAway9
  marcadorInningsAway9=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsAway9.grid(row=1, column=9)

  global marcadorInningsHome1
  marcadorInningsHome1=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome1.grid(row=2, column=1)
  global marcadorInningsHome2
  marcadorInningsHome2=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome2.grid(row=2, column=2)
  global marcadorInningsHome3
  marcadorInningsHome3=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome3.grid(row=2, column=3)
  global marcadorInningsHome4
  marcadorInningsHome4=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome4.grid(row=2, column=4)
  global marcadorInningsHome5
  marcadorInningsHome5=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome5.grid(row=2, column=5)
  global marcadorInningsHome6
  marcadorInningsHome6=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome6.grid(row=2, column=6)
  global marcadorInningsHome7
  marcadorInningsHome7=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome7.grid(row=2, column=7)
  global marcadorInningsHome8
  marcadorInningsHome8=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome8.grid(row=2, column=8)
  global marcadorInningsHome9
  marcadorInningsHome9=Label(marcadorInningsScreen,text="", bg='white', font=("Calibri",12), borderwidth=1, relief="solid", width=3)
  marcadorInningsHome9.grid(row=2, column=9)

  marcadorInningsScreen.protocol("WM_DELETE_WINDOW", on_closing)
  
def addOut(): #añade o quita Outs
  global Out
  global incdec
  if incdec.get()==1:
    if Out ==2:
      response=messagebox.askyesno("Nuevo inning", "Está seguro que quiere finalizar el inning?")
      if response==1:
        Out=0
        if topbot.get()==0: #Si estamos en top pasamos a bot
          atBat()
          topbot.set(1)
          inning()
        else: #si estamos en bot pasamos a siguiente imning
          atBat()
          topbot.set(0) 
          nextInning=currentInning.get()+1
          currentInning.set(nextInning)
          inning()
      else:
        Out=2
    else:
      atBat()
      Out=Out+1
  else:
    if Out ==0:
      Out=0
    else:
      Out=Out-1
  global imgOut
  imgOut=Image.open("img/Out"+ str(Out) + ".png")
  imgOut=imgOut.resize((30,15),Image.ANTIALIAS)
  imgOut=ImageTk.PhotoImage(imgOut)
  Label(ScoreBoardScreen,image=imgOut, bg='white').grid(row=1, column=9)
  imgOutLabel.config(image=imgOut)
  resetStrikeBola()

def resetStrikeBola():#ponemos a 0 las bolas y los strikes 
  global Strike
  Strike=0
  global Bola
  Bola=0
  global imgBola
  imgBola=Image.open("img/Bola0.png")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)

  global imgStrike
  imgStrike=Image.open("img/Strike0.png")
  imgStrike=imgStrike.resize((30,15),Image.ANTIALIAS)
  imgStrike=ImageTk.PhotoImage(imgStrike)

  imgBolaLabel.config(image=imgBola)
  imgStrikeLabel.config(image=imgStrike)

def addBola(): #añade o quita Bolas
  global Bola
  global incdec
  if incdec.get()==1:
    if Bola ==3:
      resetStrikeBola()
      atBat()
      #comprobaremos las bases para añadir corredores para añadir corredores
      if Primera.get()==0 and Segunda.get()==0:
        Primera.set(1)
      elif Primera.get()==1 and Segunda.get()==0:
        Segunda.set(1)
      elif Primera.get()==1 and Segunda.get()==1 and Tercera.get()==0:
        Tercera.set(1)
      elif Primera.get()==1 and Segunda.get()==1 and Tercera.get()==1:
        addRun()
      bases()
    else:
      Bola=Bola+1
  else:
    if Bola ==0:
      Bola=0
    else:
      Bola=Bola-1

  global imgBola
  imgBola=Image.open("img/Bola"+ str(Bola) + ".png")
  imgBola=imgBola.resize((40,15),Image.ANTIALIAS)
  imgBola=ImageTk.PhotoImage(imgBola)
 
  imgBolaLabel.config(image=imgBola)

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
  imgStrike=Image.open("img/Strike"+ str(Strike) + ".png")
  imgStrike=imgStrike.resize((30,15),Image.ANTIALIAS)
  imgStrike=ImageTk.PhotoImage(imgStrike)
  imgStrikeLabel.config(image=imgStrike)

def addRun():
  global RunsAway
  global RunsHome
  global incdec
  if incdec.get()==1:
    if topbot.get()==0: #La carrera sumara al visitante
      RunsAway=RunsAway+1
      if currentInning.get()<10:
        variable="marcadorInningsAway"+str(currentInning.get())
        if globals()[variable].cget("text")=="":
          globals()[variable].config(text="1")
        else:
          globals()[variable].config(text=str(int(globals()[variable].cget("text"))+1))
    else:
      RunsHome=RunsHome+1
      if currentInning.get()<10:
        variable="marcadorInningsHome"+str(currentInning.get())
        if globals()[variable].cget("text")=="":
          globals()[variable].config(text="1")
        else:
          globals()[variable].config(text=str(int(globals()[variable].cget("text"))+1))
  else:
    if topbot.get()==0: #La carrera restara al visitante
      RunsAway=RunsAway-1
      if currentInning.get()<10:
        variable="marcadorInningsAway"+str(currentInning.get())
        if globals()[variable].cget("text")=="":
          globals()[variable].config(text="")
        else:
          globals()[variable].config(text=str(int(globals()[variable].cget("text"))-1))
    else:
      RunsHome=RunsHome-1
      if currentInning.get()<10:
        variable="marcadorInningsHome"+str(currentInning.get())
        if globals()[variable].cget("text")=="":
          globals()[variable].config(text="")
        else:
          globals()[variable].config(text=str(int(globals()[variable].cget("text"))-1))
    
  RunsAwayLabel.config(text=str(RunsAway))
  RunsHomeLabel.config(text=str(RunsHome))
  ScoreBoardScreen.update()
  marcadorInningsAwayRuns.config(text=str(RunsAway))
  marcadorInningsHomeRuns.config(text=str(RunsHome))
  

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
  BasesLabel.config(image=imgBases)

def inning():
  global innImg
  if topbot.get()==0:
    innImg=Image.open("img/Arrow top.png")
    innImg=innImg.resize((15,15),Image.ANTIALIAS)
    innImg=ImageTk.PhotoImage(innImg)
    #cambiamos el at bat
    textatbat="A/B: " + str(atbatAway+1) +"º #"+ str(AwayNum[atbatAway]) + " "+ AwayName[atbatAway]
    atbatLabel.config(text = textatbat)
  else:
    innImg=Image.open("img/Arrow Bot.png")
    innImg=innImg.resize((15,15),Image.ANTIALIAS)
    innImg=ImageTk.PhotoImage(innImg)
    #cambiamos el at bat
    textatbat="A/B: " + str(atbatHome+1) +"º #"+ str(HomeNum[atbatHome]) + " "+ HomeName[atbatHome]
    atbatLabel.config(text = textatbat)

  actualInn=currentInning.get()
  actualInnLabel.config(text=actualInn)
  topbotInnLabel.config(image=innImg)
  updateHitterOverview()
  #Label(ScoreBoardScreen,image=innImg, bg='white').grid(row=0, column=8)
  #Label(ScoreBoardScreen,text=actualInn, bg='white').grid(row=0, column=9)

def hit():
  global hitgif
  global HitsAway
  global HitsHome

  if incdec.get()==1: #Función de incrementar 
    for i in range(2): #Animación de hit     
      for j in range (16):
        hitgif=Image.open("img/Hit/hit"+str(j)+".png")
        hitgif=ImageTk.PhotoImage(hitgif)
        BasesLabel.config(image=hitgif)
        ScoreBoardScreen.update()
        time.sleep(0.05)

      if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
        imgBases=logoAway.resize((80,80),Image.ANTIALIAS)
      else:
        imgBases=logoHome.resize((80,80),Image.ANTIALIAS)
      imgBases=ImageTk.PhotoImage(imgBases, format="gif -index 0")
      BasesLabel.config(image=imgBases)
      ScoreBoardScreen.update()
      time.sleep(0.5)

    #Muestra el número de hits en el partido
    if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      HitsAway=HitsAway+1
      TopLabel=Label(ScoreBoardScreen,text="Hits:", bg='white', font=("Calibri",12))
      TopLabel.grid(row=1, column=4, columnspan=2)
      BotLabel=Label(ScoreBoardScreen,text=HitsAway, bg='white', font=("Calibri",12))
      BotLabel.grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)
    else:
      HitsHome=HitsHome+1
      TopLabel=Label(ScoreBoardScreen,text="Hits:", bg='white', font=("Calibri",12))
      TopLabel.grid(row=1, column=4, columnspan=2)
      BotLabel=Label(ScoreBoardScreen,text=HitsHome, bg='white', font=("Calibri",12))
      BotLabel.grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)

    TopLabel.destroy()
    BotLabel.destroy()
    bases() #actualizamos las bases
    atBat() #cambiamos el at bat
    
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
  
  #Actualizamos el marcador por innings
  marcadorInningsAwayHits.config(text=HitsAway)
  marcadorInningsHomeHits.config(text=HitsHome)
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
        BasesLabel.config(image=errorgif)
        ScoreBoardScreen.update()
        time.sleep(0.1)

    img1=Image.open("img/error.png")
    img1=img1.resize((80,80),Image.ANTIALIAS)
    img1=ImageTk.PhotoImage(img1)

    img2=Image.open("img/error2.png")
    img2=img2.resize((80,80),Image.ANTIALIAS)
    img2=ImageTk.PhotoImage(img2)
    
    for i in range(2): #Animación de Error
      BasesLabel.config(image=img1)
      ScoreBoardScreen.update()
      time.sleep(0.15)
      BasesLabel.config(image=img2)
      ScoreBoardScreen.update()
      time.sleep(0.3)

      if topbot.get()==1: #el error mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
        imgBases=logoAway.resize((80,80),Image.ANTIALIAS)
      else:
        imgBases=logoHome.resize((80,80),Image.ANTIALIAS)
      imgBases=ImageTk.PhotoImage(imgBases, format="gif -index 0")
      BasesLabel.config(image=imgBases)
      ScoreBoardScreen.update()
      time.sleep(0.5)

    #Muestra el número de errors en el partido
    if topbot.get()==1: #el error mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      ErrorsAway=ErrorsAway+1
      TopLabel=Label(ScoreBoardScreen,text="Errores:", bg='white', font=("Calibri",12))
      TopLabel.grid(row=1, column=4, columnspan=2)
      BotLabel=Label(ScoreBoardScreen,text=ErrorsAway, bg='white', font=("Calibri",12))
      BotLabel.grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)
    else:
      ErrorsHome=ErrorsHome+1
      TopLabel=Label(ScoreBoardScreen,text="Errores:", bg='white', font=("Calibri",12))
      TopLabel.grid(row=1, column=4, columnspan=2)
      BotLabel=Label(ScoreBoardScreen,text=ErrorsHome, bg='white', font=("Calibri",12))
      BotLabel.grid(row=2, column=4, columnspan=2)
      ScoreBoardScreen.update()
      time.sleep(2.0)

    TopLabel.destroy()
    BotLabel.destroy()
    
    bases() #actualizamos las bases

    valor=messagebox.askquestion("Error","Siguiente bateador?")
    if valor=="yes":
      atBat() #cambiamos el at bat

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
  
  #Actualizamos el marcador por innings
  marcadorInningsAwayError.config(text=ErrorsAway)
  marcadorInningsHomeError.config(text=ErrorsHome)

def atBat(): #Pasa al siguiente bateador, mirando quien esta batenado si home o away
  global atbatAway
  global atbatHome
  
  if incdec.get()==1: #Función de incrementar 
    if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      if atbatAway==8:
        atbatAway=0
      else:
        atbatAway=atbatAway+1
      textatbat="A/B: " + str(atbatAway+1) +"º #"+ str(AwayNum[atbatAway]) + " "+ AwayName[atbatAway]
      atbatLabel.config(text = textatbat)
    else:
      if atbatHome==8:
        atbatHome=0
      else:
        atbatHome=atbatHome+1
      textatbat="A/B: " + str(atbatHome+1) +"º #"+ str(HomeNum[atbatHome]) + " "+ HomeName[atbatHome]
      atbatLabel.config(text = textatbat)
  else:
    if topbot.get()==0: #el hit mostrará el equipo que lo ha dado dependiendo si estamos en bot o top inning
      if atbatAway==0:
        atbatAway=atbatAway=8
      else:
        atbatAway=atbatAway-1
      textatbat="A/B: " + str(atbatAway+1) +"º #"+ str(AwayNum[atbatAway]) + " "+ AwayName[atbatAway]
      atbatLabel.config(text = textatbat)
    else:
      if atbatHome==0:
        atbatHome=8
      else:
        atbatHome=atbatHome-1
      textatbat="A/B: " + str(atbatHome+1) +"º #"+ str(HomeNum[atbatHome]) + " "+ HomeName[atbatHome]
      atbatLabel.config(text = textatbat)

  updateHitterOverview()

#funciones del menu bar de la root:
def exitMsg(): #Código del botón del Menu File->Exit
    valor=messagebox.askquestion("Exit","Está seguro que quiere cerrar?")
    if valor=="yes":
        ScoreBoardScreen.destroy()
        root.destroy()

def aboutMsg():
  messagebox.showinfo("About","Creado para el CB Barcelona")

def on_closing():
  #messagebox.showerror("Cerrar", "Esta ventana no puede ser cerrada")
  if messagebox.askokcancel("Cerrar", "Desea cerrar el marcador?"):
        root.destroy()
    
   
root=Tk()
root.title("CBSB - Control")
root.iconbitmap("logo/Barcelona.ico")
root.resizable(0,0) #Ancho, Alto (1 se puede 0 no se puede)
root.geometry("350x400")

#Listas de bateadores
global AwayNum
AwayNum=[1,2,3,4,5,6,7,8,9]
global AwayName
AwayName=["","","","","","","","",""]
global HomeNum
HomeNum=[1,2,3,4,5,6,7,8,9]
global HomeName
HomeName=["","","","","","","","",""]

global atbatAway
atbatAway=0
global atbatHome
atbatHome=0

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

#botones hit/error/run
Button(root,text="Hit", command=hit, width=7).grid(row=2,column=0, padx=5, pady=10)
Button(root,text="Error", command=error, width=7).grid(row=2,column=1, padx=5, pady=10)
Button(root,text="Run", command=addRun, width=7).grid(row=2,column=2, padx=5, pady=10)

#Corredores en las bases
Primera=IntVar()
Segunda=IntVar()
Tercera=IntVar()

Checkbutton(root,text="Primera", variable=Primera).grid(row=4,column=0, padx=5, pady=5)
Checkbutton(root,text="Segunda", variable=Segunda).grid(row=4,column=1, padx=5, pady=5)
Checkbutton(root,text="Tercera", variable=Tercera).grid(row=4,column=2, padx=5, pady=5)
Button(root,text="Update Bases", command=bases).grid(row=4,column=3, padx=2, pady=5)

#Lineup
Button(root,text="Line Up", command=lineUp, width=7).grid(row=5,column=0, padx=5, pady=10)

ttk.Separator(root,orient='horizontal').grid(row=6,column=0, sticky="ew", columnspan=4)

#inning
currentInning=IntVar()
currentInning.set(1)
OptionMenu(root,currentInning,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20).grid(row=7,column=0, padx=5, pady=5)

topbot=IntVar() #0 en caso de Away, 1 en caso de Home
Radiobutton(root, text="Top", variable=topbot, value=0).grid(row=7,column=1, padx=2, pady=5) 
Radiobutton(root, text="Bot", variable=topbot, value=1).grid(row=7,column=2, padx=2, pady=5)
Button(root,text="Update Inning", command=inning).grid(row=7,column=3, padx=2, pady=5)

#boton para cambiar el bateador
Button(root,text="At Bat", command=atBat).grid(row=8,column=0, padx=2, pady=5)

#Botores para incrementar o reducir
incdec=IntVar()
incdec.set(1) #Marcamos Increment por defecto al ejecutar
Radiobutton(root, text="Increment", variable=incdec, value=1).grid(row=9,column=0, padx=2, pady=5)
Radiobutton(root, text="Descent", variable=incdec, value=0).grid(row=9,column=1, padx=2, pady=5)


#Lanzamos pantalla del ScoreBoard
ScoreBoardScreen=""
hitterOverviewScreen=""
marcadorInningsScreen=""
frameAway=""
frameHome=""
root.after(10, scoreboard)
root.after(10, hitterOverview)
root.after(10, marcadorInnings)
root.geometry('+400+50')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()