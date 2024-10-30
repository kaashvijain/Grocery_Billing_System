import mysql.connector
from tabulate import tabulate
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Database connection
db = mysql.connector.connect(host="localhost",
                             user="root",
                             password="sd8823@SQL",
                             database="term1")
cur = db.cursor()

# Functions
def show_connectivity():
    if db.is_connected():
        messagebox.showinfo("Connection", "Connection successful")
    else:
        messagebox.showerror("Connection", "Not connected")

def create_table():
    cur.execute("Create table groceri(prod_no int primary key, prod_name varchar(100), prod_price int, prod_quantity int)")
    db.commit()
    messagebox.showinfo("Table", "Table has been created")

def insert():
    def submit():
        try:
            no = int(no_entry.get())
            na = name_entry.get()
            p = float(price_entry.get())
            q = int(quantity_entry.get())
            query = "insert into groceri values({}, '{}', {}, {})".format(no, na, p, q)
            cur.execute(query)
            db.commit()
            messagebox.showinfo("Insert", "Record inserted successfully")
        except:
            messagebox.showerror("Error", "Error! Please enter the records again")

    insert_window = tk.Toplevel(root)
    insert_window.title("Insert Record")

    tk.Label(insert_window, text="Product Number:").grid(row=0, column=0)
    no_entry = tk.Entry(insert_window)
    no_entry.grid(row=0, column=1)

    tk.Label(insert_window, text="Product Name:").grid(row=1, column=0)
    name_entry = tk.Entry(insert_window)
    name_entry.grid(row=1, column=1)

    tk.Label(insert_window, text="Price:").grid(row=2, column=0)
    price_entry = tk.Entry(insert_window)
    price_entry.grid(row=2, column=1)

    tk.Label(insert_window, text="Quantity:").grid(row=3, column=0)
    quantity_entry = tk.Entry(insert_window)
    quantity_entry.grid(row=3, column=1)

    submit_button = tk.Button(insert_window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

def display():
    try:
        list = []
        query = "select * from groceri"
        cur.execute(query)
        for i in cur:
            list.append(i)
        display_window = tk.Toplevel(root)
        display_window.title("Display Records")

        tree = ttk.Treeview(display_window)#used to create the widgets in which we input our records for products
        tree["columns"] = ("prod_no", "prod_name", "prod_price", "prod_quantity")

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("prod_no", anchor=tk.W, width=100)
        tree.column("prod_name", anchor=tk.W, width=200)
        tree.column("prod_price", anchor=tk.W, width=100)
        tree.column("prod_quantity", anchor=tk.W, width=100)

        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("prod_no", text="Product Number", anchor=tk.W)
        tree.heading("prod_name", text="Product Name", anchor=tk.W)
        tree.heading("prod_price", text="Price", anchor=tk.W)
        tree.heading("prod_quantity", text="Quantity", anchor=tk.W)

        for i in list:
            tree.insert("", "end", values=i)

        tree.pack()
    except:
        messagebox.showerror("Error", "Error!")

def delete():
    def submit():
        try:
            no = int(no_entry.get())
            query = "delete from groceri where prod_no={}".format(no)
            cur.execute(query)
            db.commit()
            messagebox.showinfo("Delete", "Record deleted successfully")
        except:
            messagebox.showerror("Error", "Error! Please enter the records again")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Record")

    tk.Label(delete_window, text="Product Number:").grid(row=0, column=0)
    no_entry = tk.Entry(delete_window)
    no_entry.grid(row=0, column=1)

    submit_button = tk.Button(delete_window, text="Submit", command=submit)
    submit_button.grid(row=1, column=0, columnspan=2)

def update():
    def submit():
        try:
            no = int(no_entry.get())
            na = name_entry.get()
            p = float(price_entry.get())
            q = int(quantity_entry.get())
            query = "update groceri set prod_name='{}', prod_price={}, prod_quantity={} where prod_no={}".format(na, p, q, no)
            cur.execute(query)
            db.commit ()
            messagebox.showinfo("Update", "Record updated successfully")
        except:
            messagebox.showerror("Error", "Error! Please enter the records again")

    update_window = tk.Toplevel(root)
    update_window.title("Update Record")

    tk.Label(update_window, text=" Product Number:").grid(row=0, column=0)
    no_entry = tk.Entry(update_window)
    no_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Product Name:").grid(row=1, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=1, column=1)

    tk.Label(update_window, text="Price:").grid(row=2, column=0)
    price_entry = tk.Entry(update_window)
    price_entry.grid(row=2, column=1)

    tk.Label(update_window, text="Quantity:").grid(row=3, column=0)
    quantity_entry = tk.Entry(update_window)
    quantity_entry.grid(row=3, column=1)

    submit_button = tk.Button(update_window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

def search():
    def submit():
        try:
            no = int(no_entry.get())
            query = "select * from groceri where prod_no={}".format(no)
            cur.execute(query)
            for i in cur:
                messagebox.showinfo("Search", str(i))
        except:
            messagebox.showerror("Error", "Error! Please enter the records again")

    search_window = tk.Toplevel(root)
    search_window.title("Search Record")

    tk.Label(search_window, text="Product Number:").grid(row=0, column=0)
    no_entry = tk.Entry(search_window)
    no_entry.grid(row=0, column=1)

    submit_button = tk.Button(search_window, text="Submit", command=submit)
    submit_button.grid(row=1, column=0, columnspan=2)

def bill():
    def submit():
        try:
            no = int(no_entry.get())
            q = int(quantity_entry.get())
            query = "select * from groceri where prod_no={}".format(no)
            cur.execute(query)
            for i in cur:
                p = i[2]
                t = p * q
                messagebox.showinfo("Bill", "The total amount to be paid is: " + str(t))
        except:
            messagebox.showerror("Error", "Error! Please enter the records again")

    bill_window = tk.Toplevel(root)
    bill_window.title("Generate Bill")

    tk.Label(bill_window, text="Product Number:").grid(row=0, column=0)
    no_entry = tk.Entry(bill_window)
    no_entry.grid(row=0, column=1)

    tk.Label(bill_window, text="Quantity:").grid(row=1, column=0)
    quantity_entry = tk.Entry(bill_window)
    quantity_entry.grid(row=1, column=1)

    submit_button = tk.Button(bill_window, text="Submit", command=submit)
    submit_button.grid(row=2, column=0, columnspan=2)

def happy_hour():#gives 20% discount to any product of the user's choosing
    def submit():
        try:
            no = int(no_entry.get())
            query = "select prod_price from groceri where prod_no={}".format(no)
            cur.execute(query)
            price = cur.fetchone()[0]
            discount_price = price * 0.8
            messagebox.showinfo("Happy Hour", "Discounted price: {}".format(discount_price))
        except:
            messagebox.showerror("Error", "Error! Please enter the records again")

    happy_hour_window = tk.Toplevel(root)
    happy_hour_window.title("Happy Hour")

    tk.Label(happy_hour_window, text="Product Number:").grid(row=0, column=0)
    no_entry = tk.Entry(happy_hour_window)
    no_entry.grid(row=0, column=1)

    submit_button = tk.Button(happy_hour_window, text="Submit", command=submit)
    submit_button.grid(row=1, column=0, columnspan=2)

# GUI
root = tk.Tk()
root.title("Grocery Billing System")

# Load the background image
image = Image.open("groceri_bg.jpg")
photo = ImageTk.PhotoImage(image)

# Create a frame to hold the widgets
frame = tk.Frame(root, bg="light pink")
frame.pack(fill="both", expand=True)

# Create a label to display the background image
background_label = tk.Label(frame, image=photo)
background_label.pack(fill="both", expand=True)

# Create a label and button to test the GUI
label = tk.Label(frame, text="Grocery Billing System", font=("Arial", 24), bg="light pink")
label.pack(pady=20)

# Create buttons for different operations
button_frame = tk.Frame(frame, bg="light blue")
button_frame.pack(fill="x")

insert_button = tk.Button(button_frame, text="Insert Record", command=insert, width=20)
insert_button.pack(side=tk.LEFT, padx=10)

display_button = tk.Button(button_frame, text="Display Records", command=display, width=20)
display_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Record", command=delete, width=20)
delete_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(button_frame, text="Update Record", command=update, width=20)
update_button.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(button_frame, text="Search Record", command=search, width=20)
search_button.pack(side=tk.LEFT, padx=10)

bill_button = tk.Button(button_frame, text="Generate Bill", command=bill, width=20)
bill_button.pack(side=tk.LEFT, padx=10)

happy_hour_button = tk.Button(button_frame, text="Happy Hour!", command=happy_hour, width=20)
happy_hour_button.pack(side=tk.LEFT, padx=10)

# Start the main loop
root.mainloop()
