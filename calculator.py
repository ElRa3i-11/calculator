from tkinter import *
calwin=Tk()
#Button from zero to nine
zeroButton=Button(calwin,text="0",
                font=("Arial",60,"bold"),
                )
oneButton=Button(calwin,text="1",
                font=("Arial",60,"bold"),
                )
twoButton=Button(calwin,text="2",
                font=("Arial",60,"bold"),
                )
threeButton=Button(calwin,text="3",
                font=("Arial",60,"bold"),
                )
fourButton=Button(calwin,text="4",
                font=("Arial",60,"bold"),
                )
fiveButton=Button(calwin,text="5",
                font=("Arial",60,"bold"),
                )
sixButton=Button(calwin,text="6",
                font=("Arial",60,"bold"),
                )
sevenButton=Button(calwin,text="7",
                font=("Arial",60,"bold"),
                )
eightButton=Button(calwin,text="8",
                font=("Arial",60,"bold"),
                )
nineButton=Button(calwin,text="9",
                font=("Arial",60,"bold"),
                )
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
icon = PhotoImage(file='logo.png')
calwin.iconphoto(True,icon)
calwin.geometry("380x640")
calwin.config(background="#4b4c4f")

zeroButton.grid(row=3,column=0,columnspan=2,pady=(0, 0),sticky=EW)
pointButton.grid(row=3,column=2,pady=(0, 0),sticky=EW)
oneButton.grid(row=2,column=0,pady=(0, 0))
twoButton.grid(row=2,column=1,pady=(0, 0))
threeButton.grid(row=2,column=2,pady=(0, 0))
fourButton.grid(row=1,column=0,pady=(0, 0))
fiveButton.grid(row=1,column=1,pady=(0, 0))
sixButton.grid(row=1,column=2,pady=(0, 0))
sevenButton.grid(row=0,column=0,pady=(230, 0))
eightButton.grid(row=0,column=1,pady=(230, 0))
nineButton.grid(row=0,column=2,pady=(230, 0))
equalsButton.grid(row=3,column=3,pady=(0, 0))
equalsButton.config(bg="#62d3f5")
plusButton.grid(row=2,column=3,pady=(0, 0))
minesButton.grid(row=1,column=3,pady=(0, 0) , sticky=EW)
multiplieButton.grid(row=0,column=3,pady=(230, 0) , sticky=EW)
calwin.mainloop()

