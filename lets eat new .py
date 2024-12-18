import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog
import tkinter as tk
from tkinter import messagebox, simpledialog
import tkinter as tk
from tkinter import messagebox


user_db = {}  # Format: {"username": {"password": password, "email": email}}

def navigate_to(option):
    if option == "Book a Table":
        show_booking_page()  # Show the restaurant table booking page in the same window
    else:
        messagebox.showinfo("Navigation", f"You clicked on {option}")

def init_home_page():
    global root
    root = tk.Tk()
    root.title("Let's Eat")
    root.geometry("800x600")  # Initial window size

    navbar_frame = tk.Frame(root, bg="#161B21", height=40)  # Navbar frame with background color #684121
    navbar_frame.pack(side="top", fill="x")  # Fill the top of the window

    title_label = tk.Label(
        navbar_frame,
        text="Let's Eat",
        font=("Arial", 16, "bold"),
        bg="#161B21",
        fg="#F4A950",
    )
    title_label.pack(side="left", padx=20, pady=5)

    bg_image_pil = Image.open("C:/Zukun/new/rest.jpg")  # Replace with your image file path
    bg_image_pil=bg_image_pil.resize((900,600),Image.Resampling.LANCZOS)
    bg_image_tk = ImageTk.PhotoImage(bg_image_pil)
    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(fill="both", expand=True)  # Make the canvas expand to fill the window
    bg_image_item = canvas.create_image(0, 0, image=bg_image_tk, anchor="nw")

    booking_button = tk.Button(
        root,
        text="Book a Table",
        font=("Arial", 14, "bold"),
        bg="#F4A950",
        fg="#161B21",
        command=lambda: navigate_to("Book a Table"),  # Navigate to "Book a Table"
    )
    canvas.create_window(400, 200, window=booking_button)

    admin_button = tk.Button(
        root,
        text="Admin Login",
        font=("Arial", 14, "bold"),
        bg="#F4A950",
        fg="#161B21",
        command=open_admin_page,  # Open admin login page
    )
    canvas.create_window(400, 280, window=admin_button)

    def resize_bg(event):
        new_width = event.width
        new_height = event.height
        resized_image = bg_image_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_image_resized = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(bg_image_item, image=bg_image_resized)
        canvas.image = bg_image_resized  # Save reference to avoid garbage collection

    root.bind("<Configure>", resize_bg)
    root.mainloop()

def show_booking_page():
    for widget in root.winfo_children():
        widget.destroy()

    bg_image_pil = Image.open("C:/Zukun/new/rest1.jpg")  # Update with your image file path
    bg_image_tk = ImageTk.PhotoImage(bg_image_pil)

    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    bg_image_item = canvas.create_image(0, 0, image=bg_image_tk, anchor="nw")

    def resize_bg(event):
        new_width = event.width
        new_height = event.height
        resized_image = bg_image_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_image_resized = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(bg_image_item, image=bg_image_resized)
        canvas.image = bg_image_resized

    root.bind("<Configure>", resize_bg)

    navbar_frame = tk.Frame(canvas, bg="#161B21", height=40)
    canvas.create_window(0, 0, anchor="nw", window=navbar_frame, width=root.winfo_width())

    back_button = tk.Button(
        navbar_frame,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        bg="#F4A950",
        fg="#161B21",
        command=lambda: [root.destroy(), init_home_page()],
    )
    back_button.pack(side="right", padx=20, pady=5)

    title_label = tk.Label(
        navbar_frame,
        text="Restaurant Table Booking",
        font=("Arial", 16, "bold"),
        bg="#161B21",
        fg="#F4A950",
    )
    title_label.pack(side="left", padx=20, pady=5)
    categories = ["Family", "Couples", "Friends"]
    category_label = tk.Label(
        canvas,
        text="Select a Table Category",
        font=("Arial", 16, "bold"),
        bg="#161B21",
        fg="#F4A950",  # Background color
    )
    canvas.create_window(400, 80, anchor="center", window=category_label)

    y_position = 150
    for category in categories:
        category_button = tk.Button(
            canvas,
            text=f"{category} Tables",
            font=("Arial", 14, "bold"),
            bg="#F4A950",
            fg="#161B21",
            command=lambda cat=category: show_tables_for_category(cat),
        )
        canvas.create_window(400, y_position, anchor="center", window=category_button, width=200, height=50)
        y_position += 70

    canvas.bg_image_tk = bg_image_tk
    root.mainloop()

