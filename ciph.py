from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class FrequencyImage:
    def img(self, text: str):
        x_letters = list(set([i for i in text]))
        y_count = [text.count(i) for i in x_letters]
        plt.title('Frequency')
        plt.bar(x_letters, y_count)
        plt.show()

class WorkWithFiles:
    def __init__(self, file_path: str):
        if file_path.endswith('.docx') or file_path.endswith('.txt') or file_path.endswith('.pdf'):
            self.file_path = file_path
        else:
            raise NameError

    def write_txt(self, information: str):
        '''
        :param information: text you want to write into file
        '''
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(information)
        print(f'The information has been written into the file "{self.file_path}"')

    def read_text(self):
        '''
        :return: string with an information from the file
        '''
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()


class CaesarCipher(ABC):
    def __init__(self, information: str, step: int):
        self.information = information
        self.step = step

    @abstractmethod
    def cipher_txt(self):
        pass

    @abstractmethod
    def decipher_txt(self):
        pass


class EngCipher(CaesarCipher):
    def __init__(self, information: str, step: int):
        super().__init__(information, step)

    def cipher_txt(self):
        '''
        :return: encrypted text
        '''
        ciphered_txt = ''
        for i in self.information:
            if not i.isalpha():
                ciphered_txt += i
            elif ord(i.upper())+self.step <= 90:
                ciphered_txt += chr(ord(i)+self.step)
            else:
                ciphered_txt += chr(ord(i)+self.step-26)
        n = FrequencyImage()
        n.img(ciphered_txt)
        return ciphered_txt

    def decipher_txt(self):
        '''

        :return: decrypted text
        '''
        deciphered_txt = ''
        for i in self.information:
            if not i.isalpha():
                deciphered_txt += i
            elif ord(i.upper()) >= 65+self.step:
                deciphered_txt += chr(ord(i)-self.step)
            else:
                deciphered_txt += chr(ord(i)-self.step+26)
        n = FrequencyImage()
        n.img(deciphered_txt)
        return deciphered_txt


class UkrCipher(CaesarCipher):
    ukrLangUp = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    ukrLang = ukrLangUp + 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

    def __init__(self, information: str, step: int):
        super().__init__(information, step)

    def cipher_txt(self):
        '''
        :return: encrypted text
        '''
        ciphered_txt = ''
        for i in self.information:
            if not i.isalpha():
                ciphered_txt += i
            elif self.ukrLangUp.index(i.upper())+self.step < len(self.ukrLangUp):
                ciphered_txt += self.ukrLang[self.ukrLang.index(i)+self.step]
            else:
                ciphered_txt += self.ukrLang[self.ukrLang.index(i)+self.step-33]
        n = FrequencyImage()
        n.img(ciphered_txt)
        return ciphered_txt

    def decipher_txt(self):
        '''
        :return: decrypted text
        '''
        deciphered_txt = ''
        for i in self.information:
            if not i.isalpha():
                deciphered_txt += i
            elif self.ukrLangUp.index(i.upper()) >= self.step:
                deciphered_txt += self.ukrLang[self.ukrLang.index(i)-self.step]
            else:
                deciphered_txt += self.ukrLang[self.ukrLang.index(i)-self.step+33]
        n = FrequencyImage()
        n.img(deciphered_txt)
        return deciphered_txt


class CiphInFile:
    def ukr_cipher(self, r_file: str, w_file: str, choice=1, step=3):
        '''
        :param r_file: the file that will be read
        :param w_file: the file in which the information will be written
        :param choice: 1 - encrypt the text; else decrypt the text
        :param step: displacement step
        :return: file with recorded information
        '''
        txt_from_file = WorkWithFiles(r_file).read_text()
        WorkWithFiles(w_file).write_txt(UkrCipher(txt_from_file, step).cipher_txt()) if choice == 1 \
            else WorkWithFiles(w_file).write_txt(UkrCipher(txt_from_file, step).decipher_txt())

    def eng_cipher(self, r_file: str, w_file: str, choice=1, step=3):
        '''
        :param r_file: the file that will be read
        :param w_file: the file in which the information will be written
        :param choice: 1 - encrypt the text; else decrypt the text
        :param step: displacement step
        :return: file with recorded information
        '''

        txt_from_file = WorkWithFiles(r_file).read_text()
        WorkWithFiles(w_file).write_txt(EngCipher(txt_from_file, step).cipher_txt()) if choice == 1 \
            else WorkWithFiles(w_file).write_txt(EngCipher(txt_from_file, step).decipher_txt())

n = FrequencyImage()
n.img(text='Asaasdf')
