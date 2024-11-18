def create_file(file_name: str):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("It's a text for task Найти везде,\nИспользуйте его для самопроверки.\nУспехов в решении задачи!\ntext text text")

class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        znaki = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                text = file.read().lower()
                for i in znaki:
                    text = text.replace(i, ' ')
                words = text.split()
            all_words[file_name] = words
        return all_words

    def find(self, word: str):
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                res[name] = words.index(word.lower()) + 1
        return res

    def count(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            sum = words.count(word.lower())
            if sum > 0:
                res[name] = sum
        return res

create_file('test_file.txt')
finder2 = WordsFinder('test_file.txt', "Mother Goose - Monday’s Child.txt")
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.find('child'))
print(finder2.count('teXT'))
print(finder2.count('child'))