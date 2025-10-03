import pandas as pd
import numpy as np
from PersonalityConverter import PersonalityConverter

def hammingDistance(str1, str2):
    """Calculate the Hamming distance between two strings."""
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    return sum(el1 != el2 for el1, el2 in zip(str1, str2))

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    pc = PersonalityConverter()

    for index, row in df.iterrows():
        pred = pc.convert(row)
        pred = pred.upper()
        actual = row['Actual'].upper()
        err = hammingDistance(pred, actual)
        print(f"Predicted: {pred}, Actual: {actual}, Errors: {err}")

