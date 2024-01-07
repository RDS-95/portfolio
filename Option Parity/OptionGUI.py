import tkinter as tk
import optionPosition


# Define Functions for GUI Buttons
def clear_button():
    global current_position
    current_position = optionPosition.OptionPosition()
    current_position.parity_graph()


def add_button():
    option_type = v_option_type.get()
    strike_price = int(entry_strike.get())
    premium = int(entry_premium.get())
    position_type = v_position_type.get()

    current_position.add_option(option_type=option_type,
                                strike_price=strike_price,
                                premium=premium,
                                position_type=position_type)
    current_position.parity_graph()


def create_radio_button(master, text, variable, value, x, y):
    button = tk.Radiobutton(master=master,
                            text=text,
                            font=("Helvetica", 20 * -1),
                            variable=variable,
                            value=value)
    button.place(x=x, y=y, width=160, height=44)
    return button


# Init Interface
root = tk.Tk()
root.geometry("1050x190")
root.configure(bg="#7B96A5")

# Background Canvas
canvas = tk.Canvas(root,
                   bg="#7B96A5",
                   height=200,
                   width=1050,
                   bd=0,
                   highlightthickness=0,
                   relief="ridge")
canvas.place(x=0, y=0)

# Text Labels
canvas.create_text(52, 6, anchor="nw", text="Option Type", fill="#000000", font=("Helvetica", 20 * -1))
canvas.create_text(251, 6, anchor="nw", text="Strike", fill="#000000", font=("Helvetica", 20 * -1))
canvas.create_text(443, 6, anchor="nw", text="Premium", fill="#000000", font=("Helvetica", 20 * -1))
canvas.create_text(650, 6, anchor="nw", text="Position", fill="#000000", font=("Helvetica", 20 * -1))

button_addition = tk.Button(text="Add",
                            font=("Helvetica", 20 * -1),
                            borderwidth=0,
                            highlightthickness=0,
                            command=add_button,
                            relief="flat")
button_addition.place(x=845, y=6, width=180, height=91)

button_clear = tk.Button(text="CE",
                         borderwidth=0,
                         highlightthickness=0,
                         command=clear_button,
                         relief="flat")
button_clear.place(x=845, y=111, width=180, height=67)

v_option_type = tk.StringVar(root, "1")
button_call = create_radio_button(root, "Call", v_option_type, "Call", 47, 53)
button_put = create_radio_button(root, "Put", v_option_type, "Put", 47, 111)

v_position_type = tk.StringVar(root, "2")
button_long = create_radio_button(root, "Long", v_position_type, "Long", 645, 53)
button_short = create_radio_button(root, "Short", v_position_type, "Short", 645, 111)

entry_strike = tk.Entry(font=("Helvetica", 20 * -1), bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_strike.place(x=246, y=78, width=160, height=42)

entry_premium = tk.Entry(font=("Helvetica", 20 * -1), bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_premium.place(x=445, y=78, width=160, height=42)

# Init with empty position variable
current_position = optionPosition.OptionPosition()

root.resizable(False, False)
root.mainloop()
