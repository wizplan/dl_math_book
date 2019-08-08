import numpy as np

score = [80, 78, 84, 69, 77, 73, 88, 64, 91, 72, 75, 62, 90, 83, 92, 60, 76, 89, 68, 70]

def standardize(x):
    return (x - np.mean(x)) / np.std(x)

print(standardize(score) * 10 + 50)