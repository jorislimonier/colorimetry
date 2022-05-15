import tkinter as tk
import utils

class HomeGUI:
    def __init__(self, master) -> None:
        
        self.master = master

        master.title("Colors")
        master.geometry("600x400")

        # Define widgets
        ## Labels
        self.first_name_label = tk.Label(root, text="First name", padx=10)
        self.last_name_label = tk.Label(root, text="Last name", padx=10)
        self.dob_label = tk.Label(root, text="Day of birth", padx=10)
        self.mob_label = tk.Label(root, text="Month of birth", padx=10)
        self.yob_label = tk.Label(root, text="Year of birth", padx=10)
        self.reduced_name_label = tk.Label(root, padx=10)

        ## Entries
        self.first_name_field = tk.Entry()
        self.last_name_field = tk.Entry()
        self.dob_field = tk.Entry()
        self.mob_field = tk.Entry()
        self.yob_field = tk.Entry()

        ## Buttons
        button = tk.Button(
            root,
            text="Compute name digit",
            command=self.digit_from_name,
            padx=10,
            pady=10,
        )


        # Display widgets
        ## Labels
        self.first_name_label.grid(column=0, row=0, pady=10)
        self.last_name_label.grid(column=0, row=1, pady=10)
        self.dob_label.grid(column=0, row=3, pady=10)
        self.mob_label.grid(column=0, row=4, pady=10)
        self.yob_label.grid(column=0, row=5, pady=10)
        self.reduced_name_label.grid(column=3, row=9)

        ## Entries
        self.first_name_field.grid(column=1, row=0)
        self.last_name_field.grid(column=1, row=1)
        self.dob_field.grid(column=1, row=3)
        self.mob_field.grid(column=1, row=4)
        self.yob_field.grid(column=1, row=5)
        ## Buttons
        button.grid(column=0, row=9, columnspan=2, pady=30)

    def digit_from_name(self):
        global first_name
        first_name = self.first_name_field.get()

        global last_name
        last_name = self.last_name_field.get()
        reduced_name = utils.name_to_reduced_number(first_name + last_name)
        self.reduced_name_label["text"] = f"Your name digit is: {reduced_name}"




root = tk.Tk()
home = HomeGUI(root)
root.mainloop()
