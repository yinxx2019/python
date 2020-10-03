import re


class DataAnalysis:

    def __init__(self, file):
        # set up the necessary instance variables
        self.languages = {}
        self.tld = {}
        self.total_count = 0

    def read_data(self, file_name):
        # read the data
        try:
            f = open(file_name, encoding="utf8")
        except Exception:
            print("Can't open", file_name)
            return
        for row in f:
            self.total_count += 1
            # split columns
            each_column = row.rstrip("\n").split(",")
            email = each_column[3]  # column for emails
            lang = each_column[6]  # column for languages
            # get all countries in tld
            domain = re.findall(r"[\.]([\w]{2})[$]", email + "$")
            # count lang
            if lang in self.languages.keys():
                self.languages[lang] += 1
            else:
                self.languages[lang] = 1
            # see if there's a country abbrv in tld
            if len(domain) != 0:
                domain = domain[0]
                # count tld
                if domain in self.tld.keys():
                    self.tld[domain] += 1
                else:
                    self.tld[domain] = 1

    def top_n_lang_freqs(self, N):
        # Should take a number N as an argument and return an N-length list of
        # tuples representing languages and their frequencies in the data,
        # ordered from highest frequency to lowest.
        sorted_lang = sorted(self.languages.items(),
                             key=lambda x: x[1],
                             reverse=True)
        lang_freqs = [(item, round((count/self.total_count), 3))
                      for (item, count) in sorted_lang]
        return lang_freqs[:(int(N))]

    def top_n_country_tlds_freqs(self, N):
        # Should take a number N as an argument and return an N-length list of
        # tuples representing country (2-letter) top-level domain identifiers
        # and their frequencies as email domains the data, ordered
        # from highest frequency to lowest.
        sorted_tld = sorted(self.tld.items(),
                            key=lambda x: x[1],
                            reverse=True)
        tld_freqs = [(item, round((count/self.total_count), 3))
                     for (item, count) in sorted_tld]
        return tld_freqs[:(int(N))]
