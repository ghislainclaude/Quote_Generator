#Quote Generator
#Click Button 
#Pulls quates from json folder using API 
#display API
#firstly lets install request, this will pull quoates
import tkinter as tk 
import requests
from threading import Thread #will make our code smooth when we run it 


#api link to Json file 
api = " http://api.quotable.io/random"
quotes = []
quate_number = 0
#Design ui
window = tk.Tk()
window.geometry("980x260")
window.title("Quote generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)
window.configure(bg="light grey")
#load the quotes Python Quote_Gener.py
def preload_quotes():
    global quotes
#here we take the content 
    print("***Loading more Quote***")
    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "By "+  author
        print(content)
        quotes.append(quote)

    print("***Finished Loading more quotes!***")
preload_quotes()

def get_random_quote():
    global quoate_lable
    global quotes
    global quate_number

    quoate_lable.configure(text=quotes[quate_number])
    quate_number = quate_number + 1
    print(quate_number)

    if quotes[quate_number] == quate_number[-3]:
        thread = Thread(target=preload_quotes)
        thread.start()
#UI 
quoate_lable = tk.Label(window, text="Click on the button to generate a random numbern!", height=6, pady=10, wraplength=800, 
                        font=("Helvetica", 14))
quoate_lable.grid(row=0, column=0, stick="WE", padx=20, pady=10)
button = tk.Button(text="Generate", command=get_random_quote, bg='#8052cc', fg="#ffffff", activebackground="grey",
                    font=("Helvectia", 14))
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)
#Tell the code to run if we in main file 
if __name__ == "__main__":
    window.mainloop()



