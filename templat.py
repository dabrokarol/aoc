import numpy as np


def read_file(filename):
    """Returns a list of lines from a file or from stdin if file not found

    Args:
        filename (str): The path to the file to be read.

    Raises:
        ValueError: If the input is empty.

    Returns:
        str: A list of lines from the file or from stdin.
    """
    try:
        with open(filename, "r") as f:
            lines = f.read().strip()
    except FileNotFoundError:
        print("File not found. Enter input manually (empty line to finish):")
        lines = ""
        while True:
            line = input().strip()
            if line == "":
                break
            lines += "\n" + line
    if not lines.strip():
        raise ValueError("Input is empty.")
    return lines.split("\n")


def log(*args, **kwargs):
    """Acts as a print statement if LOG is True."""
    if LOG:
        print(*args, **kwargs)


def parse_input(filename):
    """Extracts the relevant information from the input file.

    Args:
        filename (str): The path to the file to be read.

    Returns:
        np.array: An array of the relevant information.
    """
    lines = read_file(filename)
    ...


## Constants: ################################
LOG = False
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # often used in grid problems
##############################################


def solve1(arr): ...


def solve2(arr): ...


if __name__ == "__main__":
    LOG = True
    arr = parse_input("in")
    solve1(arr)
    solve2(arr)
