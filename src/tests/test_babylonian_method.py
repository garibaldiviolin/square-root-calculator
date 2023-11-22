import pytest
from decimal import Decimal

from square_root_calculator.babylonian_method import calculate_square_root


@pytest.mark.parametrize("square_number,expected_square_root", [
    (16, Decimal("4.0")),
    (9999999, Decimal("3162.277502054492370732654092")),
    (96292869029449, Decimal("9812893.0")),
])
def test_calculate_square_root(square_number, expected_square_root):
    assert calculate_square_root(square_number) == expected_square_root
