import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random as rn
import pyperclip as pc

SYMBOL_LIMIT = 1000
SYMBOL_LIMIT2 = 50


class PasswordGenerator:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        # Control tab
        control_frame = ttk.Frame(self.root, padding="20 20 20 20")
        control_frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        control_frame.columnconfigure(0, weight=1)

        # Number of symbols
        ttk.Label(control_frame, text="Number of symbols:").grid(column=0, row=0, sticky=(tk.W, tk.S))
        self.entry_symbols = ttk.Entry(control_frame)
        self.entry_symbols.grid(column=0, row=1, sticky=tk.W)

        # Checkbox for symbol types
        ttk.Label(control_frame, text="Symbol types:").grid(column=0, row=2, sticky=(tk.W, tk.S))
        self.var_numbers = tk.BooleanVar()
        self.check_numbers = ttk.Checkbutton(control_frame, text="Numbers", variable=self.var_numbers)
        self.check_numbers.grid(column=0, row=3, sticky=(tk.W, tk.S))
        self.var_letters_lower = tk.BooleanVar()
        self.check_letters_lower = ttk.Checkbutton(control_frame, text="Lowercase letters", variable=self.var_letters_lower)
        self.check_letters_lower.grid(column=0, row=4, sticky=(tk.W, tk.S))
        self.var_letters_upper = tk.BooleanVar()
        self.check_letters_upper = ttk.Checkbutton(control_frame, text="Uppercase letters", variable=self.var_letters_upper)
        self.check_letters_upper.grid(column=0, row=5, sticky=(tk.W, tk.S))
        self.var_other = tk.BooleanVar()
        self.check_other = ttk.Checkbutton(control_frame, text="Other symbols", variable=self.var_other)
        self.check_other.grid(column=0, row=6, sticky=(tk.W, tk.S))

        # Generate password button
        self.button_generate = ttk.Button(control_frame, text="Generate", command=self.generate_multiple_passwords)
        self.button_generate.grid(column=0, row=7, sticky=tk.W)

        # Spacer
        ttk.Label(control_frame, text="").grid(column=0, row=8, sticky=(tk.W, tk.S))

        # Multiple Generations tab
        multi_frame = ttk.Frame(self.root, padding="20 20 20 20")
        multi_frame.grid(row=0, column=1, sticky=(tk.N, tk.W, tk.E, tk.S))
        multi_frame.columnconfigure(0, weight=1)

        # Number of generations
        ttk.Label(multi_frame, text="Number of passwords:").grid(column=0, row=0, sticky=(tk.W, tk.S))
        self.entry_generations = ttk.Entry(multi_frame)
        self.entry_generations.grid(column=0, row=1, sticky=tk.W)

        # Password output
        ttk.Label(multi_frame, text="Generated passwords:").grid(column=0, row=3, sticky=(tk.W, tk.S))
        self.password_list = tk.Listbox(multi_frame)
        self.password_list.grid(column=0, row=4, sticky=(tk.W, tk.E))

        # Copy button
        self.button_copy = ttk.Button(multi_frame, text="Copy", command=self.copy_password)
        self.button_copy.grid(column=0, row=5, sticky=tk.W)

        # Spacer
        ttk.Label(multi_frame, text="").grid(column=0, row=6, sticky=(tk.W, tk.S))

        # Status label
        self.label_copy_success = ttk.Label(multi_frame, text="")
        self.label_copy_success.grid(column=0, row=7, sticky=tk.W)

    def generate_multiple_passwords(self):
        try:
            number_of_passwords = int(self.entry_generations.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for 'Number of passwords'!")
            return

        if number_of_passwords > SYMBOL_LIMIT2:
            messagebox.showerror("Error", "Number of passwords cannot exceed " + str(SYMBOL_LIMIT2) + "!")
            return
        self.password_list.delete(0, tk.END)
        selected_symbols = ''
        if self.var_numbers.get():
            selected_symbols += "1234567890"
        if self.var_letters_lower.get():
            selected_symbols += "abcdefghijklmnopqrstuvwxyz"
        if self.var_letters_upper.get():
            selected_symbols += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.var_other.get():
            selected_symbols += "!@#`~$%^&*()-_+=\|],[{ }',';:/?.>,<№"
        if not selected_symbols or number_of_passwords < 1:
            return

        passwords = []
        for i in range(number_of_passwords):
            try:
                amountOfSymbols = int(self.entry_symbols.get())
                if amountOfSymbols > SYMBOL_LIMIT:
                    messagebox.showerror("Error", "Number of symbols cannot exceed " + str(SYMBOL_LIMIT) + "!")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number for 'Number of symbols'!")
                return
            password = ''.join(rn.choice(selected_symbols) for _ in range(amountOfSymbols))
            passwords.append(password)
        self.password_list.insert(tk.END, *passwords)

    def copy_password(self):
        selected_passwords = [self.password_list.get(i) for i in self.password_list.curselection()]
        if not selected_passwords:
            self.label_copy_success.config(text="No passwords selected!")
            self.root.after(1000, self.clear_copy_success_label)
            return
        pc.copy('\n'.join(selected_passwords))
        self.label_copy_success.config(text="Copied to clipboard!")
        self.root.after(1000, self.clear_copy_success_label)

    def clear_copy_success_label(self):
        self.label_copy_success.config(text="")



if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
