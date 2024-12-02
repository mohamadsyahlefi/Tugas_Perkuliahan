import tkinter as tk
from tkinter import messagebox


class BankAccount:
    def __init__(self):
        self.__balance = 0 # Private attribute
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Invalid deposit amount!")

    def add_balance(self):
        try:
            amount = int(entry_amount.get())
            account.deposit(amount)
            label_balance.config(text=f"Balance: {account.get_balance()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def reset_input(self):
        entry_amount.delete(0, tk.END)  # Menghapus input di entry_amount

# GUI Tkinter
root = tk.Tk()
root.title("Data Hiding in BankAccount")

account = BankAccount()

label_balance = tk.Label(root, text=f"Balance: {account.get_balance()}")
label_balance.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

button_deposit = tk.Button(root, text="Deposit", command=account.add_balance)
button_deposit.pack()

button_reset = tk.Button(root, text="Reset Input", command=account.reset_input)
button_reset.pack()

root.mainloop()