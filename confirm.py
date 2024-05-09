import tkinter as tk

def confirm_ticket():
    confirmation_window = tk.Toplevel()
    confirmation_window.title("Confirmation Window")
    confirmation_window.configure(bg="lightblue")

    confirmation_label = tk.Label(confirmation_window, text="Ticket Confirmed!", bg="lightblue", fg="green")
    confirmation_label.pack()

# Main window
root = tk.Tk()
root.title("Main Window")

confirmation_button = tk.Button(root, text="Confirm Ticket", command=confirm_ticket)
confirmation_button.pack()

root.mainloop()
