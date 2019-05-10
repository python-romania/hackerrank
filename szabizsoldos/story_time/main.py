import collections
import re


class StoryTime:

    file = ''
    longest_word = ''
    smallest_word = ''

    """
        strip_text is used for striping spaces and removing dots for word boundary
    """
    @staticmethod
    def strip_text(text):
        return re.sub(r'[. \n]', '', text).strip()

    """
        Loading text into memory
    """
    def load_file_to_memory(self):
        with open(FILE_NAME) as file:
            self.file = file.read()

    """
        Counting words with simple split() method    
    """
    def count_words(self):
        temp_words = []
        _total_words = self.file.split()

        for wd in _total_words:
            _wd = self.strip_text(wd).lower()
            if not _wd.isspace() and _wd != "":
                temp_words.append(_wd)

        """
            Getting longest and smallest words
            TODO: there may be multiple words with the same length, then what?
        """
        sorted_words = sorted(temp_words, key=len, reverse=True)
        self.longest_word = sorted_words[0]
        self.smallest_word = sorted_words[-1]

        return temp_words

    """
        Getting most commong N words
        TODO: there may be multiple words with the same length, then what?
    """
    def most_comming_word(self, number_of_words):
        words = collections.Counter(self.count_words())
        return words.most_common(number_of_words)

    """
        Get word occurrences from user input
    """
    def get_specific_word_count(self):
        specific_word = str(input("Check word occurrences for given word, enter one: ")).lower()
        words = collections.Counter(self.count_words())
        if specific_word in words:
            print('"{}" was found with {} occurrences.'.format(specific_word, words[specific_word]))
        else:
            print('"{}" was not found, sorry'.format(specific_word))

    """
        Strip loaded file from memory and save it to a new file.
    """
    def strip_and_save_to_new_file(self):
        file = open(STRIPED_FILE_NAME, 'w')
        file.write(self.strip_text(self.file))



# Application only runs if ran from calculator.py
if __name__ == "__main__":
    FILE_NAME = 'original_story.txt'
    STRIPED_FILE_NAME = 'striped_story.txt'

    story_time = StoryTime()
    story_time.load_file_to_memory()
    total_words = len(story_time.count_words())
    print(str(total_words) + " found in the given file.")
    print("{} is the longest word with a length of {} characters.".format(story_time.longest_word, len(story_time.longest_word)))
    print("{} is the smallest word with a length of {} characters.".format(story_time.smallest_word, len(story_time.smallest_word)))
    most_common_word = story_time.most_comming_word(1)
    if len(most_common_word) > 0:
        for word, occurrences in most_common_word:
            print("{} is the most common word on the given file with {} occurrences.".format(word, occurrences))
    story_time.get_specific_word_count()
    story_time.strip_and_save_to_new_file()
