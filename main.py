import tkinter as tk
import random as rn

def generate_password():
    numberOfSymbols = int(entry_symbols.get())
    symbolLimit = 100
    symbolLimit2 = 0

    typesOfSymbols = var_symbols.get()
    if typesOfSymbols == "1":
        label_symbol_type.config(text="Symbol type: numbers")
        symbolUnsorted = "1234567890"
    elif typesOfSymbols == "2":
        label_symbol_type.config(text="Symbol type: letters")
        symbolUnsorted = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif typesOfSymbols == "3":
        label_symbol_type.config(text="Symbol type: other")
        symbolUnsorted = "!@#`~$%^&*()-_+=\|],[{ }',';:/?.>,<№"

    if numberOfSymbols > symbolLimit:
        label_result.config(text="This number is higher than the limit.")
    elif numberOfSymbols < symbolLimit2:
        label_result.config(text="This number is lower than the limit.")
    else:
        symvols = list(symbolUnsorted)
        generated_password = ""
        for _ in range(numberOfSymbols):
            generated_password += rn.choice(symvols)
        label_result.config(text="Your password is: " + generated_password)
        
root = tk.Tk()
root.title("Password Generator")

label_symbols = tk.Label(root, text="Write the number of symbols:")
label_symbols.pack()
entry_symbols = tk.Entry(root)
entry_symbols.pack()

label_type = tk.Label(root, text="Choose what type of symbols you want to use:")
label_type.pack()

var_symbols = tk.StringVar()
var_symbols.set("1")

radio_numbers = tk.Radiobutton(root, text="Numbers", variable=var_symbols, value="1")
radio_numbers.pack()

radio_letters = tk.Radiobutton(root, text="Letters", variable=var_symbols, value="2")
radio_letters.pack()

radio_other = tk.Radiobutton(root, text="Other", variable=var_symbols, value="3")
radio_other.pack()

button_generate = tk.Button(root, text="Generate", command=generate_password)
button_generate.pack()

label_symbol_type = tk.Label(root, text="")
label_symbol_type.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
