#  libraries
import random
import tkinter as tk
import tkinter.ttk as ttk

#  functions


def make_password():
    password_length = entry.get()
    entry2.delete(0, tk.END)
    if int(password_length) < 4:
        entry2.insert(0, "Entry must be more than 4 digits")
    else:
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_chars = "!@#$%^&*()"
        all_chars = lowercase_letters + uppercase_letters + numbers + special_chars
        password = random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars) + \
                    random.choice(all_chars)
        for i in range(int(password_length) - 4):  # Subtract 4 because we already added 4 characters
            password += random.choice(all_chars)
        password = ''.join(random.sample(password, len(password)))
        entry2.insert(0, password)


def save_password():
    text = entry2.get()
    password_list.insert(tk.END, text)
    entry2.delete(0, tk.END)


def on_close():
    with open('password.txt', 'w') as f:
        password_items = password_list.get(0, 'end')
        for item in password_items:
            f.write(item + '\n')
    root2.destroy()


def delete_password():
    try:
        selection = list(password_list.curselection())[::-1]
        for index in selection:
            password_list.delete(index)
    except IndexError:
        pass


# tk start
root2 = tk.Tk()

# window fixtures
root2.title("Password Generator")
root2.geometry("200x350+100+100")
root2.configure()

# entry for amount of characters for password
label = ttk.Label(root2, text="Enter Number:",)
label.pack()
entry = ttk.Entry(root2)
entry.pack()

# button
button = ttk.Button(root2, text="Generate Password", command=make_password)
button.pack()

entry2 = ttk.Entry(root2)
entry2.pack()

# saving password
save_button = ttk.Button(root2, text='Save Password', command=save_password)
save_button.pack()
password_label = ttk.Label(root2, text='Saved Passwords',)
password_label.pack()
password_list = tk.Listbox(root2, selectmode=tk.MULTIPLE, )
password_list.pack()

try:
    # Open the file in read mode ('r')
    with open('password.txt', 'r') as f:
        lines = f.readlines()
        # Add each line to the listbox
        for line in lines:
            # Strip off the newline character at the end of the line before adding it to the listbox
            password_list.insert('end', line.strip())
except FileNotFoundError:
    # If the file doesn't exist, skip loading the tasks.
    # The file will be created when you save for the first time.
    pass

# delete password button
delete_pass = ttk.Button(root2, text='Delete Password', command=delete_password)
delete_pass.pack()

root2.protocol("WM_DELETE_WINDOW", on_close)

# mainloop
root2.mainloop()
