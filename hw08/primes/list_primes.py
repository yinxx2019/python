import sys
from sieve import PrimeGenerator


def main(n):
    prime = PrimeGenerator()
    print(prime.primes_to_max(n))


main(int(sys.argv[1]))
