from tkinter import *
from tkinter import ttk
from subprocess import call

root = Tk()

root.title("Hotel")
root.geometry("990x720")
root.config(bg="white")
#pour afficer le label Client
A=Frame(root,width=1500,height=700,background='#D9D9D9')
titre1 =Label(A, text="RESERVATION",background='#B7AAAA',font=("Arial",40))
titre1.place(x=50, y=50)
titre1.pack()
#bouton quitter
def dashboard():
    root.destroy()
    call(["python","dashboard.py"])





#Pour afficher le label num_chambre
titre2 = Label(A, text="Chambre",background='#D9D9D9',font=("Arial",16))
titre2.place(x=20, y=100)
#champ de text pour le num_chambre
v1=StringVar()
degiskenler=['CLIENT','CHAMBRE','SALLE','EMPLOYE']
rolechamp=ttk.Combobox(root, values=degiskenler,font=("Inria Sans",10)).place(width=200,height=20,x=316, y=100)
#pour afficher le label categorie
titre3 = Label(A, text="Client",background='#D9D9D9',font=("Arial",16))
titre3.place(x=20, y=200)
#champ de text pour categorie
v2=StringVar()

degiskenler=['CLIENT','CHAMBRE','SALLE','EMPLOYE']
rolechamp=ttk.Combobox(root, values=degiskenler,font=("Inria Sans",10)).place(width=200,height=20,x=316, y=200)
#pour afficher le label montant à payer
titre4 = Label(A, text="Date de Reservation",background='#D9D9D9',font=("Arial",16))
titre4.place(x=20, y=300)
#le champ de text pour le montant à payer
v3=StringVar()
text4 = Entry(A, width=33,background='#FEFAFA',textvariable=v3)
text4.place(x=316, y=300)
#le label recherche
titre5 = Label(A, text="Date de fin Reservation",background='#D9D9D9',font=("Arial",16))
titre5.place(x=670, y=260)
#champ de text pour la recherche
v4=StringVar()
text5 = Entry(A, width=33,background='#FEFAFA',textvariable=v4)
text5.place(x=680, y=300)

B=Frame(root,width=1300,height=320,background='#D9D9D9')
#bouton enregistrer
b1 = Button(B, text="enregistrer",width=15,background='#93B976',font=("Arial",16))
b1.place(x=20, y=10)

#bouton modifier
b2 = Button(B, text="modifier",width=15,font=("Arial",16),background='#8E9AB7')
b2.place(x=500, y=10)

#bouton supprimer
b3 = Button(B, text="supprimer",width=15,font=("Arial",16),background='#DB7979')
b3.place(x=800, y=10)

#TABLEAU
tableAfficher = ttk.Treeview(B, columns=(1, 2, 3,4,5,6,7), height=10, show="headings")
tableAfficher.place(x=5, y=55, width=980, height=400)
# Entete
tableAfficher.heading(1, text="ID")
tableAfficher.heading(2, text="NUM_chambre")
tableAfficher.heading(3, text="ID_Client")
tableAfficher.heading(4, text="NOM_Client")
tableAfficher.heading(5, text="Prenom_Client")
tableAfficher.heading(6, text="Date_Reservation")
tableAfficher.heading(7, text="Date_fin_Reservation")



# definir les dimentions des colonnes
tableAfficher.column(1, width=50)
tableAfficher.column(2, width=50)
tableAfficher.column(3, width=50)
B.pack_propagate(False)
B.pack(side=BOTTOM)
B.pack()

A.pack_propagate(False)
A.pack(expand=YES)
A.pack()

root.mainloop()