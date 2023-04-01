from workWithFile import Funcs


class Vernam:
    def __init__(self, information, lang, message):
        self.information = information
        self.lang = lang
        self.message = message

    def koefs_of_message(self):
        list_of_keys = []
        if len(self.information) == len(self.message):
            for i in self.message:
                if not i.isalpha:
                    return ValueError
                else:
                    list_of_keys.append(self.lang.index(i.upper()))
        return list_of_keys

    def encrypt(self):
        new_str = ''
        list_of_keys = self.koefs_of_message()
        if len(list_of_keys) == len(self.information):
            for i in range(len(self.information)):
                if not self.information[i].isalpha():
                    new_str += i
                elif self.information[i].isupper():
                    new_str += self.lang[Funcs.ciph_by_step(len(self.lang), list_of_keys[i],
                                                            self.lang.index(self.information[i].upper()))]
                else:
                    new_str += self.lang[Funcs.ciph_by_step(len(self.lang), list_of_keys[i],
                                                            self.lang.index(self.information[i].upper()))].lower()
        return new_str

    def decrypt(self):
        new_str = ''
        list_of_keys = self.koefs_of_message()
        for j in range(len(self.information)):
            if not self.information[j].isalpha():
                new_str += self.information[j]
            elif self.information[j].isupper():
                new_str += self.lang[
                    Funcs.ciph_by_step(len(self.lang), len(self.lang) + self.lang.index(self.information[j]),
                                       -list_of_keys[j] % len(self.lang))]
            elif self.information[j].isupper():
                new_str += self.lang[
                    Funcs.ciph_by_step(len(self.lang), len(self.lang) + self.lang.index(self.information[j].upper()),
                                       -list_of_keys[j] % len(self.lang))]
            else:
                new_str += self.lang[
                    Funcs.ciph_by_step(len(self.lang), len(self.lang) + self.lang.index(self.information[j].upper()),
                                       -list_of_keys[j] % len(self.lang))].lower()
        return new_str
