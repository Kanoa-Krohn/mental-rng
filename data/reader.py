from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent

def read_data(filename):
    path = DATA_DIR / filename
    tokens = path.read_text().split()

    N, n = int(tokens[0]), int(tokens[1])
    values = [int(token) for token in tokens[2:]]

    if len(values) != N:
        raise ValueError(f"Expected {N} values, but got {len(values)}.")

    out_of_range = [value for value in values if value < 1 or value > n]
    if out_of_range:
        raise ValueError(f"Values {out_of_range} are out of the expected range [1, {n}].")

    return values, n