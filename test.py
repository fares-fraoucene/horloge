from tkinter import *
import time
root = Tk()
root.title("Horloge")
root.geometry("1920x1040")
root.config(bg="black")
lbl_heure = Label(root, text="15", font=("time new roman", 50, "bold"), bg="green")
lbl_heure.place(x=500, y=300, width=130, height=130)
lbl_minute = Label(root, text="12", font=("time new roman", 50, "bold"), bg="yellow")
lbl_minute.place(x=700, y=300, width=130, height=130)
lbl_seconde = Label(root, text="12", font=("time new roman", 50, "bold"), bg="red")
lbl_seconde.place(x=900, y=300, width=130, height=130)
entry_heure = Entry(root, font=("time new roman", 30, "bold"), bd=5, relief=GROOVE)
entry_heure.place(x=500, y=500, width=70, height=50)
entry_minute = Entry(root, font=("time new roman", 30, "bold"), bd=5, relief=GROOVE)
entry_minute.place(x=700, y=500, width=70, height=50)
entry_seconde = Entry(root, font=("time new roman", 30, "bold"), bd=5, relief=GROOVE)
entry_seconde.place(x=900, y=500, width=70, height=50)
def mettre_a_jour_heure():
    now = time.localtime()
    h = now.tm_hour
    m = now.tm_min
    s = now.tm_sec
    try:
        h_user = int(entry_heure.get())
        m_user = int(entry_minute.get())
        s_user = int(entry_seconde.get())
    except ValueError:
        print("Veuillez saisir des valeurs numériques valides.")
        return
    s_user += 1
    lbl_heure.config(text=str(h_user))
    lbl_minute.config(text=str(m_user))
    lbl_seconde.config(text=str(s_user))
    root.after(1000, mettre_a_jour_heure)

# Fonction appelée lorsque le bouton Valider est cliqué
def valider_heure():
    mettre_a_jour_heure()

# Bouton Valider
btn_valider = Button(root, text="Valider", font=("time new roman", 20, "bold"), bg="white", fg="black", command=valider_heure)
btn_valider.place(x=1100, y=500, width=150, height=50)

mettre_a_jour_heure()

root.mainloop()
