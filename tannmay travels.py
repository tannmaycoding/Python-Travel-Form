from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()


def rate():
    value = tmsg.askquestion("Rate Us", "You used our GUI, was you experience good")

    if value == "yes":
        tmsg.showinfo("Thank You for rating", "Thank You for rating, Please Rate Us on TkinterStore please")

    else:
        tmsg.showinfo("Thank You for rating",
                      "Thank You For Rating, We will call you back soon for what went wrong in your experience.")

    return value


def getValues():
    data = {
        "name": nameVal.get(),
        "contact": contactVal.get(),
        "emergencyContact": emergencyVal.get(),
        "whatsapp": whatsappVal.get(),
        "email": emailVal.get(),
        "paymentMode": paymentVal.get(),
        "foodService": "Yes" if foodValue else "No",
        "rating": "Yes" if rate() == "yes" else "No",
        "budget": budgetSlider.get()
    }
    for i in destinationListBox.curselection():
        data["destination"] = destinationListBox.get(i)

    for item in data.items():
        print(item)

    with open('text2.txt', 'a') as text:
        text.write(f'''{str(data.items()).replace("dict_items", "").replace("([", "[").replace(")]", "]")}\n''')


root.geometry("710x600")
root.title("TK Travels")

Label(text='Welcome To TK Travels', font='comicsansms 20 bold', pady=22).grid(row=0, column=0)

name = Label(text="Name: ", font="comicsansms 15 bold")
contact = Label(text="Contact Number: ", font="comicsansms 15 bold")
emergency = Label(text="Emergency Contact Number: ", font="comicsansms 15 bold")
whatsapp = Label(text="Whatsapp Number: ", font="comicsansms 15 bold")
email = Label(text="E-Mail ID: ", font="comicsansms 15 bold")
payment = Label(text="Payment Mode: ", font="comicsansms 15 bold")

name.grid(row=1, column=0)
contact.grid(row=2, column=0)
emergency.grid(row=3, column=0)
whatsapp.grid(row=4, column=0)
email.grid(row=5, column=0)
payment.grid(row=6, column=0)

nameVal = StringVar()
contactVal = StringVar()
emergencyVal = StringVar()
whatsappVal = StringVar()
emailVal = StringVar()
paymentVal = StringVar()
foodValue = IntVar()

nameEntry = Entry(textvariable=nameVal)
contactEntry = Entry(textvariable=contactVal)
emergencyEntry = Entry(textvariable=emergencyVal)
whatsappEntry = Entry(textvariable=whatsappVal)
emailEntry = Entry(textvariable=emailVal)
paymentEntry = Entry(textvariable=paymentVal)

nameEntry.grid(row=1, column=1)
contactEntry.grid(row=2, column=1)
emergencyEntry.grid(row=3, column=1)
whatsappEntry.grid(row=4, column=1)
emailEntry.grid(row=5, column=1)
paymentEntry.grid(row=6, column=1)

foodservice = Checkbutton(text='Want To prebook your meals?', font='comicsansms 15 bold', variable=foodValue)
foodservice.grid(row=7, column=0)

scrollBar = Scrollbar()
scrollBar.grid(row=8, column=2)

destinationLabel = Label(text="What will be your destination:", font='comicsansms 15 bold')
destinationLabel.grid(row=8, column=0)

destinationListBox = Listbox(width=40, height=10, yscrollcommand=scrollBar.set)
destinationList = ["Delhi", "Chandigarh", "Gujarat", "Rajasthan", "Uttar Pradesh", "Himachal Pradesh",
                   "Jammu And Kashmir", "Kerala", "Tamil Nadu", "Ladakh", "Punjab", "West Bengal", "Arunachal Pradesh",
                   "Maharashtra", "Karnataka"]

for ind, val in enumerate(destinationList):
    destinationListBox.insert(ind + 1, val)

destinationListBox.grid(row=8, column=1)
scrollBar.config(command=destinationListBox.yview)

budgetLabel = Label(text="What is your budget(from 10000 to 10000000)", font='comicsansms 15 bold')
budgetLabel.grid(row=9, column=0)

budgetSlider = Scale(from_=10000, to=10000000, orient=HORIZONTAL)
budgetSlider.grid(row=9, column=1)

Button(text="Submit", font="comicsansms 12 bold", padx=5, pady=5, command=getValues).grid(row=11, column=0)

root.mainloop()
