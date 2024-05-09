import tkinter as tk

def save_ticket_details():
    # Dummy function to save ticket details to the database
    ticket_details = {
        "Ticket ID": ticket_id_entry.get(),
        "Show ID": show_id_entry.get(),
        "Screen No": screen_no_entry.get(),
        "Seat No": seat_no_entry.get(),
        "Start Time": start_time_entry.get(),
        "End Time": end_time_entry.get(),
        "Date": date_entry.get()
    }
    # Here you would implement logic to save the ticket details to the database
    print("Ticket details saved:", ticket_details)

# Ticket window
ticket_window = tk.Tk()
ticket_window.title("Ticket Details")
ticket_window.configure(bg="lightgrey")

ticket_id_label = tk.Label(ticket_window, text="Ticket ID: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
ticket_id_label.pack(pady=5)
ticket_id_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
ticket_id_entry.pack(pady=5)

show_id_label = tk.Label(ticket_window, text="Show ID: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
show_id_label.pack(pady=5)
show_id_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
show_id_entry.pack(pady=5)

screen_no_label = tk.Label(ticket_window, text="Screen No: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
screen_no_label.pack(pady=5)
screen_no_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
screen_no_entry.pack(pady=5)

seat_no_label = tk.Label(ticket_window, text="Seat No: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
seat_no_label.pack(pady=5)
seat_no_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
seat_no_entry.pack(pady=5)

start_time_label = tk.Label(ticket_window, text="Start Time: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
start_time_label.pack(pady=5)
start_time_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
start_time_entry.pack(pady=5)

end_time_label = tk.Label(ticket_window, text="End Time: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
end_time_label.pack(pady=5)
end_time_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
end_time_entry.pack(pady=5)

date_label = tk.Label(ticket_window, text="Date: ", bg="lightgrey", fg="black", font=("Helvetica", 14))
date_label.pack(pady=5)
date_entry = tk.Entry(ticket_window, font=("Helvetica", 14))
date_entry.pack(pady=5)

save_button = tk.Button(ticket_window, text="Save", command=save_ticket_details, font=("Helvetica", 14))
save_button.pack(pady=10)

ticket_window.mainloop()
