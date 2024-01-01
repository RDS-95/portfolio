import tkinter as tk
import optionPosition
from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

###################

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Option Parity Graphs")
        self.geometry("1050x700")
        self.configure(bg="#7B96A5")
        self.current_position = optionPosition.OptionPosition()

    # Button Functions

    def make_graph(pos):
        canvas = FigureCanvasTkAgg(pos.parity_graph(), master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def clear_button():
        current_position = optionPosition.OptionPosition()
        make_graph(current_position)

    def add_button():
        current_position.add_option(
            option_type=v_option_type.get(),
            strike_price=int(entry_strike.get()),
            premium=int(entry_premium.get()),
            position_type=v_position_type.get()
        )
        make_graph(current_position)



########################

current_position = optionPosition.OptionPosition()

# Graphing Function for the Frame
def make_graph(pos):
    canvas = FigureCanvasTkAgg(pos.parity_graph(), master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def clear_button():
    current_position = optionPosition.OptionPosition()
    make_graph(current_position)

def add_button():
    current_position.add_option(
        option_type = v_option_type.get(),
        strike_price = int(entry_strike.get()),
        premium = int(entry_premium.get()),
        position_type = v_position_type.get()
    )
    make_graph(current_position)

# Setting up the master window.
root = tk.Tk()
root.wm_title("Option Parity Graphs")
root.geometry("1050x700")
root.configure(bg = "#7B96A5")

# Background Colour
canvas = tk.Canvas(
    root,
    bg = "#7B96A5",
    height = 700,
    width = 1050,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

# Whitespace for the plot
plot_frame = tk.Frame(root, width=1000, height=450, bg="white", highlightthickness=0)
plot_frame.place(x = 20, y = 20)

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
    command=add_button,
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
    command=clear_button,
    relief="flat"
)
button_clear.place(
    x=845.0,
    y=611.0,
    width=180.0,
    height=67.0
)

# Radio Buttons for Option Type
v_option_type = tk.StringVar(root, "1")
button_call = tk.Radiobutton(
    master=root,
    text="Call",
    font=("Helvetica", 20 * -1),
    variable=v_option_type,
    value="Call"
)
button_call.place(
    x=47.0,
    y=553.0,
    width=160.0,
    height=44.0
)

button_put = tk.Radiobutton(
    master=root,
    text="Put",
    font=("Helvetica", 20 * -1),
    variable=v_option_type,
    value="Put"
)
button_put.place(
    x=47.0,
    y=611.0,
    width=160.0,
    height=44.0
)

v_position_type = tk.StringVar(root, "2")

button_long = tk.Radiobutton(
    master=root,
    text="Long",
    font=("Helvetica", 20 * -1),
    variable=v_position_type,
    value="Long"
)
button_long.place(
    x=645.0,
    y=553.0,
    width=160.0,
    height=44.0
)

button_short = tk.Radiobutton(
    master=root,
    text="Short",
    font=("Helvetica", 20 * -1),
    variable=v_position_type,
    value="Short"
)
button_short.place(
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


root.resizable(False, False)
root.mainloop()
