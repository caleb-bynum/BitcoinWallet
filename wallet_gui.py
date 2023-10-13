import tkinter as tk
from tkinter import ttk
import random

class SimpleBitcoinWallet(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Bitcoin Wallet")
        self.geometry("600x400")

        # Colors
        self.bg_color = "#2C2F33"
        self.text_color = "#FFFFFF"
        self.button_color = "#7289DA"
        self.entry_color = "#40444B"

        self.configure(bg=self.bg_color)

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self, text="Simple Bitcoin Wallet", font=("Arial", 16), bg=self.bg_color, fg=self.text_color)
        title_label.pack(pady=10)

        # Address Section
        addr_label = tk.Label(self, text="Your Address: ", bg=self.bg_color, fg=self.text_color)
        addr_label.pack(anchor="w", padx=10, pady=5)
        
        self.address_var = tk.StringVar(self)
        addr_entry = tk.Entry(self, textvariable=self.address_var, state='readonly', width=40, bg=self.entry_color, fg=self.entry_color)
        addr_entry.pack(padx=10, pady=5)

        gen_button = tk.Button(self, text="Generate New Address", command=self.generateAddress, bg=self.button_color, fg=self.text_color)
        gen_button.pack(padx=10, pady=5)

        # Send Transaction Section
        send_frame = tk.Frame(self, bg=self.bg_color)
        send_frame.pack(padx=10, pady=10, fill="x")

        send_label = tk.Label(send_frame, text="Send Transaction: ", font=("Arial", 14), bg=self.bg_color, fg=self.text_color)
        send_label.grid(row=0, column=0, pady=5, columnspan=2)

        to_label = tk.Label(send_frame, text="To: ", bg=self.bg_color, fg=self.text_color)
        to_label.grid(row=1, column=0, sticky="e", padx=5)
        self.to_var = tk.StringVar()
        to_entry = tk.Entry(send_frame, textvariable=self.to_var, width=40, bg=self.entry_color, fg=self.text_color)
        to_entry.grid(row=1, column=1, padx=5)

        amt_label = tk.Label(send_frame, text="Amount: ", bg=self.bg_color, fg=self.text_color)
        amt_label.grid(row=2, column=0, sticky="e", padx=5)
        self.amount_var = tk.StringVar()
        amount_entry = tk.Entry(send_frame, textvariable=self.amount_var, width=20, bg=self.entry_color, fg=self.text_color)
        amount_entry.grid(row=2, column=1, sticky="w", padx=5)

        send_button = tk.Button(send_frame, text="Send", command=self.sendTransaction, bg=self.button_color, fg=self.text_color)
        send_button.grid(row=3, column=1, sticky="e", padx=5, pady=5)

        # Transaction History Section
        hist_label = tk.Label(self, text="Transaction History: ", font=("Arial", 14), bg=self.bg_color, fg=self.text_color)
        hist_label.pack(anchor="w", padx=10, pady=5)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", background=self.entry_color, fieldbackground=self.entry_color, foreground=self.text_color)
        style.map('Treeview', background=[('selected', self.button_color)])

        self.history_tree = ttk.Treeview(self, columns=("To", "Amount"), height=5)
        self.history_tree.pack(padx=10, pady=5, fill="x")
        self.history_tree.heading("#0", text="Tx ID")
        self.history_tree.column("#0", width=100)
        self.history_tree.heading("To", text="To")
        self.history_tree.column("To", width=200)
        self.history_tree.heading("Amount", text="Amount")
        self.history_tree.column("Amount", width=100)

    def generateAddress(self):
        hexstring = hex(random.randint(0, 16**8))[2:]
        self.address_var.set(hexstring)

    def sendTransaction(self):
        to = self.to_var.get()
        amount = self.amount_var.get()

        self.history_tree.insert("", "end", text="abcd1234", values=(to, amount))
        self.to_var.set("")
        self.amount_var.set("")

if __name__ == "__main__":
    app = SimpleBitcoinWallet()
    app.mainloop()
