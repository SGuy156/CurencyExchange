from tkinter import *
from tkinter.ttk import *#use combobox
from ttkthemes import ThemedTk
import requests, json

screen = ThemedTk(theme="winxpblue") #creates window
screen.configure(themebg="winxpblue")
screen.title("Currency Exchange") # Title
screen.geometry('487x100') #window dimensions
screen.resizable(height=False, width=False)

def convert():
    global baseurl
    global mainurl


    fromCurrency= tmsfrom.get()
    toCurrency= tmsto.get()

    apikey = "K3MQO5ISZGAYC6NI"

    baseurl = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    mainurl = baseurl + "&from_currency=" + fromCurrency + "&to_currency=" + toCurrency + "&apikey=" + apikey
    print(mainurl)

    req_obj = requests.get(mainurl)

    result=req_obj.json()
    exchange_rate = float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    print(exchange_rate)

    entryinput = float(entryamnt.get())

    convertedinput = round(entryinput * exchange_rate, 2)

    lblresult.configure(text=str(convertedinput))






lbl = Label(screen,text = "Currency Exchange Calculator")
lblamount = Label(screen,text = "Amount")
lblfrom = Label(screen,text = "From")
lblto = Label(screen,text = "To")
entryamnt = Entry(screen)
btn = Button(screen,text="Convert",command=convert)
lblresult = Label(screen,text="")


tmsfrom = Combobox(screen,state='readonly')
tmsfrom['values']=('EUR','USD','JPY','GBP','RUB')
tmsfrom.current(0)

tmsto = Combobox(screen,state='readonly')
tmsto['values']=('EUR','USD','JPY','GBP','RUB')
tmsto.current(0)


lbl.grid(row=0,columnspan=4)
lblamount.grid(row=1, column=0)
lblfrom.grid(row=1, column=1)
lblto.grid(row=1, column=2)
entryamnt.grid(row=2, column=0)
tmsfrom.grid(row=2, column=1)
tmsto.grid(row=2, column=2)
btn.grid(row=2, column=3)
lblresult.grid(row=3,columnspan=4)



screen.mainloop() #klenei programma