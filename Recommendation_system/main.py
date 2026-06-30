import tkinter as tk
from tkinter import messagebox
from recommender import recommend

def show_recommendations():
    movie_name = movie_entry.get().strip()

    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)

    if movie_name == "":
        messagebox.showwarning("Warning", "Please enter a movie name!")
        return

    recommendations = recommend(movie_name)

    if recommendations is None:
        result_box.insert(
            tk.END,
            "❌ Movie not found!\n\nPlease check the spelling and try again."
        )
    else:
        result_box.insert(
            tk.END,
            "🎯 Top 5 Recommended Movies\n\n"
        )

        for i, movie in enumerate(recommendations, start=1):
            result_box.insert(tk.END, f"🎬 {i}. {movie}\n")

    result_box.config(state="disabled")


def clear_all():
    movie_entry.delete(0, tk.END)
    result_box.config(state="normal")
    result_box.delete(1.0, tk.END)
    result_box.config(state="disabled")

root = tk.Tk()
root.title("AI Movie Recommendation System")
root.geometry("700x550")
root.configure(bg="#0F172A")
root.resizable(False, False)

heading = tk.Label(
    root,
    text="🎬 AI Movie Recommendation System",
    font=("Helvetica", 22, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
heading.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Content-Based Recommendation using TF-IDF & Cosine Similarity",
    font=("Arial", 11),
    bg="#0F172A",
    fg="white"
)
subtitle.pack()

frame = tk.Frame(root, bg="#0F172A")
frame.pack(pady=20)

label = tk.Label(
    frame,
    text="Enter Movie Name:",
    font=("Arial", 12, "bold"),
    bg="#0F172A",
    fg="white"
)
label.grid(row=0, column=0, padx=10)

movie_entry = tk.Entry(
    frame,
    font=("Arial", 12),
    width=30,
    bd=3
)
movie_entry.grid(row=0, column=1)

button_frame = tk.Frame(root, bg="#0F172A")
button_frame.pack()

recommend_btn = tk.Button(
    button_frame,
    text="🎯 Recommend",
    font=("Arial", 12, "bold"),
    bg="#22C55E",
    fg="white",
    width=15,
    command=show_recommendations
)
recommend_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="🧹 Clear",
    font=("Arial", 12, "bold"),
    bg="#F59E0B",
    fg="white",
    width=12,
    command=clear_all
)
clear_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(
    button_frame,
    text="❌ Exit",
    font=("Arial", 12, "bold"),
    bg="#EF4444",
    fg="white",
    width=12,
    command=root.destroy
)
exit_btn.grid(row=0, column=2, padx=10)

output_label = tk.Label(
    root,
    text="Recommendations",
    font=("Arial", 14, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
)
output_label.pack(pady=10)

result_box = tk.Text(
    root,
    width=60,
    height=12,
    font=("Consolas", 11),
    bg="#E2E8F0",
    fg="black",
    bd=3
)

result_box.pack()
result_box.config(state="disabled")

footer = tk.Label(
    root,
    text="Developed for CodeSoft AI Internship",
    font=("Arial", 10),
    bg="#0F172A",
    fg="lightgray"
)
footer.pack(pady=15)

root.mainloop()