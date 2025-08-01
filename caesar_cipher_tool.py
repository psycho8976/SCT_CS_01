import tkinter as tk
from tkinter import filedialog, messagebox

# Caesar Cipher Core Logic
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# GUI Functions
def process_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_entry.get()
    mode = mode_var.get()

    if not shift.isdigit():
        messagebox.showerror("Invalid Input", "Shift value must be a number.")
        return

    shift = int(shift)
    output = caesar_cipher(text, shift, mode)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

def load_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read())

def save_file():
    text = output_text.get("1.0", tk.END).strip()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)
        messagebox.showinfo("Success", "File saved successfully.")

# GUI Layout
window = tk.Tk()
window.title("Caesar Cipher Tool")
window.geometry("600x500")  # Reduced window size for a compact look
window.config(bg="#23272f")

# Labels and Inputs
tk.Label(window, text="Enter Text:", bg="#23272f", fg="#4CAF50", font=("Helvetica", 15, "bold")).pack(pady=(15, 6))

input_frame = tk.Frame(window, bg="#23272f")
input_frame.pack(pady=3)

input_text = tk.Text(
    input_frame,
    height=3,      # Smaller height
    width=35,      # Smaller width
    bg="white",
    fg="black",
    font=("Helvetica", 13),
    relief=tk.RIDGE,
    bd=2,
    highlightthickness=1,
    highlightbackground="#4CAF50",
    highlightcolor="#2196F3"
)
input_text.pack(padx=6, pady=3)

tk.Label(window, text="Shift Value:", bg="#23272f", fg="white", font=("Helvetica", 13, "bold")).pack(pady=3)
shift_entry = tk.Entry(window, width=10, font=("Helvetica", 12))
shift_entry.pack(pady=5)

mode_var = tk.StringVar(value="encrypt")
mode_frame = tk.Frame(window, bg="#23272f")
mode_frame.pack(pady=3)
tk.Radiobutton(
    mode_frame,
    text="Encrypt",
    variable=mode_var,
    value="encrypt",
    bg="#23272f",
    fg="white",
    font=("Helvetica", 12),
    indicatoron=True,
    selectcolor="#4CAF50",
    padx=8,
    pady=2
).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(
    mode_frame,
    text="Decrypt",
    variable=mode_var,
    value="decrypt",
    bg="#23272f",
    fg="white",
    font=("Helvetica", 12),
    indicatoron=True,
    selectcolor="#4CAF50",
    padx=8,
    pady=2
).pack(side=tk.LEFT, padx=10)

tk.Button(window, text="Run", command=process_text, bg="#4CAF50", fg="white", font=("Helvetica", 13, "bold"), width=16, height=1).pack(pady=10)

# Output
tk.Label(window, text="Output:", bg="#23272f", fg="#4CAF50", font=("Helvetica", 15, "bold")).pack(pady=6)

output_frame = tk.Frame(window, bg="#23272f")
output_frame.pack(pady=3)

output_text = tk.Text(
    output_frame,
    height=4,
    width=35,
    bg="white",
    fg="black",
    font=("Helvetica", 13),
    relief=tk.RIDGE,
    bd=2,
    highlightthickness=1,
    highlightbackground="#FF9800",
    highlightcolor="#2196F3"
)
output_text.pack(padx=6, pady=3)

# File Buttons
btn_frame = tk.Frame(window, bg="#23272f")
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Load from File", command=load_file, bg="#2196F3", fg="white", font=("Helvetica", 12), width=16, height=1).pack(side=tk.LEFT, padx=6)
tk.Button(btn_frame, text="Save Output to File", command=save_file, bg="#FF9800", fg="white", font=("Helvetica", 12), width=16, height=1).pack(side=tk.LEFT, padx=6)

window.mainloop()
