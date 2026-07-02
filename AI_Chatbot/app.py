import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_response
from datetime import datetime

def current_time():
    return datetime.now().strftime("%I:%M %p")


def send_message(event=None):
    message = entry.get().strip()

    if message == "" or message == "Type your message here...":
        return

    if message == placeholder:
        return

    entry.delete(0, tk.END)

    chat.config(state=tk.NORMAL)

    # User Message
    chat.insert(
        tk.END,
        f"👤 You ({current_time()})\n",
        "user_name"
    )
    chat.insert(
        tk.END,
        f"{message}\n\n",
        "user_msg"
    )

    chat.insert(
        tk.END,
        "🤖 CodBot is typing...\n\n",
        "typing"
    )

    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)

    root.after(900, lambda: show_response(message))


def show_response(message):

    response = get_response(message)

    chat.config(state=tk.NORMAL)

    chat.delete("end-3l", "end")

    chat.insert(
        tk.END,
        f"🤖 CodBot ({current_time()})\n",
        "bot_name"
    )

    chat.insert(
        tk.END,
        f"{response}\n\n",
        "bot_msg"
    )

    chat.config(state=tk.DISABLED)
    chat.yview(tk.END)


def clear_chat():

    chat.config(state=tk.NORMAL)
    chat.delete(1.0, tk.END)

    chat.insert(
        tk.END,
        "🤖 Welcome to CodBot\n",
        "title"
    )

    chat.insert(
        tk.END,
        "\nHello!\n\n"
        "I am your Rule-Based AI Chatbot.\n\n"
        "You can ask me about:\n"
        "• Time\n"
        "• Date\n"
        "• My Name\n"
        "• Who created me\n"
        "• Greetings\n\n"
        "Start chatting below!\n\n",
        "bot_msg"
    )

    chat.config(state=tk.DISABLED)


def clear_placeholder(event):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg="black")


def add_placeholder(event):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="gray")

root = tk.Tk()
root.title("CodBot - AI Rule-Based Chatbot")
root.geometry("700x720")
root.resizable(False, False)
root.configure(bg="#F5F7FA")

header = tk.Label(
    root,
    text="🤖 CodBot - AI Rule-Based Chatbot",
    bg="#4F46E5",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    pady=15
)

header.pack(fill=tk.X)

chat = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Segoe UI", 11),
    bg="white",
    fg="black",
    padx=12,
    pady=12,
    relief=tk.FLAT
)

chat.pack(
    padx=15,
    pady=15,
    fill=tk.BOTH,
    expand=True
)

chat.tag_config("title",
                foreground="#4F46E5",
                font=("Segoe UI", 16, "bold"))

chat.tag_config("user_name",
                foreground="#2563EB",
                font=("Segoe UI", 11, "bold"))

chat.tag_config("bot_name",
                foreground="#059669",
                font=("Segoe UI", 11, "bold"))

chat.tag_config("user_msg",
                foreground="black",
                spacing3=10)

chat.tag_config("bot_msg",
                foreground="#222222",
                spacing3=15)

chat.tag_config("typing",
                foreground="gray",
                font=("Segoe UI", 10, "italic"))

chat.config(state=tk.NORMAL)

chat.insert(
    tk.END,
    "🤖 Welcome to CodBot\n",
    "title"
)

chat.insert(
    tk.END,
    "\nHello!\n\n"
    "I am your AI Rule-Based Chatbot.\n\n"
    "Things you can ask:\n"
    "• Hi\n"
    "• Time\n"
    "• Date\n"
    "• My Name\n"
    "• Help\n"
    "• Bye\n\n"
    "Enjoy chatting!\n\n",
    "bot_msg"
)

chat.config(state=tk.DISABLED)

bottom = tk.Frame(root, bg="#F5F7FA")
bottom.pack(fill=tk.X, padx=15, pady=10)

placeholder = "Type your message here..."

entry = tk.Entry(
    bottom,
    font=("Segoe UI", 11),
    width=40,
    relief=tk.FLAT,
    bd=8,
    fg="gray"
)

entry.insert(0, placeholder)

entry.bind("<FocusIn>", clear_placeholder)
entry.bind("<FocusOut>", add_placeholder)
entry.bind("<Return>", send_message)

entry.pack(side=tk.LEFT, padx=(0, 10), ipady=7)

send_btn = tk.Button(
    bottom,
    text="Send",
    bg="#10B981",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=6,
    relief=tk.FLAT,
    command=send_message
)

send_btn.pack(side=tk.LEFT)

clear_btn = tk.Button(
    bottom,
    text="Clear",
    bg="#EF4444",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=6,
    relief=tk.FLAT,
    command=clear_chat
)

clear_btn.pack(side=tk.LEFT, padx=10)

entry.focus()

root.mainloop()