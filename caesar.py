from abc import abstractmethod
from workWithFile import *


class CaesarCipher(Funcs):
    def __init__(self, information: str, step: int):
        self.information = information
        self.step = step

    @abstractmethod
    def cipher_txt(self):
        pass

    @abstractmethod
    def decipher_txt(self):
        pass


class EngCaesarCipher(CaesarCipher):
    eng_alph_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_alph = eng_alph_up+'abcdefghijklmnopqrstuvwxyz'
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
            elif i.isupper():
                ciphered_txt += self.eng_alph[self.ciph_by_step(len(self.eng_alph_up),
                                                                     self.step, self.eng_alph_up.index(i))]
            else:
                ciphered_txt += self.eng_alph[self.ciph_by_step(len(self.eng_alph_up), self.step,
                                                                     self.eng_alph_up.index(i.upper())) + len(self.eng_alph_up)]
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
            elif i.isupper():
                deciphered_txt += self.eng_alph_up[self.deciph_by_step(len(self.eng_alph_up),
                                                                       self.step, self.eng_alph_up.index(i))].upper()
            else:
                deciphered_txt += self.eng_alph_up[self.deciph_by_step(len(self.eng_alph_up), self.step,
                                                                       self.eng_alph_up.index(i.upper()))].lower()
        n = FrequencyImage()
        n.img(deciphered_txt)
        return deciphered_txt


class UkrCaesarCipher(CaesarCipher):
    __ukrLangUp = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    __ukrLang = __ukrLangUp + 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

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
            elif i.isupper():
                ciphered_txt += self.__ukrLang[self.ciph_by_step(len(self.__ukrLangUp),
                                                                 self.step, self.__ukrLangUp.index(i))]
            else:
                ciphered_txt += self.__ukrLang[self.ciph_by_step(len(self.__ukrLangUp), self.step,
                                                                 self.__ukrLangUp.index(i.upper()))+len(self.__ukrLangUp)]
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
            elif i.isupper():
                deciphered_txt += self.__ukrLangUp[self.deciph_by_step(len(self.__ukrLangUp),
                                                                 self.step, self.__ukrLangUp.index(i))].upper()
            else:
                deciphered_txt += self.__ukrLangUp[self.deciph_by_step(len(self.__ukrLangUp), self.step,
                                                                     self.__ukrLangUp.index(i.upper()))].lower()
        n = FrequencyImage()
        n.img(deciphered_txt)
        return deciphered_txt

