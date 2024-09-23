import smtplib
import random 
import datetime as dt
import pandas as pd 
from tkinter import *
import os 


my_email="oussama.chakeur@student.aiu.edu.my"
password="kaddakadda"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email, password=password)

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# Directory containing the letter files
letter_directory = 'C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Email SMTP/'

# Load all letters from the directory where letters are saved
letters = [os.path.join(letter_directory, file)
           for file in os.listdir(letter_directory)
           if file.startswith("letter_")]

# Debugging step: Check if letters list is empty
if not letters:
    print("No letter files found in the directory. Please make sure files start with 'letter_'.")
else:
    print(f"Letters found: {letters}")

# Check if letters exist before choosing a random letter
if letters:
    readletter = random.choice(letters)
else:
    readletter = None

# Proceed with sending the email if a letter was found
if readletter:
    birthdays_list = pd.read_csv("C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Email SMTP/birthdays.csv")
    for index, row in birthdays_list.iterrows():
        if day == row['day'] and month == row['month']:
            with open(readletter, 'r') as file:
                read_file = file.read()
            read_file = read_file.replace("[name]", row["name"])
            connection.sendmail(from_addr=my_email, to_addrs=row['gmail'], msg=f'subject:it works \n\n{read_file}')

connection.close()


def add_member():
    window1 = Tk()
    window1.title("Add Member")
    window1.minsize(600, 600)
    window1.config(padx=100, pady=100, bg="black")

    name_label = Label(window1, text='Name: ', font=('arial', 10, 'bold'), bg="black", fg="white")
    name_label.grid(column=0, row=0)

    email_username_label = Label(window1, text='Email: ', font=('arial', 10, 'bold'), bg="black", fg="white")
    email_username_label.grid(column=0, row=3)

    yearOfBirth_label = Label(window1, text='Year of birth (yyyy): ', font=('arial', 10, 'bold'), bg="black", fg="white")
    yearOfBirth_label.grid(column=0, row=6)

    monthOfBirth_label = Label(window1, text='Month of birth (mm): ', font=('arial', 10, 'bold'), bg="black", fg="white")
    monthOfBirth_label.grid(column=0, row=9)

    dayOfBirth_label = Label(window1, text='Day of birth (dd): ', font=('arial', 10, 'bold'), bg="black", fg="white")
    dayOfBirth_label.grid(column=0, row=12)

    # Entry fields
    name_entry = Entry(window1, width=40)
    name_entry.grid(column=1, row=0)

    email_entry = Entry(window1, width=40)
    email_entry.grid(column=1, row=3)

    yearOfBirth_entry = Entry(window1, width=20)
    yearOfBirth_entry.grid(column=1, row=6)

    monthOfBirth_entry = Entry(window1, width=20)
    monthOfBirth_entry.grid(column=1, row=9)

    dayOfBirth_entry = Entry(window1, width=20)
    dayOfBirth_entry.grid(column=1, row=12)

    space = Label(window1, text=" ", bg='black')
    space.grid(column=0, row=1)
    space.grid(column=0, row=2)
    space1 = Label(window1, text=" ", bg="black")
    space1.grid(column=0, row=4)
    space1.grid(column=0, row=5)
    space2 = Label(window1, text="", bg="black")
    space2.grid(column=0, row=7)
    space2.grid(column=0, row=8)
    space3 = Label(window1, text="", bg="black")
    space3.grid(column=0, row=10)
    space3.grid(column=0, row=11)
    space4 = Label(window1, text="", bg="black")
    space4.grid(column=0, row=13)
    space4.grid(column=0, row=14)

    def addToList():
        name = name_entry.get().lower()
        email = email_entry.get().lower()
        year = yearOfBirth_entry.get()
        month = monthOfBirth_entry.get()
        day = dayOfBirth_entry.get()
        try:
            with open("C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Email SMTP/birthdays.csv", "a") as add_file:
                add_file.write(f"{name},{email},{year},{month},{day}\n")
        except:
            error = Label(text="File selected is not found", font=("arial", 10, "bold"), fg="red")
            error.grid(column=1, row=16)

        window1.destroy()

    add = Button(window1, text="Add", font=("arial", 15, "bold"), bg="yellow", command=addToList)
    add.grid(column=1, row=15)

    window1.mainloop()


def add_letter():
    window2 = Tk()
    window2.title("Add Letter")
    window2.minsize(600, 600)
    window2.config(padx=100, pady=100, bg="black")

    text_label = Label(window2, text="Write your letter: ", font=('arial', 10, "bold"), bg="white")
    text_label.grid(column=0, row=0)

    text_entry = Text(window2, width=40, height=20)
    text_entry.grid(column=1, row=0)

    def save_letter():
        new_letter = text_entry.get("1.0", END).strip()  # Get the entire content from the Text widget
        if new_letter:
            letter_filename = f"letter_{int(dt.datetime.now().timestamp())}.txt"  # Create a unique file name
            letter_path = os.path.join(letter_directory, letter_filename)
            
            # Save the new letter
            with open(letter_path, "w") as letter_file:
                letter_file.write(new_letter)
            
            # Dynamically update the list of letters
            letters.append(letter_path)

            success_label = Label(window2, text="Letter added successfully!", font=('arial', 10, 'bold'), bg="black", fg="green")
            success_label.grid(column=1, row=2)

    add = Button(window2, text="Add", font=("arial", 15, "bold"), bg="yellow", command=save_letter)
    add.grid(column=1, row=15)

    window2.mainloop()


window = Tk()
window.title("Email Sender")
window.minsize(600, 600)
window.config(padx=100, pady=100, bg="black")

canvas = Canvas(width=400, height=300, highlightthickness=0)

# Store the image as a global variable to prevent garbage collection
ballons = PhotoImage(file="C:/Users/lenovo/Desktop/python bootcamp/PROJECTS/intermediat/Email SMTP/Untitled design.png")

# Create the image on the canvas
canvas.create_image(200, 200, image=ballons)
canvas.config(bg="black")
canvas.grid(column=0, row=0)

space = Label(text="", highlightthickness=0, bg='black')
space.grid(column=0, row=3)
space = Label(text="", highlightthickness=0, bg='black')
space.grid(column=0, row=1)

# Buttons
add_member_button = Button(text="Add a Member", width=45, font=("arial", 15, "bold"), bg="yellow", command=add_member)
add_member_button.grid(column=0, row=2)

new_letter_button = Button(text="Form a New Letter", width=45, font=("arial", 15, "bold"), bg="yellow", command=add_letter)
new_letter_button.grid(column=0, row=4)

window.mainloop()
