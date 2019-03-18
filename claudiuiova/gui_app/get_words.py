import itertools
import nltk
import time
import multiprocessing as mp


class Words(object):
    def __init__(self, random_string='', word_length=2):
        """
        Object initialization
        :param random_string: random string used to create words
        :param word_length: desired length of the word
        """
        self.words_list = self.get_words()
        self.random_string = list(random_string)
        self.word_length = word_length

    @staticmethod
    def get_words():
        try:
            return nltk.corpus.words.words()
        except LookupError:
            nltk.download('words')
            return nltk.corpus.words.words()

    def create_words(self):
        return [''.join(x) for x in itertools.permutations(self.random_string, self.word_length)]

    def get_english_words(self, obtained_permutations):
        bag_of_english_words = []
        for word in obtained_permutations:
            if word in self.words_list:
                bag_of_english_words.append(word)

        return bag_of_english_words

    def get_english_words_with_multiprocessing(self):
        procs = mp.cpu_count()
        p = mp.Pool(procs)
        fls = list(set(self.create_words()))
        split_fls = [fls[i * len(fls) // procs: (i + 1) * len(fls) // procs] for i in range(procs)]

        return list(itertools.chain(*p.map(self.get_english_words, split_fls)))


if __name__ == "__main__":
    wd = Words(random_string="dfasfg", word_length=4)

    # test 1
    start = time.time()
    print(wd.get_english_words_with_multiprocessing())
    print(time.time() - start)

    # test 2
    # start1 = time.time()
    # x = wd.create_words()
    # f = wd.get_english_words(x)
    # print(time.time() - start1)





