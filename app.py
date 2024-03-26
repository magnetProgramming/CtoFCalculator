import customtkinter
import tkinter
import math

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x200")
app.resizable(width=False, height=False)
app.title("Celsius to Fahrenheit Calculator")

inputBox = customtkinter.CTkEntry(master=app, placeholder_text="Enter Celsius")
inputBox.pack(padx=10, pady=10)


def calculate():
    try:
        cel_input = inputBox.get()
        calculated_celInput =(float(cel_input)) * 1.8 + 32
        print(calculated_celInput)
        calculatedAnswerLabel.configure(text=calculated_celInput)

    except:
        return


calculatedAnswerLabel = customtkinter.CTkLabel(master=app, text="Enter degrees in celsius above.")
calculatedAnswerLabel.pack()


calculate_button = customtkinter.CTkButton(master=app, text="Calculate", command=calculate)
calculate_button.pack()



app.mainloop()
