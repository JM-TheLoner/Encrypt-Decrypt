from tkinter import *
from tkinter import messagebox
import base64

root=Tk()
root.overrideredirect(1)
root.withdraw()
messagebox.showinfo("INFO", "Set Passkey in Terminal")
root.destroy()

passkey = input("Set Passkey: ")

def encrypt():
    password = code.get()

    if password==passkey:
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ED3833")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ED3833").place(x=10,y=0)
        text2=Text(screen1, font="rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,height=150,width=380)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("Encryption", "Input Password")

    elif password != passkey:
        messagebox.showerror("Encryption", "Invalid Password")

        
def decrypt():
    password = code.get()

    if password==passkey:
        screen2=Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00BD56")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00BD56").place(x=10,y=0)
        text2=Text(screen2, font="rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,height=150,width=380)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("Decryption", "Input Password")

    elif password != passkey:
        messagebox.showerror("Decryption", "Invalid Password")


def cryptic():

    global screen
    global code
    global text1

    screen=Tk()
    screen.title("Cryptic Message")
    screen.config(bg="#E6E6E6")
    screen.geometry("375x398")
    screen.resizable(False, False)

    image_icon=PhotoImage(file="Py_Project Directory\kindpng.png")     #put the image you wish to use in this directory
    screen.iconphoto(False, image_icon)

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter Text", fg="black", font=("calibri", 13, "bold"), bg="#F2F2F2").place(x=10, y=10)       #text entry
    text1=Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0, border=3)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter Secret key", fg="black", font=("calibri", 10, "bold"), bg="#F2F2F2").place(x=10, y=170)     #Passcode entry
    
    code=StringVar()
    Entry(width=19, font=("arial", 25), textvariable=code, bd=0, show="*", border=2).place(x=10, y=200)

    Button(text="ENCRYPT",width=23,bg="#ED3833",fg="white", height=2, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT",width=23,bg="#00BD56",fg="white",height=2, command=decrypt).place(x=200, y=250)
    Button(text="RESET",width=50,bg="#1089FF",fg="white",height=2, command=reset).place(x=10, y=300)

    screen.mainloop()

cryptic()