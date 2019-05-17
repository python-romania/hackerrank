"""
Author: Ibrahim Zarifeh

Project description:
    Giving a file as an input that contains a story, you have to read the file and:
        - Count the words from the text
        - Print the largest word
        - Count and print how many times we can find the word "was"
        - Write the text in another file named story_copy.txt in one line, eliminating the spaces

Created on : 17/05/2019 22:07
"""

from termcolor import colored


def open_file(file_path: str):
    """
    This function opens and reads a file
    :param file_path: Path to file
    :return: List that contains all the words from the file
    """
    f = open(file_path).read().split()

    words = []

    for line in f:
        line = line.replace(".", "")
        line = line.replace(",", "")
        words.append(line)

    return words


def count_word(text_words):
    """
    This function counts all the words available in a list
    :param text_words: List with words to count
    :return: Number of words in the list
    """
    return print(len(text_words))


def get_longest_word(words):
    """
    This function gets the longest word from the list and prints it
    :param words: List with words
    :return: Print the longest word found
    """
    longest_word_length = max(len(word) for word in words)

    longest_word = []

    for word in words:
        if len(word) == longest_word_length:
            longest_word.append(word)

    longest_word = "".join(longest_word)

    return print(longest_word)


def count_specific_word(words, selected_word):
    """
    This function checks for how many time is a specific word repeated in the text
    :param words: List of words
    :param selected_word: Word to check
    :return: Print for how many times was the selected word repeated
    """
    found_word = []

    for word in words:
        if selected_word in word:
            found_word.append(selected_word)

    print(len(found_word))

    return print("The word " + colored(selected_word, 'red') + " is repeated in the text " + str(len(found_word)) +
                 " times")


def write_text_copy(new_filename, text):
    """
    This function copy's the original content into a new file and eliminates all the spaces
    :param new_filename: New Filename to be created
    :param text: Original content
    """
    f = open(new_filename, "w+")
    new_text = "".join(text)
    print(new_text)
    f.write(new_text)


if __name__ == '__main__':
    filename = "story.txt"
    copy_filename = "story_copy.txt"
    specific_word = "was"
    words_list = open_file(filename)
    count_word(words_list)

    get_longest_word(words_list)
    count_specific_word(words_list, specific_word)
    write_text_copy(copy_filename, words_list)