def show_tables_for_category(category):
    """Show tables for the selected category."""
    for widget in root.winfo_children():
        widget.destroy()

    bg_image_pil = Image.open("C:/Zukun/new/rest1.jpg")
    bg_image_tk = ImageTk.PhotoImage(bg_image_pil)

    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    bg_image_item = canvas.create_image(0, 0, image=bg_image_tk, anchor="nw")

    def resize_bg(event):
        new_width = event.width
        new_height = event.height
        resized_image = bg_image_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_image_resized = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(bg_image_item, image=bg_image_resized)
        canvas.image = bg_image_resized

    root.bind("<Configure>", resize_bg)

    navbar_frame = tk.Frame(canvas, bg="#161B21", height=40)
    canvas.create_window(0, 0, anchor="nw", window=navbar_frame, width=root.winfo_width())

    back_button = tk.Button(
        navbar_frame,
        text="Back to Table",
        font=("Arial", 12, "bold"),
        bg="#F4A950",
        fg="#161B21",
        command=show_booking_page,  # Navigate back
    )
    back_button.pack(side="right", padx=20, pady=5)

    category_label = tk.Label(
        root,
        text=f"Select a Table for {category}",
        font=("Arial", 16, "bold"),
        fg="#161B21",
        bg="#F4A950",  # Background color
    )
    canvas.create_window(400, 70, anchor="center", window=category_label)

    chairs_per_table = {"Couples": 2, "Family": 5, "Friends": 8}
    available_chairs = chairs_per_table[category]
    y_position = 120

    for i in range(1, 6):
        table_button = tk.Button(
            canvas,
            text=f"{category} Table {i} - Available Chairs: {available_chairs}",
            font=("Arial", 14, "bold"),
            bg="#161B21",
            fg="#F4A950",
            command=lambda table=f"{category} Table {i}": show_booking_button(table, available_chairs, category),
        )
        canvas.create_window(400, y_position, anchor="center", window=table_button, width=350, height=50)
        y_position += 70

    canvas.bg_image_tk = bg_image_tk

def show_booking_button(table_name, available_chairs, category):
    """Display the booking button for a selected table."""
    messagebox.showinfo(
        "Booking Selection",
        f"Table Selected: {table_name}\nAvailable Chairs: {available_chairs}\nCategory: {category}",
    )

from tkcalendar import DateEntry
from tkinter import ttk
from datetime import datetime



def show_booking_button(table_name, available_chairs, category):
    for widget in root.winfo_children():
        widget.destroy()
 
    root.configure(bg="#F4A950")
    navbar_frame = tk.Frame(root, bg="#161B21", height=40)
    navbar_frame.pack(side="top", fill="x")

    back_button = tk.Button(
        navbar_frame,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        fg="#161B21",
        bg="#F4A950",
        command=lambda: [root.destroy(), init_home_page()],
    )
    back_button.pack(side="right", padx=20, pady=5)

    back_to_tables_button = tk.Button(
        navbar_frame,
        text="Back to Tables",
        font=("Arial", 12, "bold"),
        fg="#161B21",
        bg="#F4A950",
        command=lambda: show_tables_for_category(category),
    )
    back_to_tables_button.pack(side="left", padx=20, pady=5)

    table_label = tk.Label(
        root,
        text=f"Selected {table_name}",
        font=("Arial", 16, "bold"),
        fg="black",
        bg="#F4A950",  # Background color
    )
    table_label.pack(pady=20)

    available_chairs_label = tk.Label(
        root,
        text=f"Available Chairs: {available_chairs}",
        font=("Arial", 12),
        fg="black",
        bg="#F4A950",  # Background color
    )
    available_chairs_label.pack(pady=10)

    booking_button = tk.Button(
        root,
        text="Proceed to Booking",
        font=("Arial", 14, "bold"),
        fg="#F4A950",
        bg="#161B21",
        command=lambda: show_booking_form(table_name),
    )
    booking_button.pack(pady=20)

# Sample user database
import json
import os

USER_DB_FILE = "users.json"

