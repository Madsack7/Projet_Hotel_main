from tkinter import *
from tkinter import ttk


root = Tk()

root.title("Hotel")
root.geometry("1080x720")
root.config(bg="white")
#pour afficer le label Client
A=Frame(root,width=1500,height=700,background='#D9D9D9')
titre1 =Label(A, text="RESTAURANT",background='#B7AAAA',font=("Arial",40))
titre1.place(x=50, y=50)
titre1.pack()
#bouton quitter
b4 = Button(text='<-',font=("Arial",16),background='#5C4D4D',width=5)
b4.place(x=0, y=0)

#Pour afficher le label Id
titre2 = Label(A, text="Id",background='#D9D9D9',font=("Arial",16))
titre2.place(x=20, y=100)
#champ de text pour l' Id
v1=StringVar()
text2 = Entry(A, width=33,background='#FEFAFA',textvariable=v1)
text2.place(x=316, y=100)
#pour afficher le label type_nouriture
titre3 = Label(A, text="Type_nouriture",background='#D9D9D9',font=("Arial",16))
titre3.place(x=20, y=200)
#champ de text pour le type_nouriture
v2=StringVar()
text3 = Entry(A, width=33,background='#FEFAFA',textvariable=v2)
text3.place(x=316, y=200)
#pour afficher le label prix_nouriture
titre4 = Label(A, text="Prix_nouriture",background='#D9D9D9',font=("Arial",16))
titre4.place(x=20, y=300)
#le champ de text pour le prix_nouriture
v3=StringVar()
text4 = Entry(A, width=33,background='#FEFAFA',textvariable=v3)
text4.place(x=316, y=300)
#le label recherche
titre5 = Label(A, text="Recherche",background='#D9D9D9',font=("Arial",16))
titre5.place(x=800, y=260)
#champ de text pour la recherche
v4=StringVar()
text5 = Entry(A, width=33,background='#FEFAFA',textvariable=v4)
text5.place(x=780, y=300)

B=Frame(root,width=1500,height=320,background='#D9D9D9')
#bouton enregistrer
b1 = Button(B, text="enregistrer",width=15,background='#93B976',font=("Arial",16))
b1.place(x=20, y=10)

#bouton modifier
b2 = Button(B, text="modifier",width=15,font=("Arial",16),background='#8E9AB7')
b2.place(x=500, y=10)

#bouton supprimer
b3 = Button(B, text="supprimer",width=15,font=("Arial",16),background='#DB7979')
b3.place(x=1000, y=10)

#TABLEAU
tableAfficher = ttk.Treeview(B, columns=(1, 2, 3), height=10, show="headings")
tableAfficher.place(x=5, y=55, width=1280, height=400)
# Entete
tableAfficher.heading(1, text="Id")
tableAfficher.heading(2, text="Type_nouriture")
tableAfficher.heading(3, text="Prix_nouriture")


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