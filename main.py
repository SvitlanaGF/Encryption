import tkinter
from ciph import CiphInFile
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x450")
root.title("Caesar Cipher")
frame = customtkinter.CTkScrollableFrame(master=root, width=350, height=450)
frame.pack(pady=10, padx=40)
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

# Write file path
label3 = customtkinter.CTkLabel(master=frame, text='Files'
                                , font=('Roboto', 14))
label3.pack(pady=5, padx=10)
r_file = customtkinter.CTkEntry(master=frame, placeholder_text='File to read', width=250, height=30)
w_file = customtkinter.CTkEntry(master=frame, placeholder_text='File to write', width=250, height=30)
r_file.pack(pady=7, padx=5)
w_file.pack(pady=7, padx=5)
# Choose language
label4 = customtkinter.CTkLabel(master=frame, text='Choose language', font=('Roboto', 14))
label4.pack(pady=12, padx=10)

lang_var = tkinter.IntVar()


def choose_lang():
    print('Ukr') if lang_var.get() == 1 else print('Eng')


ukr_lang = customtkinter.CTkRadioButton(master=frame, text="Ukrainian", command=choose_lang, variable=lang_var, value=1)
eng_lang = customtkinter.CTkRadioButton(master=frame, text="English", command=choose_lang, variable=lang_var, value=2)

ukr_lang.pack(padx=20, pady=10)
eng_lang.pack(padx=20, pady=10)

# Button


def save_information():
    n = CiphInFile()
    if lang_var.get() == 1:
        n.ukr_cipher(r_file=r_file.get(), w_file=w_file.get(), step=int(step.get()), choice=choose_ciph.get())
    else:
        n.eng_cipher(r_file=r_file.get(), w_file=w_file.get(), step=int(step.get()), choice=choose_ciph.get())


button = customtkinter.CTkButton(master=frame, text="Ok", command=save_information)
button.pack(padx=20, pady=10)

root.mainloop()
