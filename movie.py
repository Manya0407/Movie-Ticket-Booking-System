import tkinter as tk

def save_movie_details():
    # Dummy function to save movie details to the database
    movie_details = {
        "Movie Title": movie_title_entry.get(),
        "Movie Stars": movie_stars_entry.get(),
        "Movie Description": movie_description_entry.get(),
        "Screen No": screen_no_entry.get(),
        "Theatre ID": theatre_id_entry.get(),
        "Seats": seats_entry.get()
    }
    # Here you would implement logic to save the movie details to the database
    print("Movie details saved:", movie_details)

# Movie window
movie_window = tk.Tk()
movie_window.title("Movie Details")
movie_window.configure(bg="lightcoral")

movie_title_label = tk.Label(movie_window, text="Movie Title: ", bg="lightcoral", fg="black", font=("Helvetica", 14))
movie_title_label.pack(pady=5)
movie_title_entry = tk.Entry(movie_window, font=("Helvetica", 14))
movie_title_entry.pack(pady=5)

movie_stars_label = tk.Label(movie_window, text="Movie Stars: ", bg="lightcoral", fg="black", font=("Helvetica", 14))
movie_stars_label.pack(pady=5)
movie_stars_entry = tk.Entry(movie_window, font=("Helvetica", 14))
movie_stars_entry.pack(pady=5)

movie_description_label = tk.Label(movie_window, text="Movie Description: ", bg="lightcoral", fg="black", font=("Helvetica", 14))
movie_description_label.pack(pady=5)
movie_description_entry = tk.Entry(movie_window, font=("Helvetica", 14))
movie_description_entry.pack(pady=5)

screen_no_label = tk.Label(movie_window, text="Screen No: ", bg="lightcoral", fg="black", font=("Helvetica", 14))
screen_no_label.pack(pady=5)
screen_no_entry = tk.Entry(movie_window, font=("Helvetica", 14))
screen_no_entry.pack(pady=5)

theatre_id_label = tk.Label(movie_window, text="Theatre ID: ", bg="lightcoral", fg="black", font=("Helvetica", 14))
theatre_id_label.pack(pady=5)
theatre_id_entry = tk.Entry(movie_window, font=("Helvetica", 14))
theatre_id_entry.pack(pady=5)

seats_label = tk.Label(movie_window, text="Seats: ", bg="lightcoral", fg="black", font=("Helvetica", 14))
seats_label.pack(pady=5)
seats_entry = tk.Entry(movie_window, font=("Helvetica", 14))
seats_entry.pack(pady=5)

save_button = tk.Button(movie_window, text="Save", command=save_movie_details, font=("Helvetica", 14))
save_button.pack(pady=10)

movie_window.mainloop()

