#la fenetre
from subprocess import call
from tkinter import *
from tkinter import ttk, Entry
root = Tk()
root.title("Hotel")
root.geometry("1000x650")
root.resizable(False, False)
root.configure(background='#D9D9D9')
# Ajouter un titre
lbltitre = Label(root, text="employés", font=("Arial",20), background='#B7AAAA', foreground='black')
lbltitre.place(x=170, y=10, width=300)

#bouton quitter
def dashboard():
    root.destroy()
    call(["python","dashboard.py"])
    
b4 = Button(text='<-',font=("Arial",16),background='#5C4D4D',width=5,command=dashboard)
b4.place(x=0, y=0)

lblnom = Label(root, text="Nom", font=("sans serif", 14), background='#D9D9D9', foreground='black')
lblnom.place(x=10, y=70, width=130)
txtnom=Entry(root, bd=4, font=("Arial", 14))
txtnom.place(x=200, y=70, width=150)

lblprenom = Label(root, text="Prenom", font=("sans serif", 14), background='#D9D9D9', foreground='black')
lblprenom.place(x=400, y=70, width=70)
txtprenom=Entry(root, bd=4, font=("Arial", 14))
txtprenom.place(x=600, y=70, width=150)

lblnumero = Label(root, text="numero", font=("sans serif", 14), background='#D9D9D9', foreground='black')
lblnumero.place(x=10, y=150, width=80)
txtnumero=Entry(root, bd=4, font=("Arial", 14))
txtnumero.place(x=200, y=150, width=150)

lblsalaire = Label(root, text="Salaire", font=("sans serif", 14), background='#D9D9D9', foreground='black')
lblsalaire.place(x=400, y=150, width=90)
txtsalaire=Entry(root, bd=4, font=("Arial", 14))
txtsalaire.place(x=600, y=150, width=150)

lbldate = Label(root, text="Date_embauche", font=("sans serif", 14), background='#D9D9D9', foreground='black')
lbldate.place(x=10, y=220, width=150)
txtdate=Entry(root, bd=4, font=("Arial", 14))
txtdate.place(x=200, y=220, width=150)

btnAjouter = Button(root, text="Enregistrer", font=("Arial", 24), bg="#93B976", fg="black")
btnAjouter.place(x=100, y=320, width=200)

btnmodifier = Button(root, text="Modifier", font=("Arial", 24), bg="#8E9AB7", fg="black")
btnmodifier.place(x=400, y=320, width=200)

btnsupprimer = Button(root, text="Supprimer", font=("Arial", 24), bg="#DB7979", fg="black")
btnsupprimer.place(x=700, y=320, width=200)


# Table
tableAfficher = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), height=10, show="headings")
tableAfficher.place(x=0, y=450, width=1000, height=200)
# Entete
tableAfficher.heading(1, text="Num_employe")
tableAfficher.heading(2, text="Nom_employe")
tableAfficher.heading(3, text="Prenom")
tableAfficher.heading(4, text="numero")
tableAfficher.heading(5, text="salaire")
tableAfficher.heading(6, text="Dated_embauche")
# definir les dimentions des colonnes
tableAfficher.column(1, width=50)
tableAfficher.column(2, width=50)
tableAfficher.column(3, width=50)
tableAfficher.column(4, width=50)
tableAfficher.column(5, width=50)
tableAfficher.column(6, width=50)


# l'exterieur
root.mainloop()