# Load user database from file
def load_user_db():
    if os.path.exists(USER_DB_FILE):
        with open(USER_DB_FILE, "r") as file:
            return json.load(file)
    return {}  # Return an empty dictionary if file doesn't exist

# Save user database to file
def save_user_db():
    with open(USER_DB_FILE, "w") as file:
        json.dump(user_db, file, indent=4)

user_db = load_user_db()


def open_forgot_password_page():
    forgot_password_window = tk.Tk()
    forgot_password_window.title("Forgot Password")
    forgot_password_window.geometry("400x400")
    forgot_password_window.configure(bg="#F4A950")

    navbar = tk.Frame(forgot_password_window, bg="#161B21", height=40)
    navbar.pack(fill="x")

    nav_label = tk.Label(navbar, text="Forgot Password", bg="#161B21", fg="#F4A950", font=("Arial", 14, "bold"))
    nav_label.pack(pady=5)

    tk.Label(forgot_password_window, text="Enter Username:", font=("Arial", 12), bg="#F4A950", fg="#161B21").pack(pady=10)
    username_entry = tk.Entry(forgot_password_window, font=("Arial", 12))
    username_entry.pack(pady=5)

    def reset_password():
        username = username_entry.get()

        if username not in user_db:
            messagebox.showerror("Error", "Username not found. Please check and try again.")
        else:
            new_password = simpledialog.askstring("New Password", "Enter new password:", show="*")
            if new_password:
                user_db[username]["password"] = new_password
                messagebox.showinfo("Password Reset", f"Password for {username} has been successfully reset.")
                forgot_password_window.destroy()
            else:
                messagebox.showerror("Error", "Password cannot be empty.")
    tk.Button(forgot_password_window, text="Reset Password", font=("Arial", 12, "bold"),bg="#161B21" ,fg="#F4A950", command=reset_password).pack(pady=20)
    forgot_password_window.mainloop()


# Sample user database
user_db = {}

