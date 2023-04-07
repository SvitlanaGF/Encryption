from gamma import *
from vernam import Vernam
from vigenere import VigenereCiph
from caesar import *


class CeasarCiphInFile:
    @staticmethod
    def ukr_cipher(txt: str, encryption: str, w_file: str, choice=1, step=3, key='', motto=''):
        '''
        :param txt: the text that will be read
        :param w_file: the file in which the information will be written
        :param choice: 1 - encrypt the text; else decrypt the text
        :param step: displacement step
        :return: file with recorded information
        '''
        if encryption == 'Ceasar':
            WorkWithFiles(w_file).write_txt(UkrCaesarCipher(txt, step).cipher_txt()), print(UkrCaesarCipher(txt, step).cipher_txt()) \
                if choice == 1 else WorkWithFiles(w_file).write_txt(UkrCaesarCipher(txt, step).decipher_txt()),\
                print(UkrCaesarCipher(txt, step).decipher_txt())
        elif encryption == 'Gamma':
            if choice == 1:
                n = GammaCiph(txt, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ').encrypt()
                WorkWithFiles(w_file).write_txt(n)
                print(n)
            else:
                n = GammaCiph(txt, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ').decrypt(key)
                WorkWithFiles(w_file).write_txt(n)
                print(n)
        elif encryption == 'Vigenere':
            if choice == 1:
                WorkWithFiles(w_file).write_txt(VigenereCiph(txt, motto, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ').encrypt())
            else:
                WorkWithFiles(w_file).write_txt(VigenereCiph(txt, motto, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ').decrypt())
        elif encryption == "Vernam":
            if choice == 1:
                WorkWithFiles(w_file).write_txt(Vernam(txt, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ', motto).encrypt())
                print(Vernam(txt, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ', motto).encrypt())
            else:
                WorkWithFiles(w_file).write_txt(Vernam(txt, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ', motto).decrypt())
                print(Vernam(txt, 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ', motto).decrypt())
    @staticmethod
    def eng_cipher(txt: str, encryption: str, w_file: str, choice =1, step=3, key='', motto=''):
        '''
        :param txt: the text that will be read
        :param w_file: the file in which the information will be written
        :param choice: 1 - encrypt the text; else decrypt the text
        :param step: displacement step
        :return: file with recorded information
        '''
        if encryption == 'Ceasar':
            WorkWithFiles(w_file).write_txt(EngCaesarCipher(txt, step).cipher_txt()), print(EngCaesarCipher(txt, step).cipher_txt()) if \
                choice == 1 else WorkWithFiles(w_file).write_txt(EngCaesarCipher(txt, step).decipher_txt()), \
                print(EngCaesarCipher(txt, step).decipher_txt())
        elif encryption == 'Gamma':
            if choice == 1:
                n = GammaCiph(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').encrypt()
                WorkWithFiles(w_file).write_txt(n)
                print(n)
            else:
                n = GammaCiph(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').decrypt(key)
                WorkWithFiles(w_file).write_txt(n)
                print(n)
        elif encryption == 'Vigenere':
            if choice == 1:
                WorkWithFiles(w_file).write_txt(VigenereCiph(txt, motto, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').encrypt())
                print(VigenereCiph(txt, motto, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').encrypt())
            else:
                WorkWithFiles(w_file).write_txt(VigenereCiph(txt, motto, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').decrypt())
                print(VigenereCiph(txt, motto, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ').encrypt())
        elif encryption == "Vernam":
            if choice == 1:
                WorkWithFiles(w_file).write_txt(Vernam(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', motto).encrypt())
                print(Vernam(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', motto).encrypt())
            else:
                WorkWithFiles(w_file).write_txt(Vernam(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', motto).decrypt())
                print(Vernam(txt, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', motto).decrypt())

    def encr_it(self, txt: str, encryption: str, w_file: str, choice=1,  step=3, key='', motto=''):
        if txt.endswith('.docx') or txt.endswith('.txt'):
            text = WorkWithFiles(txt).read_text()
        else:
            text = txt
        n = 0
        while True:
            if text[n].isalpha():
                if 65 <= ord(text[n].upper()) <= 90:
                    self.eng_cipher(txt=text, encryption=encryption, w_file=w_file, choice=choice, step=step, key=key, motto=motto)
                else:
                    self.ukr_cipher(txt=text, encryption=encryption, w_file=w_file, choice=choice, step=step, key=key, motto=motto)
                break
            n += 1

