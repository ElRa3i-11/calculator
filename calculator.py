from tkinter import *
equation=""
calwin=Tk()
#button fonction
            #####Important#####
#######Lezem nl9wa methode n5tsro biha he4a el kol########
##jrbt n3ml haka ama m5dmtch
#def Buttonpr(n) :
#    global equation
#    equation=equation+str(n)
#    inLabel.config(text=equation)
#oneButton=Button(calwin,text="1",
#                font=("Arial",60,"bold"),
#                command=Buttonpr(1),
#               )
#twoButton=Button(calwin,text="2",
#                font=("Arial",60,"bold"),
#                command=Buttonpr(2),
#               )
def Button0() :
    global equation
    n = 0
    equation = equation + str(n)
    inLabel.config(text=equation)

def Button1() :
    global equation
    n = 1
    equation = equation + str(n)
    inLabel.config(text=equation)
def Button2() :
    global equation
    n = 2
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button2() :
    global equation
    n = 2
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button3() :
    global equation
    n = 3
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button4() :
    global equation
    n = 4
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button5() :
    global equation
    n = 5
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button6() :
    global equation
    n = 6
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button7() :
    global equation
    n = 7
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button8() :
    global equation
    n = 8
    equation=equation+str(n)
    inLabel.config(text=equation)
def Button9() :
    global equation
    n = 9
    equation=equation+str(n)
    inLabel.config(text=equation)

#Button from zero to nine
zeroButton=Button(calwin,text="0",
                font=("Arial",60,"bold"),
                command=Button0 ,
                )
oneButton=Button(calwin,text="1",
                font=("Arial",60,"bold"),
                command=Button1,
                )
twoButton=Button(calwin,text="2",
                font=("Arial",60,"bold"),
                command=Button2 ,
                )
threeButton=Button(calwin,text="3",
                font=("Arial",60,"bold"),
                command=Button3 ,
                )
fourButton=Button(calwin,text="4",
                font=("Arial",60,"bold"),
                command=Button4,
                )
fiveButton=Button(calwin,text="5",
                font=("Arial",60,"bold"),
                command=Button5 ,
                )
sixButton=Button(calwin,text="6",
                font=("Arial",60,"bold"),
                command=Button6,
                )
sevenButton=Button(calwin,text="7",
                font=("Arial",60,"bold"),
                command=Button7 ,
                )
eightButton=Button(calwin,text="8",
                font=("Arial",60,"bold"),
                command=Button8 ,
                )
nineButton=Button(calwin,text="9",
                font=("Arial",60,"bold"),
                command=Button9 ,
                )
#lablels
inLabel= Label(calwin,font=("Arial",50,"bold"),bd=10,relief="sunken")
ResultLabel=Label(calwin,font=("Arial",50,"bold"),bd=10,relief="sunken")

#other Button
pointButton=Button(calwin,text=".",
                font=("Arial",60,"bold"),
                )
equalsButton=Button(calwin,text="=",
                font=("Arial",60,"bold"),
                )
plusButton=Button(calwin,text="+",
                font=("Arial",60,"bold"),
                )
minesButton=Button(calwin,text="-",
                font=("Arial",60,"bold"),
                )
multiplieButton=Button(calwin,text="x",
                font=("Arial",60,"bold"),
                )
# SE = SHIVA + ElRa3i
calwin.title(" SE Calculator")
#icon = PhotoImage(file='logo.png')
#calwin.iconphoto(True,icon)
calwin.geometry("380x640")
calwin.config(background="#4b4c4f")

zeroButton.grid(row=5,column=0,columnspan=2,pady=(0, 0),sticky=EW)
pointButton.grid(row=5,column=2,pady=(0, 0),sticky=EW)
oneButton.grid(row=4,column=0,pady=(0, 0))
twoButton.grid(row=4,column=1,pady=(0, 0))
threeButton.grid(row=4,column=2,pady=(0, 0))
fourButton.grid(row=3,column=0,pady=(0, 0))
fiveButton.grid(row=3,column=1,pady=(0, 0))
sixButton.grid(row=3,column=2,pady=(0, 0))
sevenButton.grid(row=2,column=0,pady=(0, 0))
eightButton.grid(row=2,column=1,pady=(0, 0))
nineButton.grid(row=2,column=2,pady=(0, 0))

inLabel.grid(row=0,column=0,columnspan=6,pady=(50,0),sticky=EW)
ResultLabel.grid(row=1,column=0,columnspan=6,pady=(0,0),sticky=EW)

equalsButton.grid(row=4,column=3,pady=(0, 0))
equalsButton.config(bg="#62d3f5")
plusButton.grid(row=3,column=3,pady=(0, 0))
minesButton.grid(row=2,column=3,pady=(0, 0) , sticky=EW)
multiplieButton.grid(row=3,column=4,pady=(0, 0) , sticky=EW)
calwin.mainloop()

