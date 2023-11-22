from decimal import Decimal

SQUARE_ROOT_PRECISON = 0.000000000001


def calculate_initial_estimate(square_number: int) -> int:
    """Calculate the initial estimate for square root based on the
    length of the square number. The initial estimate is the number
    with 1 and a sequence of zeros with the absolute number of the
    square number digits's half. In other words, if the square_number
    is for example 7_777, the initial estimate is 10."""
    length = len(str(square_number))
    zeros = (length // 2)
    return 10 ** zeros


def calculate_square_root(square_number: int) -> Decimal:
    square_root_estimate = calculate_initial_estimate(square_number)
    estimate_square = square_root_estimate ** 2

    while abs(square_number - estimate_square) > SQUARE_ROOT_PRECISON:
        square_root_estimate = (
            Decimal(square_number) / Decimal(square_root_estimate)
                + Decimal(square_root_estimate)
        )
        square_root_estimate /= 2
        estimate_square = square_root_estimate ** 2

    has_integer_square_root = int(square_root_estimate) ** 2 == square_number
    if has_integer_square_root is True:
        return Decimal(int(square_root_estimate))
    return square_root_estimate
