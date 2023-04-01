import tkinter
from ciph import CeasarCiphInFile
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x550")
root.title("Ciphers")
frame = customtkinter.CTkScrollableFrame(master=root, width=650, height=800)
frame.pack(pady=10, padx=40)
# Choose cipher
label1 = customtkinter.CTkLabel(master=frame, text='Cipher:'
                                , font=('Roboto', 14))
label1.pack(pady=12, padx=10)
optionmenu_var = customtkinter.StringVar(value="Ceasar")

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = customtkinter.CTkOptionMenu(master=frame,
                                       values=["Ceasar", "Gamma", "Vernam", "Vigenere"],
                                       command=optionmenu_callback,
                                       variable=optionmenu_var)
combobox.pack(padx=20, pady=10)

# Choose you want to encrypt or decrypt text
label1 = customtkinter.CTkLabel(master=frame, text='Do you want to encrypt or decrypt your text?'
                                , font=('Roboto', 14))
label1.pack(pady=12, padx=10)
choose_ciph = tkinter.IntVar()


def ciph_or_deciph():
    print('Encrypt the text') if choose_ciph.get() == 1 else print('Decrypt the text')


encr = customtkinter.CTkRadioButton(master=frame, text="Encrypt"
                                    , command=ciph_or_deciph, variable=choose_ciph, value=1)
decr = customtkinter.CTkRadioButton(master=frame, text="Decrypt"
                                    , command=ciph_or_deciph, variable=choose_ciph, value=2)
encr.pack(padx=20, pady=10)
decr.pack(padx=20, pady=10)


# Choose step
label2 = customtkinter.CTkLabel(master=frame, text='Step:', font=('Roboto', 14))
label2.pack(pady=5, padx=10)

step_var = customtkinter.StringVar(value="3")


def step_callback(choice: str):
    if choice.isdigit:
        print("combobox dropdown clicked:", int(step_var.get()))
    else:
        raise TypeError


step = customtkinter.CTkComboBox(master=frame, values=["1", "2", "3", "4", "5"], command=step_callback,
                                     variable=step_var)
step.pack(padx=20, pady=5)
# Write motto
label2 = customtkinter.CTkLabel(master=frame, text='Write a message for Vigenere or Vernam:'
                                , font=('Roboto', 14))
label2.pack(pady=5, padx=10)
w_motto = customtkinter.CTkEntry(master=frame, placeholder_text='Message', width=250, height=30)
w_motto.pack(pady=7, padx=5)
# Write key
label2 = customtkinter.CTkLabel(master=frame, text='Write key for gamma:'
                                , font=('Roboto', 14))
label2.pack(pady=5, padx=10)
w_key = customtkinter.CTkEntry(master=frame, placeholder_text='Key', width=250, height=30)
w_key.pack(pady=7, padx=5)
# Write file path
label3 = customtkinter.CTkLabel(master=frame, text='Files'
                                , font=('Roboto', 14))
label3.pack(pady=5, padx=10)
r_file = customtkinter.CTkEntry(master=frame, placeholder_text='Text', width=250, height=100)
w_file = customtkinter.CTkEntry(master=frame, placeholder_text='File to write', width=250, height=30)
r_file.pack(pady=7, padx=5)
w_file.pack(pady=7, padx=5)

# Button

def save_information():
    n = CeasarCiphInFile()
    n.encr_it(txt=r_file.get(), w_file=w_file.get(), step=int(step.get()), choice=choose_ciph.get(),
              encryption=combobox.get(), key=w_key.get(), motto=w_motto.get())


button = customtkinter.CTkButton(master=frame, text="Ok", command=save_information)
button.pack(padx=20, pady=10)

root.mainloop()

