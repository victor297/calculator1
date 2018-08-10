from tkinter import*

root =Tk()
root.geometry("300x340+50+50")
root.title("SammyCalculator")

Tops = Frame(root, width = 300, height=20, bd=4, relief="raise")
Tops.pack(side=TOP)

Below = Frame(root, width = 300, height=300, bd=4, relief="raise")
Below.pack(side=BOTTOM)

#==================================================================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set( operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")


def btnEqual():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

operator = ""
text_Input = StringVar()


#==================================================================================

txtDisplay = Entry(Tops, font=('arial' ,18, 'bold'),textvariable=text_Input, width = 21, bd=4, justify = 'right')
txtDisplay.grid(row =0, column =0)

btn7 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "7", command =lambda:btnClick(7)).grid(row=0, column=0)

btn8 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "8", command =lambda:btnClick(8)).grid(row=0, column=1)

btn9 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "9", command =lambda:btnClick(9)).grid(row=0, column=2)

btnAdd = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "+", command =lambda:btnClick("+")).grid(row=0, column=3)


btn4 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "4", command =lambda:btnClick(4)).grid(row=1, column=0)

btn5 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "5", command =lambda:btnClick(5)).grid(row=1, column=1)

btn6 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "6", command =lambda:btnClick(6)).grid(row=1, column=2)

btnSub = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "-", command =lambda:btnClick("-")).grid(row=1, column=3)


btn1 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "1", command =lambda:btnClick(1)).grid(row=2, column=0)

btn2 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "2", command =lambda:btnClick(2)).grid(row=2, column=1)

btn3 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "3", command =lambda:btnClick(3)).grid(row=2, column=2)

btnMult = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "*", command =lambda:btnClick("*")).grid(row=2, column=3)


btn0 = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "0", command =lambda:btnClick(0)).grid(row=3, column=0)

btnClear = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "C", command =btnClear).grid(row=3, column=1)

btnEquals = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "=", command =btnEqual).grid(row=3, column=2)

btnDiv = Button(Below, padx=16, pady=1, bd=4, fg="black",font=('arial' , 16, 'bold'),width=2 , height =2,
text = "/", command =lambda:btnClick("/")).grid(row=3, column=3)


root.mainloop()
