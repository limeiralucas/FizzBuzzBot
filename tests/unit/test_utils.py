from random import randrange

from fizzbuzz_core.utils import fizzbuzz


def test_fizzbuzz():
    """
    Fizzbuzz function should return:
    fizz to multiples of 3
    buzz to multiples of 5
    fizzbuzz to multiples of 3 and 5
    """
    multi_3 = (3 * randrange(-1000, 1000))
    multi_5 = (5 * randrange(-1000, 1000))

    multi_both = (multi_3 * multi_5)

    assert fizzbuzz(multi_3) == 'fizz'
    assert fizzbuzz(multi_5) == 'buzz'
    assert fizzbuzz(multi_both) == 'fizzbuzz'


def test_fizzbuzz_invalid_number():
    """
    When the number passed to fizzbuzz
    is not a multiple of 3 or 5,
    it should return the same number
    """
    test_cases = [
        2, 7, 8, 11
    ]

    for number in test_cases:
        assert fizzbuzz(number) == number
