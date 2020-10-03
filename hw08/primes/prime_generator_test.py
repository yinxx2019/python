from prime_generator import PrimeGenerator


def test_primes_to_max():
    p = PrimeGenerator()
    # test the list within primes smaller or equal to 100
    p_100 = p.primes_to_max(100)
    assert p_100 == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                     53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert 10 not in p_100
    # test the list within primes smaller or equal to 1000
    p_1000 = p.primes_to_max(1000)
    assert 877 in p_1000
    assert 409 in p_1000
    assert 555 not in p_1000
    # test the list within primes smaller or equal to 3966
    p_3966 = p.primes_to_max(3966)
    assert 991 in p_3966
    assert 3119 in p_3966
    # even 3967 is a prime, it is out of index of 3966 so it shouldn't in it
    assert 3967 not in p_3966
    assert 2688 not in p_3966
