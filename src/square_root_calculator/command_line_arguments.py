import argparse


def check_positive_integer(value):
    invalid_positive_value_message = (
        f"{value} is an invalid positive integer argument"
    )
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(invalid_positive_value_message)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(invalid_positive_value_message)
    return ivalue


def parse_square_number() -> int:
    parser = argparse.ArgumentParser(description='A square root calculator.')
    parser.add_argument('square_number', type=check_positive_integer,
                        help='input square number for the calculator', default=None)

    args = parser.parse_args()
    return args.square_number
