from tkinter import *

class App:
    def __init__(self, master):
        self.master = master
        self.master.title('Easy Ticket')
        self.master.geometry("400x400")

        self.cellno_lbl = Label(master, text="Enter Cell Number:").place(x=10, y=30)
        self.cellno_entry = Entry(master).place(x=200, y=30)

        self.category_lbl = Label(master, text="Select Ticket Category:").place(x=10, y=80)
        self.options = ["Select Ticket", "Soccer", "Movie", "Theatre"]
        self.click = StringVar()
        self.click.set((self.options[0]))
        self.category_list = OptionMenu(master, self.click, *self.options).place(x=200, y=74)

        self.tickets_bought = Label(master, text="Number Of Tickets Bought:").place(x=10, y=130)
        self.bought_entry = Entry(master).place(x=200, y=130)

        # My buttons
        self.calculate_button = Button(master, text="Calculate Ticket").place(x=10, y=180)
        self.clear_button = Button(master, text="Clear Entries").place(x=200, y=180)

        # Output section
        self.lb1 = Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx").place(x=10, y=230)
        self.payable = Label(master, text="Amount Payable: ").place(x=10, y=260)
        self.payable_output = Label(master, text="R1000").place(x=180, y=260)
        self.reservation = Label(master, text="Reservation: ").place(x=10, y=290)
        self.reservation_output = Label(master, text="Soccer").place(x=180, y=290)
        self.number = Label(master, text="Was done by: ").place(x=10, y=320)
        self.number = Label(master, text="0860010111").place(x=180, y=320)
        self.lb2 = Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx").place(x=10, y=350)


root = Tk()
app = App(root)
root.mainloop()
