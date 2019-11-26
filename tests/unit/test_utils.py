from random import randrange

from fizzbuzz_core.utils import fizzbuzz


def test_fizzbuzz():
    multi_3 = (3 * randrange(-1000, 1000))
    multi_5 = (5 * randrange(-1000, 1000))

    multi_both = (multi_3 * multi_5)

    assert fizzbuzz(multi_3) == 'fizz'
    assert fizzbuzz(multi_5) == 'buzz'
    assert fizzbuzz(multi_both) == 'fizzbuzz'


def test_fizzbuzz_invalid_number():
    test_cases = [
        2, 7, 8, 11
    ]

    for number in test_cases:
        assert fizzbuzz(number) == number
