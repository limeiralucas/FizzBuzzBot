from random import randrange

from fizzbuzz_core.utils import fizzbuzz


def test_fizzbuzz():
    """
    Fizzbuzz function should return:
    fizz to multiples of 3
    buzz to multiples of 5
    fizzbuzz to multiples of 3 and 5
    """
    multi_3 = [-27, -12, -9, -3, 3, 9, 12, 27]
    multi_5 = [-80, -35, -10, -5, 5, 10, 35, 80]

    for number in multi_3:
        assert fizzbuzz(number) == 'fizz'

    for number in multi_5:
        assert fizzbuzz(number) == 'buzz'

    for i in range(len(multi_3)):
        number = multi_3[i] * multi_5[i]
        assert fizzbuzz(number) == 'fizzbuzz'


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
