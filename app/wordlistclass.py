class WordListClass():
    """
    Contains the word lists needed for URL link generation.
    """
    def __init__(self, first_list, second_list):
        self.first_list = []
        with open(first_list, 'r') as file:
            self.first_list = file.read().split('\n')

        self.second_list = []
        with open(second_list, 'r') as file:
            self.second_list = file.read().split('\n')

wordlist = WordListClass('app/static/adjectives.txt', 'app/static/animals.txt')
