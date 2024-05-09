import tkinter as tk

def save_customer_details():
    # Dummy function to save customer details to the database
    customer_details = {
        "Customer ID": customer_id_entry.get(),
        "Date of Birth": dob_entry.get(),
        "Email": email_entry.get(),
        "Mobile": mobile_entry.get()
    }
    # Here you would implement logic to save the customer details to the database
    print("Customer details saved:", customer_details)

# Customer window
customer_window = tk.Tk()
customer_window.title("Customer Details")
customer_window.configure(bg="lightgreen")

customer_id_label = tk.Label(customer_window, text="Customer ID: ", bg="lightgreen", fg="black", font=("Helvetica", 14))
customer_id_label.pack(pady=5)
customer_id_entry = tk.Entry(customer_window, font=("Helvetica", 14))
customer_id_entry.pack(pady=5)

dob_label = tk.Label(customer_window, text="Date of Birth: ", bg="lightgreen", fg="black", font=("Helvetica", 14))
dob_label.pack(pady=5)
dob_entry = tk.Entry(customer_window, font=("Helvetica", 14))
dob_entry.pack(pady=5)

email_label = tk.Label(customer_window, text="Email: ", bg="lightgreen", fg="black", font=("Helvetica", 14))
email_label.pack(pady=5)
email_entry = tk.Entry(customer_window, font=("Helvetica", 14))
email_entry.pack(pady=5)

mobile_label = tk.Label(customer_window, text="Mobile: ", bg="lightgreen", fg="black", font=("Helvetica", 14))
mobile_label.pack(pady=5)
mobile_entry = tk.Entry(customer_window, font=("Helvetica", 14))
mobile_entry.pack(pady=5)

save_button = tk.Button(customer_window, text="Save", command=save_customer_details, font=("Helvetica", 14))
save_button.pack(pady=10)

customer_window.mainloop()

