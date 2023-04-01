from workWithFile import Funcs


class VigenereCiph:
    def __init__(self, information, motto, lang):
        self.information = information
        self.motto = motto
        self.lang = lang

    def encrypt(self):
        m = ''
        while len(m) < len(self.information):
            m += self.motto
        motto = m[:len(self.information)]
        new_txt = ''
        for i in range(len(self.information)):
            if not self.information[i].isalpha():
                new_txt += self.information[i]
            elif self.information[i].isupper():
                new_txt += self.lang[Funcs.ciph_by_step(len(self.lang), self.lang.index(motto[i].upper()),
                                                        self.lang.index(self.information[i].upper()))]
            else:
                new_txt += self.lang[Funcs.ciph_by_step(len(self.lang), self.lang.index(motto[i].upper()),
                                                        self.lang.index(self.information[i].upper()))].lower()
        return new_txt

    def decrypt(self):
        m = ''
        while len(m) < len(self.information):
            m += self.motto
        motto = m[:len(self.information)]
        new_txt = ''
        for i in range(len(self.information)):
            if not self.information[i].isalpha():
                new_txt += self.information[i]
            elif self.information[i].isupper():
                new_txt += self.lang[Funcs.ciph_by_step(len(self.lang), len(self.lang) +
                                                        self.lang.index(self.information[i].upper()),
                                                        - self.lang.index(motto[i].upper()) % len(self.lang))]
            else:
                new_txt += self.lang[Funcs.ciph_by_step(len(self.lang), len(self.lang) + self.lang.index(self.information[i].upper()),
                                                        - self.lang.index(motto[i].upper()) % len(self.lang))].lower()
        return new_txt
