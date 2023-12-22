import tkinter as tk

window = tk.Tk()

window.geometry("1050x700")
window.configure(bg = "#7B96A5")

canvas = tk.Canvas(
    window,
    bg = "#7B96A5",
    height = 700,
    width = 1050,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# Whitespace for the plot
canvas.create_rectangle(
    25.0,
    24.0,
    1025.0,
    474.0,
    fill="#FFFFFF",
    outline="")

# Button Labels
canvas.create_text(
    52.0,
    506.0,
    anchor="nw",
    text="Option Type",
    fill="#000000",
    font=("Helvetica", 20 * -1)
)
canvas.create_text(
    251.0,
    506.0,
    anchor="nw",
    text="Strike",
    fill="#000000",
    font=("Helvetica", 20 * -1)
)
canvas.create_text(
    443.0,
    506.0,
    anchor="nw",
    text="Premium",
    fill="#000000",
    font=("Helvetica", 20 * -1)
)
canvas.create_text(
    650.0,
    506.0,
    anchor="nw",
    text="Position",
    fill="#000000",
    font=("Helvetica", 20 * -1)
)

# Add Option to Position Button
button_addition = tk.Button(
    text="Add",
    font=("Helvetica", 20 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Add button clicked"),
    relief="flat"
)
button_addition.place(
    x=845.0,
    y=506.0,
    width=180.0,
    height=91.0
)

# Clear all Options from Position Button
button_clear = tk.Button(
    text="CE",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Clear Button clicked"),
    relief="flat"
)
button_clear.place(
    x=845.0,
    y=611.0,
    width=180.0,
    height=67.0
)

button_2 = tk.Button(
    text="2",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=47.0,
    y=553.0,
    width=160.0,
    height=44.0
)

button_3 = tk.Button(
    text="3",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=47.0,
    y=611.0,
    width=160.0,
    height=44.0
)

button_4 = tk.Button(
    text="4",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=645.0,
    y=553.0,
    width=160.0,
    height=44.0
)

button_5 = tk.Button(
    text="5",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=645.0,
    y=611.0,
    width=160.0,
    height=44.0
)

# Strike Price Entry Field
entry_strike = tk.Entry(
    font=("Helvetica", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_strike.place(
    x=246.0,
    y=578.0,
    width=160.0,
    height=42.0
)

# Premium Entry Field
entry_premium = tk.Entry(
    font=("Helvetica", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_premium.place(
    x=445.0,
    y=578.0,
    width=160.0,
    height=42.0
)


window.resizable(False, False)
window.mainloop()
