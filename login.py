from tkinter import*
from subprocess import call
from PIL import ImageTk, Image
#retour
def enregistrer():
    fenetre.destroy()
    call(["python","inscription.py"])
#retour

#inscription
def s_inscrire():
    call(["python","inscri_user.py"])
from subprocess import call
#retour
def se_connecter():
    fenetre.destroy()
    call(["python","dashboard.py"])


fenetre = Tk()
fenetre.title("AUTHENTIFIACATION ")
fenetre.geometry("470x400")
fenetre.minsize(470, 400)
#fenetre.maxsize(470, 400)
fenetre.config(background="white")
#a_fr=Frame(fenetre,bg="yellow")
a=Frame(fenetre,width=800,height=400,bg="#D9D9D9")

s=Label(a,text="AUTHENTIFIFCATION ", font=("Arial", 20), width=38, height=1, fg="black",bg="#D9D9D9")
s.place(x=120,y=20)



email = Label(a, text="EMAIL ", font=("Arial", 20), width=6, height=1,  fg="black",bg="#D9D9D9")
#Nom.grid(row=0, column=0)
email.place(x=10,y=110)

entre1= Entry(a, font=("Arial", 20), bg="#9E9696", fg="black", width=20)
entre1.place(x=300,y=110)


mot_passe=Label(a, text="MOT DE PASSE ", font=("Arial", 20), width=13, height=1,  fg="black",bg="#D9D9D9")
mot_passe.place(x=4,y=170 )

entre2= Entry(a, font=("Arial", 20), bg="#9E9696", fg="black", width=20)
entre2.place(x=300,y=170)



bouton=Button(a,text="se connecter",font=("Arial", 15), width=17, height=1,  fg="white",bg="#5C4D4D",command= se_connecter )
bouton.place(x=200,y=300)

bouton1=Button(a,text="s'inscrire",font=("Arial", 15), width=17, height=1,  fg="white",bg="#5C4D4D",command=s_inscrire)
bouton1.place(x=510,y=300)

a.pack_propagate(False)
a.pack(expand=YES)
a.pack()
fenetre.mainloop()