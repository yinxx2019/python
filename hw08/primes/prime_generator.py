class PrimeGenerator:
    """A class generating all primes from 2 to the argument value"""
    def __init__(self):
        self.composite_set = set()
        self.prime_list = []

    def primes_to_max(self, n):
        divider = 2
        # test all divider smaller than n
        while divider <= n:
            for i in range(2, n + 1):  # starts at 2 since 1 is not prime
                if i % divider == 0 and i != divider:
                    # get hall composite
                    self.composite_set.add(i)
            divider += 1
        for k in range(2, n + 1):
            if k not in self.composite_set:
                # if k is not a composite, it is a prime
                self.prime_list.append(k)
        return self.prime_list
