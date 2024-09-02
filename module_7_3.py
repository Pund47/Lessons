
class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                lines = file.read().lower()
                line = lines.split()
                all_words[file_name] = line
                return all_words
    def find(self, word):
        text = self.get_all_words()
        positions = {}
        for file_name, words in text.items():
            pos = words.index(word.lower())
            positions[file_name] = pos
            return positions
    def count(self, word):
        text = self.get_all_words()
        counts = {}
        for file_name, words in text.items():
            pos = words.count(word.lower())
            counts[file_name] = pos
            return counts

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))