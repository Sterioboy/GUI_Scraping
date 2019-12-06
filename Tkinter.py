import requests
from bs4 import BeautifulSoup
import random
from tkinter import *

#Request
response = requests.get(
    f"http://quotes.toscrape.com/page/{random.randint(1,10)}/")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="quote")

res = []
for i in quotes:
    quote = i.find(class_="text").get_text()
    name = i.find(class_="author").get_text()
    link = i.find("a")["href"]
    res.append([quote, name, link])

#Game with GUI
root = Tk()
root.title("Quotes-20000")
#
random_quote = random.choice(res)
text = random_quote[0], random_quote[1]
myLabel = Label(root, text=text)
myLabel.grid(row=0, column=0)
#
users_answer = Entry(root, width=35, borderwidth=5)
users_answer.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
users_answer.insert(0, "Who said this")
#
def info():
    info = users_answer.get()
    if info != random_quote[1]:
        myLabel1 = Label(root, text="Wrong!")
        myLabel1.pack()
    else:
        myLabel1 = Label(root, text="Congrats!!!")
        myLabel1.pack()
        root.destroy()
def hint0():
    hint0 = f"THE FIRST LETTER TO WRITE IS $ {random_quote[1][0]} $"
    myLabel2 = Label(root, text=hint0)
    myLabel2.pack()

def hint1():
    resp_1 = requests.get(f"http://quotes.toscrape.com/{random_quote[2]}/")
    soup = BeautifulSoup(resp_1.text, "html.parser")
    birth_date = soup.find(class_="author-born-date").get_text()
    hint1 = f"The author was born in {birth_date}"
    myLabel2 = Label(root, text=hint1)
    myLabel2.pack()

def hint2():
    resp_1 = requests.get(
    f"http://quotes.toscrape.com/{random_quote[2]}/")
    soup = BeautifulSoup(resp_1.text, "html.parser")
    birth_loc = soup.find(class_="author-born-location").get_text()
    hint2 = f"The author was born in {birth_loc}"
    myLabel3 = Label(root, text=hint2)
    myLabel3.pack()

myButton = Button(root, padx=30, pady=20, text="Check", command=info, fg="purple")
myButton.grid(row=2, column=0)

hintButton = Button(root, padx=30, pady=20, text="Hint 1", command=hint0)
hintButton.grid(row=2, column=1)
hintButton1 = Button(root, padx=30, pady=20, text="Hint 2", command=hint1)
hintButton1.grid(row=2, column=2)
hintButton2 = Button(root, padx=30, pady=20, text="Hint 3", command=hint2)
hintButton2.grid(row=2, column=3)

root.mainloop()

