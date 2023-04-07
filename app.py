# by☺☺☺
#     Koutam
#     Moulaye
# importation du module tkinter
from tkinter import *
import webbrowser


def open_twitter():
    webbrowser.open_new("https://twitter.com/KoutamMohamed/")


# création de notre première fenetre
window = Tk()

# personnalisation de notre fenetre
window.title("My Application")
window.geometry('720x480')
window.iconbitmap("km_logo.ico")
window.config(background='#3e4927')
# Creer notre div pour centrer nos elements
frame = Frame(window, bg='#3e4927')
# Taille mimimale de notre fenetre
window.minsize(480, 360)
# Ajoutons du texte
label_title = Label(frame, text="Welcome to My Application", font=('Courrier', 40), bg='#3e4927', fg='white')
# l'intégrer dans notre fenetre
label_title.pack()
# Ajoutons du texte2
label_subtitle = Label(frame, text="Hey everybody it's Koutam", font=('Courrier', 25), bg='#3e4927', fg='white')
label_subtitle.pack()
# ajout d'un boutton
tw_button = Button(frame, text='open twitter', bg='white', font=('courrier', 25), fg='#3e4927',command=open_twitter)
tw_button.pack(pady=25, fill=X, )
# l'intégrer dans notre fenetre
frame.pack(expand=YES)
# afficher dans notre boucle principale
window.mainloop()
