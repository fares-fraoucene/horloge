from tkinter import *
import time
import sys

root = Tk()

root.title("Horloge")
root.geometry("1920x1040")
root.config(bg="black")

lbl_heure = Label(root, text="15", font=("time new roman", 50,"bold"), bg="green")
lbl_heure.place(x=500, y=300,width=130, height=130)

lbl_minute = Label(root, text="12", font=("time new roman", 50,"bold"), bg="yellow")
lbl_minute.place(x=700, y=300,width=130, height=130)

lbl_seconde = Label(root, text="12", font=("time new roman", 50,"bold"), bg="red")
lbl_seconde.place(x=900, y=300,width=130, height=130)

def recupHeure():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    print(h,"h",m,"m",s,"s", end="\r")
    sys.stdout.flush()  
    lbl_heure.config(text=h)
    lbl_minute.config(text=m)
    lbl_seconde.config(text=s)
    lbl_heure.after(200, recupHeure)

recupHeure()
print(recupHeure)
root.mainloop()