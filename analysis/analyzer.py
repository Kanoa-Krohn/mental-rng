from math import log2, log
from pathlib import Path
from scipy.stats import chisquare
import sys

HERE = Path(__file__).resolve().parent
sys.path.append(str(HERE.parent / "data"))

from reader import read_data

def main():
    # Read data
    print("Enter the name of the file to analyze (e.g., 'data.txt'):", end=" ")
    file_name = input().strip()
    values, n = read_data(file_name)
    N = len(values)

    # Count occurrences of each value
    occurrence = {str(i): 0 for i in range(1, n + 1)}
    for value in values:
        occurrence[str(value)] += 1

    # ------------------------------ Chi-square test ------------------------------------

    # Perform Chi-square test
    observed = list(occurrence.values())
    expected = [N / n] * n  # Assuming uniform distribution
    chi2_stat, p_value = chisquare(observed, expected)

    print("\nChi-square test results:")
    print(f"Chi-square: {chi2_stat:.2f}   | aim: about {n - 1:.2f}")
    print(f"P-value   : {p_value:.2f}   | aim: above 0.05")

    # -----------------------------------------------------------------------------------

    # -------------------------------- Repeat rate --------------------------------------

    repeat_rate = sum(1 for i in range(1, N) if values[i] == values[i - 1]) / (N - 1)

    print("\nRepeat rate analysis:")
    print(f"Repeat rate: {repeat_rate:.2f}  | aim: about {1 / n:.2f}")

    # -----------------------------------------------------------------------------------

    # ---------------------------- Entropy calculation ----------------------------------

    entropy = -sum((count / N) * log2(count / N) for count in occurrence.values() if count > 0)
    print("\nEntropy analysis:")
    print(f"Entropy: {entropy:.2f} bits | aim: about {log2(n) - (n - 1) / (2 * N * log(2)):.2f} - {log2(n):.2f} bits")

    # -----------------------------------------------------------------------------------

if __name__ == "__main__":
    main()