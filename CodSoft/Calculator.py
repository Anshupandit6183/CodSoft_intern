import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2    
    elif operation == "/":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    elif operation == "%":
        result = num1 % num2                       
    else:
        result = "Invalid operation"

    label_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Calculator")
root.configure(bg="#8a5454")

label1 = tk.Label(root, text="Enter the first number:", width="20", bg="green")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Enter the second number:", width="20", bg="green")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label_operation = tk.Label(root, text="Choose an operation:", bg="green")
label_operation.grid(row=2, column=0)

var = tk.StringVar()
var.set("+")

radio_add = tk.Radiobutton(root, text="+", variable=var, value="+", bg="yellow")
radio_add.grid(row=2, column=1)

radio_subtract = tk.Radiobutton(root, text="-", variable=var, value="-", bg="yellow")
radio_subtract.grid(row=3, column=1)

radio_multiply = tk.Radiobutton(root, text="*", variable=var, value="*", bg="yellow")
radio_multiply.grid(row=4, column=1)

radio_divide = tk.Radiobutton(root, text="/", variable=var, value="/", bg="yellow")
radio_divide.grid(row=5, column=1)

radio_divide = tk.Radiobutton(root, text="%", variable=var, value="%", bg="yellow")
radio_divide.grid(row=6, column=1)

button_calculate = tk.Button(root, text="Calculate", command=calculate, bg="brown")
button_calculate.grid(row=7, column=0, columnspan=2)

label_result = tk.Label(root, text="Result:", bg="brown")
label_result.grid(row=8, column=0, columnspan=2)

root.mainloop()