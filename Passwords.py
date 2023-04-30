import tkinter
import ttkbootstrap
import random


root = tkinter.Tk()
root.title("Password generator")
root.geometry("240x340")
root.resizable(width=False,height=False)


signs = '1234567890!$%@QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm'

def generatepasswords():
    n_passwords = number_of_passwords.get()
    pwd_length = password_length.get()
    if not n_passwords.isdigit() or not pwd_length.isdigit():
        def popupok():
            popup.destroy()
        popup = tkinter.Toplevel()
        popup.title("Error")
        popup.geometry("200x100")
        popup_label = tkinter.Label(popup, text="Please enter valid integer values.")
        popup_label.pack()
        ok= ttkbootstrap.Button(popup,text="OK",bootstyle="danger",command=popupok)
        ok.pack(anchor="center",side="bottom")

    else:
        n_passwords = int(n_passwords)
        pwd_length = int(pwd_length)
        passwords = []
        for i in range(n_passwords):
            password = ""
            for j in range(pwd_length):
                password += random.choice(signs)
            passwords.append(password)
        password_text = '\n'.join(passwords)
        password_list.config(state='normal')
        password_list.delete('1.0', tkinter.END)
        password_list.insert(tkinter.END, password_text)
        password_list.config(state='disabled')
        password_list.place(anchor="center",x=120,y=250)

number_label = ttkbootstrap.Label(root, text="Number of passwords:", bootstyle="dark")
number_label.place(anchor="center",x=120,y=20)
password_label = ttkbootstrap.Label(root, text="Password length:", bootstyle="dark")
password_label.place(anchor="center",x=120,y=80)

number_of_passwords = ttkbootstrap.Entry(root,bootstyle="secondary")
number_of_passwords.place(anchor="center",x=120,y=50)
password_length= ttkbootstrap.Entry(root,bootstyle="secondary")
password_length.place(anchor="center",x=120,y=105)

generateButton = ttkbootstrap.Button(bootstyle="success",text="Generate",command=generatepasswords).place(anchor="center",x=120,y=140)
password_list = ttkbootstrap.Text(root, height=10, width=30, state='disabled')
password_list.place(anchor="center",x=120,y=250)


root.mainloop()