import string


class TextProcessor(object):
    # перелік знаків пунктуації
    def __init__(self):
        self._punktuation = string.punctuation

    # прибираємо знаки пунктуації з переліку string.punctuation
    def get_clean_text(self, text):
        clean_text = text.translate(str.maketrans('', '', self._punktuation))
        return clean_text

    # перевірка символу у переліку string.punctuation
    def __is_punctiantian(self, symb):
        return symb in self._punktuation


class TextLoader:
    # ініціалізація
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ""

    # очищуємо текст та зберігаємо у змінну clean_string
    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_text(text)

    # повертаємо значення очищеної змінної
    def get_clean_text(self):
        return self.__clean_string


class DataInterface:
    # ініціалізація
    def __init__(self):
        self._text_loader = TextLoader()

    # обробка списку та вивід у консоль
    def process_text(self, list_text):
        for i in range(len(list_text)):
            self._text_loader.set_clean_text(list_text[i])
            print(self._text_loader.get_clean_text())


proc = TextProcessor()
print(proc.get_clean_text("P5Nb!"))
# don`t do that!
print(proc._TextProcessor__is_punctiantian('~'))

text_loader = TextLoader()
text_loader.set_clean_text("=g6+V")
print(text_loader.get_clean_text())

my_list = ["$F@sv", "MTJNd", "E2z6Z", "qax*y"]
data_interface = DataInterface()
data_interface.process_text(my_list)
