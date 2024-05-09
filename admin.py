import tkinter as tk

def get_admin_name():
    # Dummy function to simulate retrieving admin name from admin ID
    admin_id = admin_id_entry.get()
    # Here you can implement logic to fetch admin name from database or any other source
    # For demo purposes, let's just return a hardcoded name based on admin ID
    if admin_id == "123":
        admin_name = "John Doe"
    elif admin_id == "456":
        admin_name = "Jane Smith"
    else:
        admin_name = "Unknown"

    result_label.config(text=admin_name, fg="green", font=("Helvetica", 14))

# Main window
root = tk.Tk()
root.title("Admin Name Lookup")
root.configure(bg="lightblue")

admin_id_label = tk.Label(root, text="Admin ID: ", bg="lightblue", fg="black", font=("Helvetica", 14))
admin_id_label.pack(pady=10)

admin_id_entry = tk.Entry(root, font=("Helvetica", 14))
admin_id_entry.pack(pady=10)

lookup_button = tk.Button(root, text="Lookup Admin Name", command=get_admin_name, font=("Helvetica", 14))
lookup_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="lightblue", fg="black", font=("Helvetica", 16))
result_label.pack(pady=10)

root.mainloop()




