from tkinter import *
import random
import time

#To create a basic box layout
root = Tk()
root.geometry("1600x700+0+0")
#To add title on the left top most corner of the basic box layout
root.title("RESTAURANT MANAGEMENT SYSTEM")
tops = Frame(root, width=1600, height=50, bg="black", relief=SUNKEN)
tops.pack(side=TOP)


f1 = Frame(root, width=900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
f2 = Frame(root, width=400,height=700,bg="powder blue",relief=SUNKEN)
f2.pack(side=RIGHT)

#To add TIME
localtime = time.asctime(time.localtime(time.time()))
#Add information to TOP
labelinfo = Label(tops, font = ('arial',30,'bold'),text = "RESTAURANT MANAGEMENT SYSTEM",fg="PURPLE",bd=20,anchor='w')
labelinfo.grid(row=0,column=0)
labelinfo = Label(tops, font = ('arial',20,'bold'),text = "localtime",fg="steel blue",bd=20,anchor='w')
labelinfo.grid(row=1,column=0)

def onclick(numbers):
    global operator
    operator += str(numbers)
    text_input.set(operator)


def onclear():
    global operator
    operator = ""
    text_input.set(operator)


def onequals():
    global operator
    val = str(eval(operator))
    text_input.set(val)
    operator = ""


operator = ""
text_input = StringVar()

txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='powder blue',
                   justify='right').grid(columnspan=4)

b7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="white",
            command=lambda: onclick(7)).grid(row=2, column=2)
b8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="white",
            command=lambda: onclick(8)).grid(row=2, column=1)
b9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="white",
            command=lambda: onclick(9)).grid(row=2, column=0)
badd = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="pink",
              command=lambda: onclick("+")).grid(row=2, column=3)

b6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="white",
            command=lambda: onclick(6)).grid(row=3, column=0)
b5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="white",
            command=lambda: onclick(5)).grid(row=3, column=1)
b4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="white",
            command=lambda: onclick(4)).grid(row=3, column=2)
bsub = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="pink",
              command=lambda: onclick("-")).grid(row=3, column=3)

b3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="white",
            command=lambda: onclick(3)).grid(row=4, column=0)
b2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="white",
            command=lambda: onclick(2)).grid(row=4, column=1)
b1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="white",
            command=lambda: onclick(1)).grid(row=4, column=2)
bmul = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="pink",
              command=lambda: onclick("*")).grid(row=4, column=3)

b0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="white",
            command=lambda: onclick(0)).grid(row=5, column=0)
bc = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg="white",
            command=onclear).grid(row=5, column=1)
beq = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="white",
             command=onequals).grid(row=5, column=2)
bdiv = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", bg="pink",
              command=lambda: onclick("/")).grid(row=5, column=3)

#ITEMS LIST

rand = StringVar()
Fries = StringVar()
Pizza = StringVar()
Burger = StringVar()
Drinks = StringVar()
SubTotal = StringVar()
Total = StringVar()
Tax = StringVar()

lblreference = Label(f1, font=('comic sans', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="Silver",
                     justify='right')
txtreference.grid(row=0, column=1)

lblfries = Label(f1, font=('comic sans', 16, 'bold'), text="Fries", bd=16, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="Silver",
                 justify='right')
txtfries.grid(row=1, column=1)

lblpizza = Label(f1, font=('comic sans', 16, 'bold'), text="Pizza", bd=16, anchor='w')
lblpizza.grid(row=2, column=0)
txtpizza = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=Pizza, bd=10, insertwidth=4, bg="Silver",
                 justify='right')
txtpizza.grid(row=2, column=1)

lblburger = Label(f1, font=('comic sans', 16, 'bold'), text="Burger", bd=16, anchor='w')
lblburger.grid(row=3, column=0)
txtburger = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="Silver",
                  justify='right')
txtburger.grid(row=3, column=1)


lbldrinks = Label(f1, font=('comic sans', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lbldrinks.grid(row=0, column=2)
txtdrinks = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="Silver",
                  justify='right')
txtdrinks.grid(row=0, column=3)

lbltax = Label(f1, font=('comic sans', 16, 'bold'), text="GST", bd=16, anchor='w')
lbltax.grid(row=2, column=2)
txttax = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="Silver",
               justify='right')
txttax.grid(row=2, column=3)

lblsubtotal = Label(f1, font=('comic sans', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblsubtotal.grid(row=1, column=2)
txtsubtotal = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="Silver",
                    justify='right')
txtsubtotal.grid(row=1, column=3)

lbltotal = Label(f1, font=('comic sans', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lbltotal.grid(row=3, column=2)
txttotal = Entry(f1, font=('comic sans', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="Silver",
                 justify='right')
txttotal.grid(row=3, column=3)

#buttons

def stop():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Pizza.set("")
    Burger.set("")
    SubTotal.set("")
    Total.set("")
    Drinks.set("")
    Tax.set("")
    IceCream.set("")



def Cal_Total():
    x = random.randint(1, 1000)
    randomRef = str(x)
    rand.set(randomRef)

    COF = float(Fries.get())
    COP = float(Pizza.get())
    COB = float(Burger.get())
    COD = float(Drinks.get())
    COIC = float(IceCream.get())

    COF = COF * 50
    COP = COP * 120
    COB = COB * 30
    COD = COD * 200
    COIC = COIC * 60


    total_Tax = ((COF + COP + COB + COD + COIC ) * 0.05)
    total_cost = (COF + COP + COB + COD + COIC )
    overall = (total_Tax + total_cost)
    Tax.set(total_Tax)
    SubTotal.set(total_cost)
    Total.set(overall)


btnReset = Button(f1, padx=16, pady=8, bd=16, fg="Black", font=('arial', 16, 'bold'), width=10, text="RESET", bg="Pink",
                  command=Reset).grid(row=7, column=1)
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="Black", font=('arial', 16, 'bold'), width=10, text="TOTAL", bg="Pink",
                  command=Cal_Total).grid(row=7, column=2)
btnStop = Button(f1, padx=16, pady=8, bd=16, fg="Black", font=('arial', 16, 'bold'), width=10, text="CLOSE", bg="Pink",
                 command=stop).grid(row=7, column=3)

root.mainloop()

root.mainloop()