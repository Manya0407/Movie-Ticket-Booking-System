import tkinter as tk

def save_theatre_details():
    # Dummy function to save theatre details to the database
    theatre_details = {
        "Theatre ID": theatre_id_entry.get(),
        "Theatre Name": theatre_name_entry.get(),
        "Location": location_entry.get()
    }
    # Here you would implement logic to save the theatre details to the database
    print("Theatre details saved:", theatre_details)

# Theatre window
theatre_window = tk.Tk()
theatre_window.title("Theatre Details")
theatre_window.configure(bg="lightyellow")

theatre_id_label = tk.Label(theatre_window, text="Theatre ID: ", bg="lightyellow", fg="black", font=("Helvetica", 14))
theatre_id_label.pack(pady=5)
theatre_id_entry = tk.Entry(theatre_window, font=("Helvetica", 14))
theatre_id_entry.pack(pady=5)

theatre_name_label = tk.Label(theatre_window, text="Theatre Name: ", bg="lightyellow", fg="black", font=("Helvetica", 14))
theatre_name_label.pack(pady=5)
theatre_name_entry = tk.Entry(theatre_window, font=("Helvetica", 14))
theatre_name_entry.pack(pady=5)

location_label = tk.Label(theatre_window, text="Location: ", bg="lightyellow", fg="black", font=("Helvetica", 14))
location_label.pack(pady=5)
location_entry = tk.Entry(theatre_window, font=("Helvetica", 14))
location_entry.pack(pady=5)

save_button = tk.Button(theatre_window, text="Save", command=save_theatre_details, font=("Helvetica", 14))
save_button.pack(pady=10)

theatre_window.mainloop()

