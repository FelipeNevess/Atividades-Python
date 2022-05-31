import pytest
from fibonacci import taking_fibonacci_values, taking_even_values, sum_values


@pytest.fixture
def list_values_fibinacci4000000():
    return [
        1, 2, 3, 5, 8, 13, 21, 34,
        55, 89, 144, 233, 377, 610,
        987, 1597, 2584, 4181, 6765,
        10946, 17711, 28657, 46368,
        75025, 121393, 196418, 317811,
        514229, 832040, 1346269, 2178309, 3524578
    ]


@pytest.fixture
def list_values_fibinacci10():
    return [1, 2, 3, 5, 8]


@pytest.fixture
def pair_numbers():
    return [2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]


def test_should_return_string_fibonacci_from_limit_4000000(
    list_values_fibinacci4000000
):
    result = taking_fibonacci_values()

    assert len(result) > 0
    assert list_values_fibinacci4000000 == result


def test_should_return_string_fibonacci_from_limit_10(list_values_fibinacci10):
    result = taking_fibonacci_values(10)

    assert len(result) > 0
    assert list_values_fibinacci10 == result


def test_should_return_even_values_correctly(
    list_values_fibinacci4000000,
    pair_numbers
):
    result = taking_even_values(list_values_fibinacci4000000)

    assert len(result) > 0
    assert pair_numbers == result


def test_should_return_the_correct_sum(pair_numbers):
    result = sum_values(pair_numbers)

    assert result > 0
    assert result == 4613732


def test_should_return_a_type_error_if_a_value_other_than_integer_is_passed():
    with pytest.raises(
        TypeError, match="O tipo <class 'str'> não é um tipo inteiro"
    ):
        taking_fibonacci_values('4000000')
