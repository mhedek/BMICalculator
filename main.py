from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)


def giris():

    try:

        kilo= int(entry1.get())
        boy = int(entry2.get())

        hesapla = kilo / (boy / 100) ** 2

        if hesapla < 18.4:
            sonuc_label.config(text="Your BMI is {}. You are Underweight. ".format(round(hesapla, 2)))

        elif 18.4 < hesapla < 24.9:
            sonuc_label.config(text="Your BMI is {}. You are Normal. ".format(round(hesapla, 2)))

        elif 25 < hesapla < 29.9:
            sonuc_label.config(text="Your BMI is {}. You are Overweight. ".format(round(hesapla, 2)))

        else:
            sonuc_label.config(text="Your BMI is {}. You are Obese. ".format(round(hesapla, 2)))


    except ValueError:
        sonuc_label.config(text="Enter a valid number")



#label or #entry

label1 = Label(window, text="Enter your weight(kg)")
label1.pack()

entry1 = Entry(window, width=10)
entry1.pack()

label2 = Label(window, text="Enter your height(cm)")
label2.pack()

entry2 = Entry(window, width=10)
entry2.pack()


bt = Button(window, text="Colculator", command=giris)
bt.pack()

sonuc_label = Label(window, text="")
sonuc_label.pack()

window.mainloop()