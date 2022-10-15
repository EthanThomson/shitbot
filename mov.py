#imps
import time
from gpiozero import PhaseEnableMotor, LED
from tkinter import *

root = Tk()

# bing chilling

# gui
##:sliders feed into profile
##:gui inputs bot heading for botgui
root.title('Control Board V1')

# labels&frames

bothead = Label(root, text="Bot:")
slidershead = Label(root, text="Sliders:")
terminalhead = Label(root, text="Terminal:")
loghead = Label(root, text="Log:")

logbox = Listbox(root)
logscroll = Scrollbar(root)
logbox.config(yscrollcommand=logscroll.set)
logscroll.config(command=logbox.yview)

terminalbox = Listbox(root)
terminalscroll = Scrollbar(root)
terminalbox.config(yscrollcommand=terminalscroll.set)
terminalscroll.config(command=terminalbox.yview)



# sliders
glodalspeed = Scale(root, from_=1, to=100, orient=HORIZONTAL)

# griding
bothead.grid(row=0, column=0)
slidershead.grid(row=0, column=3)
terminalhead.grid(row=1, column=0)
loghead.grid(row=1, column=3)
logbox.grid(row=3, column=3)
logscroll.grid(row=3, column=4)
terminalbox.grid(row=3, column=0)
terminalscroll.grid(row=3, column=1)

glodalspeed.grid(row=1, column=3)

# exec
def slp(x):
    time.sleep(x)


leftmotor = PhaseEnableMotor(24, 15)
rightmotor = PhaseEnableMotor(14, 25)

mode = LED(18)
mode.on()

def goforward():
    leftmotor.forward(0.4)
    rightmotor.forward(0.4)
    slp(1)
    leftmotor.stop()
    rightmotor.stop()


def gobackward():
    leftmotor.backward(0.4)
    rightmotor.backward(0.4)
    slp(1)
    leftmotor.stop()
    rightmotor.stop()



while 1:
    print(1)
    goforward()
    print(2)
    goforward()
    print(3)
    goforward()
    print("ree")




root.mainloop()



# router
##:router takes profile as consts and then uses "wasd" to move the bot  might make diagnal keys aswell

# profile
##:profile gives router the values





    







                       