import tkinter as tk
import Joking


root = tk.Tk()
root.title("Combobox Example")

# Create Combobox
options = ("Option 1", "Option 2", "Option 3")
combo = tk.Combobox(root, values=options, state="readonly")
combo.pack(pady=20)

# Set default value
combo.current(0)

# Get selected value
def show_selected():
    print("Selected:", combo.get())

tk.Button(root, text="Show Selection", command=show_selected).pack()

root.mainloop()
joks=Joking.random_joke()
print(joks)
