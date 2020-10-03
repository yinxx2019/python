class TextCleaner:
    ''' carry out the text pre-processing'''
    def __init__(self, f):
        self.all_lines = []
        self.f = f
        self.pre_dot = ["mr.", "ms.", "mrs.", "dr.", "miss.", "sir."]
        self.pre_clean = ["mr", "ms", "mrs", "dr", "miss", "sir"]
        self.punctuations = ["\"", "(", ")"]

    def format(self):
        for line in self.f:
            line = line.lower()
            line = line.replace(",", " COMMA")
            # handle prefixes
            i = 0
            while i < len(self.pre_dot):
                line = line.replace(self.pre_dot[i], self.pre_clean[i])
                i += 1
            # handle punctuations
            for item in self.punctuations:
                line = line.replace(item, "")
            # split to a list of sentences
            line = line.split(".")
            self.all_lines.extend(line)
        return self.all_lines
