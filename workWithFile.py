import matplotlib.pyplot as plt


class WorkWithFiles:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write_txt(self, information: str):
        '''
        :param information: text you want to write into file
        '''
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(information)
        print(f'The information has been written into the file "{self.file_path}"')

    def read_text(self):
        '''
        :return: string with an information from the file
        '''
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def write(self, information):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write(information)
        print(f'The information has been written into the file "{self.file_path}"')

    def read(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            n = f.readlines()
        l = []
        for i in n:
            st = i[:i.index('-')]
            nums = i[i.index('[')+1:i.index(']')].split(',')
            l.append([st, nums])
        return l


class Funcs:
    @staticmethod
    def ciph_by_step(length_of_str, step, letter):
        return (step+letter) % length_of_str

    @staticmethod
    def deciph_by_step(length_of_str, step, letter):
        return letter-step % length_of_str


class FrequencyImage:
    @staticmethod
    def img(text: str):
        x_letters = list(set([i for i in text]))
        y_count = [text.count(i) for i in x_letters]
        plt.title('Frequency')
        plt.bar(x_letters, y_count)
        plt.show()
