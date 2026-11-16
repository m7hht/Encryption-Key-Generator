import base64
import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Made By Matthew J Colman

KEY_TYPES = [
    "Hex (AES-128, 16 bytes)",
    "Hex (AES-256, 32 bytes)",
    "Base64 (32 bytes, Fernet-compatible)",
    "Alphanumeric (custom length)",
    "Raw bytes as hex (custom length)",
]

def generate_key(index, length=32):
    if index == 0:
        return secrets.token_hex(16)
    if index == 1:
        return secrets.token_hex(32)
    if index == 2:
        return base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
    if index == 3:
        chars = string.ascii_letters + string.digits
        return "".join(secrets.choice(chars) for _ in range(length))
    return secrets.token_bytes(length).hex()

def on_generate():
    index = KEY_TYPES.index(type_var.get())
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number for length.")
        return
    if length < 1:
        messagebox.showerror("Error", "Length must be at least 1.")
        return
    result_var.set(generate_key(index, length))

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())

def on_close():
    if messagebox.askyesno("Confirm", "Are you sure you want to close?"):
        root.destroy()

root = tk.Tk()
root.title("Key Generator")
root.protocol("WM_DELETE_WINDOW", on_close)

tk.Label(root, text="Key type:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
type_var = tk.StringVar(value=KEY_TYPES[0])
tk.OptionMenu(root, type_var, *KEY_TYPES).grid(row=0, column=1, sticky="w", pady=5)

tk.Label(root, text="Length (types 4 and 5):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root, width=6)
length_entry.insert(0, "32")
length_entry.grid(row=1, column=1, sticky="w", pady=5)

tk.Button(root, text="Generate", command=on_generate).grid(row=2, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=50, justify="center").grid(row=3, column=0, columnspan=2, padx=10)

tk.Button(root, text="Copy", command=on_copy).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
# Made By Matthew J Colman
