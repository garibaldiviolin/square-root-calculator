from command_line_arguments import parse_square_number
from babylonian_method import calculate_square_root


if __name__ == "__main__":
    square_number = parse_square_number()
    square_root = calculate_square_root(square_number)
    print(f"result={square_root}")
