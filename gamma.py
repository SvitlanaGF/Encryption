from random import randrange, choice
from string import ascii_letters, digits
from workWithFile import *


class GammaCiph:

    gammas = WorkWithFiles('gammas.txt')

    def __init__(self, information, lang):
        self.information = information
        self.lang = lang

    def encrypt(self):
        new_str = ''
        list_of_keys = []
        for i in self.information:
            if not i.isalpha():
                new_str += i
                list_of_keys.append(-10)
            elif i.isupper():
                n = randrange(len(self.lang))
                new_str += self.lang[Funcs.ciph_by_step(len(self.lang), n, self.lang.index(i))]
                list_of_keys.append(n)
            else:
                n = randrange(len(self.lang))
                new_str += self.lang[Funcs.ciph_by_step(len(self.lang), n, self.lang.index(i.upper()))].lower()
                list_of_keys.append(n)
        key = ''.join(choice(ascii_letters + digits) for i in range(10))
        self.gammas.write(f'{key}--{list_of_keys}')
        print('Key:', key)
        return new_str

    def decrypt(self, key):
        new_str = ''
        keys = self.gammas.read()
        for i in keys:
            if key == i[0]:
                list_of_keys = [int(k) for k in i[1]]
                for j in range(len(self.information)):
                    if not self.information[j].isalpha():
                        new_str += self.information[j]
                    elif self.information[j].isupper():
                        new_str += self.lang[
                            Funcs.ciph_by_step(len(self.lang), len(self.lang) + self.lang.index(self.information[j]),
                                               -list_of_keys[j] % len(self.lang))]
                    else:
                        new_str += self.lang[
                            Funcs.ciph_by_step(len(self.lang), len(self.lang) + self.lang.index(self.information[j].upper()),
                                               -list_of_keys[j] % len(self.lang))].lower()
                return new_str

