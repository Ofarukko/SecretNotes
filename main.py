import tkinter
import base64
import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


#encode_function
def encode(key, clear):
    enc = []

    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) +
                     ord(key_c)) % 256)

        enc.append(enc_c)

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#decrypt_function
def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
    return "".join(dec)

# get value and encrypt
def function1():
    t = entry1.get()
    s = textbox1.get("1.0",END)
    m = entry2.get()

    if t == "" or s == "" or m == "":
        messagebox.showerror(title="ERROR!",message="Please Enter All Informations !")

    else:
        message_encrypted = encode(m,s)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{t}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{t}\n{message_encrypted}")
        finally:
            entry1.delete(0,END)
            entry2.delete(0,END)
            textbox1.delete("1.0",END)

# decode secret
def function2():
    m_encrypted = textbox1.get("1.0",END)
    master_secret = entry2.get()

    if m_encrypted == "" or master_secret == "" :
        messagebox.showerror(title="ERROR!",message="Please Enter All Informations !")
    else:
        try:
            dec_secret = decode(master_secret,m_encrypted)
            textbox1.delete("1.0",END)
            textbox1.insert("1.0",dec_secret)
        except:
            tkinter.messagebox.showerror(title="ERROR!",message="Please Enter Your Encrypted Message !")

#screen
screen = Tk()
screen.title("Secret Notes")
screen.config(padx=20,pady=20)

#image
img = Image.open('photo.png')
img = ImageTk.PhotoImage(img)

#image_label
image_label = tkinter.Label(image=img)
image_label.config(width=300,height=200)
image_label.pack()

#label1
label1 = tkinter.Label()
label1.config(text="Enter Your Title: ")
label1.config(font=("Arial",14,"bold"))
label1.pack()

#title_entry
entry1 = tkinter.Entry(width=30)
entry1.pack()

#label2
label2 = tkinter.Label(text="Enter Your Secret: ")
label2.config(font=("Arial",14,"bold"))
label2.pack()

#textbox
textbox1= tkinter.Text()
textbox1.config(width=50,height=20)
textbox1.pack()

#label3
label3 = tkinter.Label(text="Enter Master KEY: ")
label3.config(font=("Arial",14,"bold"))
label3.pack()

#key_entry
entry2 = tkinter.Entry(width=30)
entry2.pack()

#save_button
save_button = tkinter.Button(text="Save & Encrypt",command=function1)
save_button.config(font=("Arial",13,"normal"))
save_button.config(fg="red",bg="yellow")
save_button.pack()

#Decrypt_button
decrypt_button = tkinter.Button(text="Decrypt",command=function2)
decrypt_button.config(font=("Arial",13,"normal"))
decrypt_button.config(fg="yellow",bg="red")
decrypt_button.pack()


screen.mainloop()