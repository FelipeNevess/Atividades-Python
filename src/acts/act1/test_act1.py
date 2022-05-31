import pytest
from multiplos import soma_multiplos


def test_should_return_the_result_the_range_100():
    assert soma_multiplos() == 233168


def test_should_return_the_result_the_range_20():
    assert soma_multiplos(10) == 23


def test_should_return_a_type_error_if_a_value_other_than_integer_is_passed():
    with pytest.raises(
        TypeError, match="O tipo <class 'str'> não é um tipo inteiro"
    ):
        soma_multiplos('1000')
