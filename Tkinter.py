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
myLabel.pack()
#
users_answer = Entry(root)
users_answer.pack()
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
    hint2 = f"I've almost completed the name for you :) $ {random_quote[1][0]+random_quote[1][1]+random_quote[1][2]+random_quote[1][3]} $"
    myLabel3 = Label(root, text=hint2)
    myLabel3.pack()

myButton = Button(root, text="Check", command=info, fg="purple")
myButton.pack()

hintButton = Button(root, text="Hint 1", command=hint0)
hintButton.pack()
hintButton1 = Button(root, text="Hint 2", command=hint1)
hintButton1.pack()
hintButton2 = Button(root, text="Hint 3", command=hint2)
hintButton2.pack()

root.mainloop()

