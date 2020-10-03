class PrimeGenerator:
    """A class generating all primes from 2 to the argument value"""
    def __init__(self):
        self.list_to_n = []

    def primes_to_max(self, n):
        for num in range(2, n + 1):
            self.list_to_n.append(num)
        divider = 2
        while divider ^ 2 <= n:
            if divider in self.list_to_n:
                for j in range(divider*2, num+1, divider):
                    if j in self.list_to_n:
                        self.list_to_n.remove(j)
            divider += 1
        return self.list_to_n
