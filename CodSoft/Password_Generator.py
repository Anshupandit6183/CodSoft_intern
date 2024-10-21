import tkinter as tk
import pyperclip
import random

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password_length = int(password_length_entry.get())
    password = "".join(random.choices(characters, k=password_length))
    password_entry.config(state="normal")  
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly") 

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)
    clipboard_label.config(text="Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#8a5454")  


password_length_label = tk.Label(root, text="Enter password length:", bg="Green")
password_length_label.pack(pady=10)
password_length_entry = tk.Entry(root, width=20)
password_length_entry.pack(pady=5)


generate_password_button = tk.Button(root, text="Generate Password", command=generate_password, bg="Brown") 
generate_password_button.pack(pady=10)


password_entry = tk.Entry(root, width=40, state="readonly") 
password_entry.pack(pady=10)


copy_clipboard_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="Brown")
copy_clipboard_button.pack(pady=10)


clipboard_label = tk.Label(root, text="", bg="Yellow")
clipboard_label.pack(pady=5)

root.mainloop()