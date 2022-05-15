import tkinter as tk
import utils


root = tk.Tk()
root.title("Colors")
root.geometry("1000x400")


def store_name():
    global first_name
    first_name = first_name_field.get()

    global last_name
    last_name = last_name_field.get()
    reduced_name = utils.name_to_reduced_number(first_name + last_name)
    reduced_name_label["text"] = f"Reduced name {reduced_name}"


# Define widgets
## Labels
first_name_label = tk.Label(root, text="First name", padx=10)
last_name_label = tk.Label(root, text="Last name", padx=10)
reduced_name_label = tk.Label(root, text="", padx=10)

## Entries
first_name_field = tk.Entry()
last_name_field = tk.Entry()

## Buttons
button = tk.Button(
    root,
    text="Compute number from name",
    command=store_name,
    padx=10,
    pady=10,
)

# Display widgets

## Labels
first_name_label.grid(column=0, row=0)
last_name_label.grid(column=3, row=0)
reduced_name_label.grid(column=2, row=9)

## Entries
button.grid(column=0, row=1, columnspan=9)

## Buttons
first_name_field.grid(column=1, row=0)
last_name_field.grid(column=4, row=0)


root.mainloop()
