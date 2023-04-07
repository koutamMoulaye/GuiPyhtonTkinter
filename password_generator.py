# by☺☺☺
#     Koutam
#     Moulaye
from tkinter import *
from random import *
import string
def password_generate():
    password_max=12
    password_min=6
    all_chars= string.digits + string.punctuation + string.ascii_letters
    password ="" .join(choice(all_chars) for x in range(randint(password_min,password_max)))
    password_entry.delete(0,END)
    password_entry.insert(0,password)
# creation de ma fenetre
window = Tk()
# personnalisation de notre fenetre
window.title("Password generator")
window.geometry('720x480')
window.minsize(720, 480)
window.iconbitmap("km_logo.ico")
window.config(bg="#3e4927")
#creation de notre frame
frame = Frame(window, bg='#3e4927')
# creation d'image dans un canvas comme un div den HTML
width = 300
height = 300
image = PhotoImage(file="password_logo.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#3e4927',bd=0,highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0,column=0,sticky=W)
#creation sous frame
right_frame = Frame(frame, bg='#3e4927')
#creation titre
lable_title=Label(right_frame, text='Password', font=('Helvetica', 20), bg='#3e4927', fg = "white")
lable_title.pack()
#creation d'entrer
password_entry=Entry(right_frame, font=('Helvetica', 20), bg='#3e4927', fg = "white")
password_entry.pack()
#creation boutton
generate_password_button=Button(right_frame, text='Generate', font=('Helvetica', 20), bg='#3e4927', fg = "white",command=password_generate)
generate_password_button.pack(fill=X)

#on place notre sous frame à droite de notre frame mère
right_frame.grid(row=0,column=1, sticky=W)
#affichage de notre frame
frame.pack(expand=YES)
#creation barre de menu
nav_Bar=Menu(window)
#creation menu fichier
file_nav=Menu(nav_Bar,tearoff=0)
file_nav.add_command(label="new", command=password_generate)
file_nav.add_command(label="quit", command=window.quit)
nav_Bar.add_cascade(label='File',menu=file_nav)
#configuartion de notre fenetre pourajouter notre menu
window.config(menu=nav_Bar)

# affichage fenetre
window.mainloop()
