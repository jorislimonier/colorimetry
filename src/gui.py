import tkinter as tk
import utils


class HomeGUI:
    def __init__(self, master) -> None:
        self.master = master

        master.title("Colors")
        master.geometry("600x400")

        # Define widgets
        ## Labels
        self.firstname_label = tk.Label(root, text="First name", padx=10)
        self.lastname_label = tk.Label(root, text="Last name", padx=10)
        self.dob_label = tk.Label(root, text="Day of birth", padx=10)
        self.mob_label = tk.Label(root, text="Month of birth", padx=10)
        self.yob_label = tk.Label(root, text="Year of birth", padx=10)
        self.digit_from_name_label = tk.Label(root, padx=10)
        self.digit_from_birthdate_label = tk.Label(root, padx=10)

        ## Entries
        self.firstname_field = tk.Entry()
        self.lastname_field = tk.Entry()
        self.dob_field = tk.Entry()
        self.mob_field = tk.Entry()
        self.yob_field = tk.Entry()

        ## Buttons
        name_button = tk.Button(
            root,
            text="Compute name digit",
            command=self.digit_from_name,
            padx=10,
            pady=10,
        )
        birthdate_button = tk.Button(
            root,
            text="Compute birth date digit",
            command=self.digit_from_birthdate,
            padx=10,
            pady=10,
        )

        # Display widgets
        ## Labels
        self.firstname_label.grid(column=0, row=0, pady=10)
        self.lastname_label.grid(column=0, row=1, pady=10)
        self.dob_label.grid(column=0, row=3, pady=10)
        self.mob_label.grid(column=0, row=4, pady=10)
        self.yob_label.grid(column=0, row=5, pady=10)
        self.digit_from_name_label.grid(column=3, row=9, padx=30)
        self.digit_from_birthdate_label.grid(column=3, row=10, padx=10)

        ## Entries
        self.firstname_field.grid(column=1, row=0)
        self.lastname_field.grid(column=1, row=1)
        self.dob_field.grid(column=1, row=3)
        self.mob_field.grid(column=1, row=4)
        self.yob_field.grid(column=1, row=5)

        ## Buttons
        name_button.grid(column=0, row=9, columnspan=2, pady=30)
        birthdate_button.grid(column=0, row=10, columnspan=2, pady=30)

        ## Canvas
        self.canvas = tk.Canvas()
        self.canvas.grid(column=5, row=4)
        oval_element = self.canvas.create_oval(20,20,100,100,width=2, fill="white")
        self.canvas.grid(column=5, row=4)
        
    def digit_from_name(self):
        self.firstname = self.firstname_field.get()
        self.lastname = self.lastname_field.get()

        reduced_name = utils.digit_from_name(self.firstname + self.lastname)
        self.digit_from_name_label["text"] = f"Your name digit is: {reduced_name}"

    def digit_from_birthdate(self):
        self.dob = self.dob_field.get()
        self.mob = self.mob_field.get()
        self.yob = self.yob_field.get()

        digit_from_birthdate = utils.digit_from_number(self.dob + self.mob + self.yob)
        self.digit_from_birthdate_label[
            "text"
        ] = f"Your birthdate digit is: {digit_from_birthdate}"


if __name__ == "__main__":
    root = tk.Tk()
    home = HomeGUI(root)
    root.mainloop()
