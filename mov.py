#imps
from tkinter import *


root = Tk()

from gpiozero import PhaseEnableMotor, Pin, BadPinFactory, PinFactoryFallback, exc

#bing chilling
leftmotor = PhaseEnableMotor(12, 5)
rightmotor = PhaseEnableMotor(13, 6)
def goforwards():
    leftmotor.forward()
    rightmotor.forward()
    logbox.insert(END, "forwards: ")
    logbox.update()

def gobackwards():
    leftmotor.backward()
    rightmotor.backward()
    logbox.insert(END, "backwards: ")
    logbox.update()


#gui
##:sliders feed into profile
##:gui inputs bot heading for botgui
root.title('Control Board V1')


#labels&frames&fields
lmpha = Entry(root, width= 10)
lmen = Entry(root, width= 10)
rmpha = Entry(root, width= 10)
rmen = Entry(root, width= 10)


bothead = Label(root, text="Bot:")
slidershead = Label(root, text="Sliders:")
terminalhead = Label(root, text="Terminal:")
loghead = Label(root, text="Log:")


logbox = Listbox(root)
logscroll = Scrollbar(root)
logbox.config(yscrollcommand= logscroll.set)
logscroll.config(command=logbox.yview)


terminalbox = Listbox(root)
terminalscroll = Scrollbar(root)
terminalbox.config(yscrollcommand= terminalscroll.set)
terminalscroll.config(command=terminalbox.yview)

#sliders
glodalspeed = Scale(root, from_= 1, to= 100, orient= HORIZONTAL)

wkey = Button(root, text= "w",command= goforwards)
skey = Button(root, text="s", command= gobackwards)
#griding
bothead.grid(row=0, column=0)
slidershead.grid(row=0, column=3)
terminalhead.grid(row=3, column=0)
loghead.grid(row=1, column=3)
logbox.grid(row=4, column=3)
logscroll.grid(row=4, column=4)
terminalbox.grid(row= 4, column=0)
terminalscroll.grid(row= 4, column=1)

wkey.grid(row= 1, column= 0)
skey.grid(row= 2, column= 0)

glodalspeed.grid(row= 1, column=3)
lmpha.grid(row=2, column=3)
lmen.grid(row=2, column=4)
rmpha.grid(row=3, column=3)
rmen.grid(row=3, column=4)

root.mainloop()


#router
##:router takes profile as consts and then uses "wasd" to move the bot  might make diagnal keys aswell
#leftmotor = PhaseEnableMotor(lmpha.get(), lmen.get())
#rightmotor = PhaseEnableMotor(rmpha.get(), rmen.get())






#profile
##:profile gives router the values




