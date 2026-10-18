
import tkinter as tk

def calculate(operation):
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = a / b

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Enter valid numbers")


root = tk.Tk()
root.title("My Python Calculator")
root.geometry("350x300")

tk.Label(root, text="First Number").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Add (+)",
          command=lambda: calculate("+")).pack(pady=3)

tk.Button(root, text="Subtract (-)",
          command=lambda: calculate("-")).pack(pady=3)

tk.Button(root, text="Multiply (*)",
          command=lambda: calculate("*")).pack(pady=3)

tk.Button(root, text="Divide (/)",
          command=lambda: calculate("/")).pack(pady=3)

result_label = tk.Label(root, text="Result:",
                        font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
