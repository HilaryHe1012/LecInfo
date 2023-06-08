import random

class Trie:

    def __init__(self):
        self.is_word = False
        self.children = [None for _ in range(26)]

    def add_word(self, word):
        if word == "":
            self.is_word = True
        else:
            if self.children[letter_index(word[0])] == None:
                self.children[letter_index(word[0])] = Trie()
            self.children[letter_index(word[0])].add_word(word[1:])

    def check_word(self, word):
        if word == "":
            return self.is_word
        else:
            if self.children[letter_index(word[0])] == None:
                return False
            return self.children[letter_index(word[0])].check_word(word[1:])

    def get_height(self):
        heights = []
        for child in self.children:
            if child != None:
                heights.append(child.get_height())
        if heights == []:
            return 1
        return 1 + max(heights)

    def get_num_words(self):
        num_words = []
        for child in self.children:
            if child != None:
                num_words.append(child.get_num_words())
        if self.is_word:
            return 1 + sum(num_words)
        return sum(num_words)

    def create_random_word(self):
        index_list = []
        for i in range(26):
            if self.children[i] != None:
                index_list.append(i)
        if self.is_word:
            index_list.append(-1)
        j = random.randint(0, len(index_list) - 1)
        j = index_list[j]
        if j == -1:
            return ""
        return char_from_index(j) + self.children[j].create_random_word()


def letter_index(letter):
    return ord(letter) - 97

def char_from_index(i):
    return chr(i+97)