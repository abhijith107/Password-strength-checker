import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include at least one digit.")

    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")

    common_patterns = ["password", "123456", "123456789", "12345678", "12345", "qwerty","abcde","987654",]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Password should not contain common patterns (e.g., 'password', '123456').")
        score -= 1

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

def on_check_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)
    strength_label.config(text=f"Password Strength: {strength}")
    feedback_listbox.delete(0, tk.END)
    for suggestion in feedback:
        feedback_listbox.insert(tk.END, suggestion)














root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter your password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

check_button = tk.Button(root, text="Check Password", command=on_check_password)
check_button.pack()

strength_label = tk.Label(root, text="Password Strength: ")
strength_label.pack()

feedback_label = tk.Label(root, text="Suggestions to improve your password:")
feedback_label.pack()

feedback_listbox = tk.Listbox(root, width=50, height=10)
feedback_listbox.pack()

root.mainloop()