def open_create_account_page():
    # Create a new window for creating an account
    create_account_window = tk.Tk()
    create_account_window.title("Create New Account")
    create_account_window.geometry("400x400")

    # Set background color
    create_account_window.configure(bg="#F4A950")

    # Add navbar
    navbar = tk.Frame(create_account_window, bg="#161B21", height=40)
    navbar.pack(fill="x")

    nav_label = tk.Label(navbar, text="Create Account", bg="#161B21", fg="#F4A950", font=("Arial", 14, "bold"))
    nav_label.pack(pady=5)

    # Add form fields
    tk.Label(create_account_window, text="Enter Username:", font=("Arial", 12), bg="#F4A950").pack(pady=10)
    username_entry = tk.Entry(create_account_window, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(create_account_window, text="Enter Password:", font=("Arial", 12), bg="#F4A950").pack(pady=10)
    password_entry = tk.Entry(create_account_window, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    tk.Label(create_account_window, text="Enter Email:", font=("Arial", 12), bg="#F4A950").pack(pady=10)
    email_entry = tk.Entry(create_account_window, font=("Arial", 12))
    email_entry.pack(pady=5)

    def create_account():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()

        if username in user_db:
            messagebox.showerror("Account Creation Failed", "Username already exists. Please choose another one.")
        elif not username or not password or not email:
            messagebox.showerror("Account Creation Failed", "All fields are required.")
        else:
            user_db[username] = {"password": password, "email": email}
            messagebox.showinfo("Account Created", f"Account for {username} has been created successfully!")
            create_account_window.destroy()
    tk.Button(create_account_window, text="Create Account", font=("Arial", 12, "bold"),bg="#161B21" ,fg="#F4A950", command=create_account).pack(pady=20)
    create_account_window.mainloop()

import smtplib
from tkinter import messagebox
from requests import Session as Client
from dotenv import load_dotenv
import os
import smtplib
from tkinter import messagebox
from twilio.rest import Client


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def open_admin_page():
    root.destroy()
    admin_root = tk.Tk()
    admin_root.title("Admin Login")
    admin_root.geometry("800x600")
    admin_root.config()

    bg_image_pil = Image.open("C:/Zukun/new/rest1.jpg")  # Replace with your image file path
    bg_image_tk = ImageTk.PhotoImage(bg_image_pil)

    canvas = tk.Canvas(admin_root, highlightthickness=0)
    canvas.pack(fill="both", expand=True)  # Make the canvas expand to fill the window
    bg_image_item = canvas.create_image(0, 0, image=bg_image_tk, anchor="nw")

    def resize_bg(event):
        new_width = event.width
        new_height = event.height
        resized_image = bg_image_pil.resize((new_width, new_height), Image.Resampling.LANCZOS)
        bg_image_resized = ImageTk.PhotoImage(resized_image)
        canvas.itemconfig(bg_image_item, image=bg_image_resized)
        canvas.image = bg_image_resized  # Save reference to avoid garbage collection

    admin_root.bind("<Configure>", resize_bg)
    navbar_frame = tk.Frame(admin_root, bg="#161B21", height=40)
    navbar_frame.pack(side="top", fill="x")

    back_button = tk.Button(
        navbar_frame,
        text="Back to Home",
        font=("Arial", 12, "bold"),
        fg="#161B21",
        bg="#F4A950",
        command=lambda: [admin_root.destroy(), init_home_page()],
    )
    back_button.pack(side="right", padx=20, pady=5)

    title_label = tk.Label(
        navbar_frame,
        text="Admin Login",
        font=("Arial", 16, "bold"),
        fg="#F4A950",
        bg="#161B21",
    )
    title_label.pack(side="left", padx=20, pady=5)

    label_font = ("Arial", 14, "bold")
    entry_font = ("Arial", 12)
    button_font = ("Arial", 12, "bold")
    login_frame = tk.Frame(admin_root, bg="#F4A950", bd=5)
    login_frame.place(x=150, y=150, width=300, height=400)

    tk.Label(login_frame, text="Username", font=label_font, bg="#F4A950").pack(pady=10)
    username_entry = tk.Entry(login_frame, font=entry_font)
    username_entry.pack(pady=5, ipadx=5, ipady=5)

    tk.Label(login_frame, text="Password", font=label_font, bg="#F4A950").pack(pady=10)
    password_entry = tk.Entry(login_frame, show="*", font=entry_font)
    password_entry.pack(pady=5, ipadx=5, ipady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username in user_db and user_db[username]["password"] == password:
            messagebox.showinfo("Login", f"Welcome, {username}!")
            show_dashboard(admin_root)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    tk.Button(
        login_frame,
        text="Login",
        font=button_font,
        fg="#F4A950",
        bg="#161B21",
        command=login,
    ).pack(pady=20, ipadx=10, ipady=5)

    tk.Button(
        login_frame,
        text="Create Account",
        font=button_font,
        fg="#F4A950",
        bg="#161B21",
        command=open_create_account_page,
    ).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(
        login_frame,
        text="Forgot Password?",
        font=button_font,
        fg="#F4A950",
        bg="#161B21",
        command=open_forgot_password_page,
    ).pack(pady=10, ipadx=10, ipady=5)

    admin_root.mainloop()

BOOKINGS_FILE = "bookings.json"

# Load existing bookings

def load_bookings():
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as file:
            return json.load(file)
    return []

# Save bookings
def save_bookings(bookings):
    with open(BOOKINGS_FILE, "w") as file:
        json.dump(bookings, file, indent=4)

# Email Confirmation
def send_email_confirmation(email, name, table_name, date, time):
    try:
        sender_email = "kannandurvas@gmail.com"  # Replace with actual sender email
        sender_password = "xshj mmbp puis sfwu"       # Replace with actual password
        subject = "Booking Confirmation"
        body = f"Dear {name},\n\nYour table booking has been confirmed!\nTable: {table_name}\nDate: {date}\nTime: {time}\n\nThank you for choosing us!"

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(sender_email, email, message)

        messagebox.showinfo("Email Confirmation", f"Confirmation email sent to {email}.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# Confirm Booking
def confirm_booking(name, contact, email, date, time, table_name):
    if not all([name, contact, email, date, time]):
        messagebox.showerror("Error", "All fields are required.")
        return

    bookings = load_bookings()
    booking = {
        "name": name,
        "contact": contact,
        "email": email,
        "date": date,
        "time": time,
        "table_name": table_name
    }
    bookings.append(booking)
    save_bookings(bookings)

    send_email_confirmation(email, name, table_name, date, time)
    messagebox.showinfo("Booking Confirmed", f"Booking confirmed for {name} at {date}, {time} on {table_name}.")

# Send Email from Dashboard
def send_email_from_dashboard(selected_item):
    if not selected_item:
        messagebox.showerror("Error", "No booking selected.")
        return

    bookings = load_bookings()
    booking = bookings[int(selected_item) - 1]  # Convert index to list position
    send_email_confirmation(
        booking["email"],
        booking["name"],
        booking["table_name"],
        booking["date"],
        booking["time"]
    )

# Show Dashboard
def show_dashboard(admin_root):
    dashboard_window = tk.Tk()
    dashboard_window.title("Booking Dashboard")
    dashboard_window.geometry("800x600")

    navbar_frame = tk.Frame(dashboard_window, bg="#161B21", height=40)
    navbar_frame.pack(side="top", fill="x")

    title_label = tk.Label(
        navbar_frame,
        text="Booking Dashboard",
        font=("Arial", 16, "bold"),
        bg="#161B21",
        fg="#F4A950",
    )
    title_label.pack(side="left", padx=20, pady=5)

    # Table for displaying bookings
    columns = ("Index", "Name", "Contact", "Email", "Date", "Time", "Table")
    tree = ttk.Treeview(dashboard_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    bookings = load_bookings()
    for idx, booking in enumerate(bookings, start=1):
        tree.insert("", "end", values=(
            idx,
            booking["name"],
            booking["contact"],
            booking["email"],
            booking["date"],
            booking["time"],
            booking["table_name"]
        ))

    tree.pack(fill="both", expand=True, padx=20, pady=20)

    def on_send_email():
        selected_item = tree.item(tree.selection())['values'][0] if tree.selection() else None
        send_email_from_dashboard(selected_item)

    send_email_button = tk.Button(
        dashboard_window,
        text="Send Confirmation Email",
        font=("Arial", 12, "bold"),
        bg="#F4A950",
        fg="#161B21",
        command=on_send_email
    )
    send_email_button.pack(pady=10)

    dashboard_window.mainloop()

# Booking Form
def show_booking_form(table_name):
    form_window = tk.Tk()
    form_window.title("Book a Table")
    form_window.geometry("400x500")
    form_window.configure(bg="#F4A950")

    tk.Label(form_window, text=f"Booking for {table_name}", font=("Arial", 16, "bold"), bg="#F4A950").pack(pady=20)

    tk.Label(form_window, text="Enter Name:", font=("Arial", 12), bg="#F4A950").pack(pady=5)
    name_entry = tk.Entry(form_window, font=("Arial", 12))
    name_entry.pack(pady=5)

    tk.Label(form_window, text="Enter Contact Number:", font=("Arial", 12), bg="#F4A950").pack(pady=5)
    contact_entry = tk.Entry(form_window, font=("Arial", 12))
    contact_entry.pack(pady=5)

    tk.Label(form_window, text="Enter Email ID:", font=("Arial", 12), bg="#F4A950").pack(pady=5)
    email_entry = tk.Entry(form_window, font=("Arial", 12))
    email_entry.pack(pady=5)

    tk.Label(form_window, text="Select Date:", font=("Arial", 12), bg="#F4A950").pack(pady=5)
    date_entry = DateEntry(form_window, font=("Arial", 12), mindate=datetime.now())
    date_entry.pack(pady=5)

    tk.Label(form_window, text="Select Time:", font=("Arial", 12), bg="#F4A950").pack(pady=5)
    time_entry = ttk.Combobox(form_window, font=("Arial", 12), state="readonly")
    time_entry["values"] = [f"{hour:02d}:00" for hour in range(9, 22)]
    time_entry.pack(pady=5)

    tk.Button(
        form_window,
        text="Confirm Booking",
        font=("Arial", 14, "bold"),
        bg="#161B21",
        fg="#F4A950",
        command=lambda: confirm_booking(
            name_entry.get(),
            contact_entry.get(),
            email_entry.get(),
            date_entry.get(),
            time_entry.get(),
            table_name
        ),
    ).pack(pady=20)

    form_window.mainloop()



init_home_page()
