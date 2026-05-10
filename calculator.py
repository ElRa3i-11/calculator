from tkinter import *
equation=""
calwin=Tk()
def leb() :
    inLabel.config(state='normal')
    inLabel.delete(0, END)
    inLabel.insert(0, equation)
    inLabel.xview_moveto(1)
    inLabel.config(state='disabled')

        
def Button0() :
    global equation
    n = 0
    equation = equation + str(n)
    leb()

def Button1() :
    global equation
    n = 1
    equation = equation + str(n)
    leb()
def Button2() :
    global equation
    n = 2
    equation=equation+str(n)
    leb()
def Button2() :
    global equation
    n = 2
    equation=equation+str(n)
    leb()
def Button3() :
    global equation
    n = 3
    equation=equation+str(n)
    leb()
def Button4() :
    global equation
    n = 4
    equation=equation+str(n)
    leb()
def Button5() :
    global equation
    n = 5
    equation=equation+str(n)
    leb()
def Button6() :
    global equation
    n = 6
    equation=equation+str(n)
    leb()
def Button7() :
    global equation
    n = 7
    equation=equation+str(n)
    leb()
def Button8() :
    global equation
    n = 8
    equation=equation+str(n)
    leb()
def Button9() :
    global equation
    n = 9
    equation=equation+str(n)
    leb()
######
def Plus() :
    global equation
    n = "+"
    equation=equation+n
    leb()
def minus() :
    global equation
    n = "-"
    equation=equation+n
    leb()
def Multiplicaiton() :
    global equation
    n = "*"
    equation=equation+n
    leb()
def point() :
    global equation
    n = "."
    equation=equation+n
    leb()
def calculator() :
    result=0.0
    num=""
    num2=""
    i=0
    while i<len(equation) :
        if equation[i].isdecimal() == True :
                num=num+equation[i]
                print(num,"ff")
                if i == len(equation) - 1 :
                    print(equation[i-1])
                    if equation[i-1] == "+" :
                        result=result+float(num)
                    elif equation[i-1] == "-" :
                        result=result-float(num)
                    else :
                        result=result*float(num)
        else :
            sign=equation[i]
            c=i+1
            while c<len(equation) and equation[c].isdecimal() == True :
                num2=num2+equation[c]
                c=c+1
            if sign == "+" :
                print(num,"ss")
                print(num2)
                result=result+float(num) + float(num2)
            if sign == "-" :
                print(num,"ss")
                print(num2)
                result=result+(float(num) - float(num2))
            if sign == "*" :
                print(num,"ss")
                print(num2)
                result=result+(float(num) * float(num2))  
            num=""
            num2=""
            i=c
        
        i=i+1 
    ResultLabel.config(text=result) 
def vanish():
    global equation,result 
    equation = ''
    result = 0.0
    inLabel.config(state='normal')
    inLabel.delete(0, END)
    inLabel.config(state='disabled')
    ResultLabel.config(text="")
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
inLabel= Entry(calwin,font=("Arial",40,"bold"),bd=10,relief="sunken",justify='right', state='disabled', disabledforeground='black')
ResultLabel=Label(calwin,font=("Arial",40,"bold"),bd=10,relief="sunken")

#other Button
pointButton=Button(calwin,text=".",
                font=("Arial",60,"bold"),
                command=point,
                )
equalsButton=Button(calwin,text="=",
                font=("Arial",60,"bold"),
                command=calculator
                )
plusButton=Button(calwin,text="+",
                font=("Arial",60,"bold"),
                command=Plus,
                )
minusButton=Button(calwin,text="-",
                font=("Arial",60,"bold"),
                command=minus
                )
multiplieButton=Button(calwin,text="x",
                font=("Arial",60,"bold"),
                command=Multiplicaiton,
                )
CButton=Button(calwin,text="C",
                font=("Arial",60,"bold"),
                command=vanish,
                )
# SE = SHIVA + ElRa3i
calwin.title(" SE Calculator")
#icon = PhotoImage(file='logo.png')
#calwin.iconphoto(True,icon)
calwin.geometry("600x640")
calwin.config(background="#4b4c4f")
calwin.minsize(600, 640)
for i in range(5):
    calwin.columnconfigure(i, weight=1)

zeroButton.grid(row=5,column=0,columnspan=2,pady=(0, 0),sticky=EW)
oneButton.grid(row=4,column=0,pady=(0, 0),sticky=EW)
twoButton.grid(row=4,column=1,pady=(0, 0),sticky=EW)
threeButton.grid(row=4,column=2,pady=(0, 0),sticky=EW)
fourButton.grid(row=3,column=0,pady=(0, 0),sticky=EW)
fiveButton.grid(row=3,column=1,pady=(0, 0),sticky=EW)
sixButton.grid(row=3,column=2,pady=(0, 0),sticky=EW)
sevenButton.grid(row=2,column=0,pady=(0, 0),sticky=EW)
eightButton.grid(row=2,column=1,pady=(0, 0),sticky=EW)
nineButton.grid(row=2,column=2,pady=(0, 0),sticky=EW)

inLabel.grid(row=0,column=0,columnspan=4,pady=(50,0),sticky=EW)
ResultLabel.grid(row=1,column=0,columnspan=4,pady=(0,0),sticky=EW)

pointButton.grid(row=5,column=2,pady=(0, 0),sticky=EW)
equalsButton.grid(row=4,column=3,rowspan=2,pady=(0, 0),sticky=NSEW)
equalsButton.config(bg="#62d3f5")
plusButton.grid(row=3,column=3,pady=(0, 0),sticky=EW)
minusButton.grid(row=2,column=3,pady=(0, 0) , sticky=EW)
CButton.grid(row=2,column=4,pady=(0, 0) , sticky=EW)
multiplieButton.grid(row=3,column=4,pady=(0, 0) , sticky=EW)
calwin.mainloop()

