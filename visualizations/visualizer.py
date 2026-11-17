import matplotlib.pyplot as plt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE.parent / "data"))

from reader import read_data

def main():
    # Read data
    print("Enter the name of the file to visualize (e.g., 'data.txt'):", end=" ")
    file_name = input().strip()
    values, n = read_data(file_name)
    N = len(values)

    # Count occurrences of each value
    occurrence = {str(i): 0 for i in range(1, n + 1)}
    for value in values:
        occurrence[str(value)] += 1

    # Create a simple plot
    name = Path(file_name).stem

    plt.bar(list(occurrence.keys()), list(occurrence.values()))
    plt.title(f"{name.capitalize()} Method (N = {N}, range: 1 - {n})")
    plt.xlabel("Values")
    plt.ylabel("Occurrence")
    plt.savefig(HERE / f"{name}.png")

    print("Complete.")

if __name__ == "__main__":
    main()