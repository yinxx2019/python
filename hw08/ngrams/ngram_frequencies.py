
class NgramFrequencies():

    def __init__(self, clean_txt):
        self.unigrams = {}
        self.bigrams = {}
        self.trigrams = {}
        self.total_uni_count = 0
        self.total_bi_count = 0
        self.total_tri_count = 0
        self.clean_txt = clean_txt  # pass the value of clean.format()
        self.sorted_uni_counts = []
        self.sorted_bi_counts = []
        self.sorted_tri_counts = []
        self.words = []
        self.all_bigrams = []
        self.all_trigrams = []

    def add_item(self):
        ''' add items to dictionaries for counting purposes'''
        for sentence in self.clean_txt:
            # split the sentence to a list of words
            self.words = sentence.split()
            for unigram in self.words:
                self.total_uni_count += 1
                if unigram in self.unigrams.keys():
                    self.unigrams[unigram] += 1
                else:
                    self.unigrams[unigram] = 1
            # get bigrams
            self.all_bigrams = zip(self.words, self.words[1:])
            for bigram in self.all_bigrams:
                self.total_bi_count += 1
                bigram = bigram[0] + "_" + bigram[1]
                if bigram in self.bigrams.keys():
                    self.bigrams[bigram] += 1
                else:
                    self.bigrams[bigram] = 1
            # get trigrams
            self.all_trigrams = zip(self.words, self.words[1:], self.words[2:])
            for trigram in self.all_trigrams:
                self.total_tri_count += 1
                trigram = trigram[0] + "_" + trigram[1] + "_" + trigram[2]
                if trigram in self.trigrams.keys():
                    self.trigrams[trigram] += 1
                else:
                    self.trigrams[trigram] = 1

    def top_n_counts(self, N):
        ''' take a number N as an argument and return an N-length list of
        tuples representing counts in the grams from highest to lowest'''
        # unigram
        self.sorted_uni_counts = sorted(self.unigrams.items(),
                                        key=lambda x: x[1],
                                        reverse=True)
        # bigram
        self.sorted_bi_counts = sorted(self.bigrams.items(),
                                       key=lambda x: x[1],
                                       reverse=True)
        # trigram
        self.sorted_tri_counts = sorted(self.trigrams.items(),
                                        key=lambda x: x[1],
                                        reverse=True)
        return [self.sorted_uni_counts[:(int(N))],
                self.sorted_bi_counts[:(int(N))],
                self.sorted_tri_counts[:(int(N))]]

    def frequency(self):
        ''' takes an item and returns its frequency'''
        # unigram
        self.uni_freqs = [(item, round((count/self.total_uni_count), 3))
                          for (item, count) in self.sorted_uni_counts]
        # bigram
        self.bi_freqs = [(item, round((count/self.total_bi_count), 3))
                         for (item, count) in self.sorted_bi_counts]
        # trigram
        self.tri_freqs = [(item, round((count/self.total_tri_count), 3))
                          for (item, count) in self.sorted_tri_counts]

    def top_n_freqs(self, N):
        '''return an N-length list of tuples representing frequencies'''
        # unigram
        return [self.uni_freqs[:(int(N))], self.bi_freqs[:(int(N))],
                self.tri_freqs[:(int(N))]]
