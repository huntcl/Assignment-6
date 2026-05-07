# Author: Clara Hunt
# Github username: huntcl
# Date: 05/06/26
# Description: Returns the sample standard deviation of word lengths in a string.

def word_length_std_dev(text):
    """
    Returns the sample standard deviation of word lengths in a string.
    """
    words = text.split()

    if len(words) <= 1:
        return 0.0

    lengths = []

    for word in words:
        lengths = lengths + [len(word)]

    mean = sum(lengths) / len(lengths)

    total = 0

    for length in lengths:
        total = total + (length - mean) ** 2

    variance = total / (len(lengths) - 1)

    return variance ** 0.5

