from tkinter import *
from tkinter.tix import ComboBox
from tkinter.ttk import Combobox
from turtle import bgcolor
from tkinter.tix import ComboBox
from subprocess import call
#retour
def enregistrer():
    fenetre.destroy()
    call(["python","inscription.py"])

fenetre=Tk()
fenetre.title("Hotel")
fenetre.geometry("1280x720")
fenetre.minsize(480,320)
fenetre.config(background='#D9D9D9')
inscription=Label(fenetre,text="INSCRIPTION",font=('Courrier',40),bg='#C6C2C2').pack(side=TOP)
cadre=Frame(fenetre,bg='#C6C2C2',bd=1,relief=SUNKEN,height=450,width=800)

nom=Label(cadre,text="Nom",font=('Inria Sans',18),bg='#C6C2C2').place(y=50,x=200)
v1=StringVar()
nomchamp=Entry(cadre,width=30,textvariable=v1,bg='#D9D9D9').place(y=50,x=500)

prenom=Label(cadre,text="Prenom",font=('Inria Sans',18),bg='#C6C2C2').place(y=100,x=200)
v2=StringVar()
prenomchamp=Entry(cadre,width=30,textvariable=v2,bg='#D9D9D9').place(y=100,x=500)

numero=Label(cadre,text="Numero",font=('Inria Sans',18),bg='#C6C2C2').place(y=150,x=200)
v3=StringVar()
numerochamp=Entry(cadre,width=30,textvariable=v3,bg='#D9D9D9').place(y=150,x=500)

role=Label(cadre,text="Role",font=('Inria Sans',18),bg='#C6C2C2').place(y=200,x=200)
degiskenler=['Gérant','Responsable']
rolechamp=Combobox(cadre, values=degiskenler,height=3,background='#D9D9D9').place(width=185,height=20,y=200,x=500)

email=Label(cadre,text="Email",font=('Inria Sans',18),bg='#C6C2C2').place(y=250,x=200)
v5=StringVar()
emailchamp=Entry(cadre,width=30,textvariable=v5,bg='#D9D9D9').place(y=250,x=500)

mot_de_passe=Label(cadre,text="Mot de passe",font=('Inria Sans',18),bg='#C6C2C2').place(y=300,x=200)
v6=StringVar()
mot_de_passechamp=Entry(cadre,width=30,textvariable=v6,bg='#D9D9D9').place(y=300,x=500)

confirmer_mot_de_passe=Label(cadre,text="Confirmer votre mot de passe",font=('Inria Sans',18),bg='#C6C2C2').place(y=350,x=160)
v7=StringVar()
confirmer_mot_de_passechamp=Entry(cadre,width=30,textvariable=v7,bg='#D9D9D9').place(y=350,x=500)

b1 =Button(cadre, text="enregistrer",background='#93B976',font=("Arial",16),command=enregistrer)
b1.place(y=400, x=560)

cadre.pack_propagate(False)
cadre.pack(expand=YES)
fenetre.mainloop()