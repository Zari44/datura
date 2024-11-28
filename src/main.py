
from collections import defaultdict

# lets assume those are all the possible
# puncutations in the text
PUNCTUATION_CHARS = ".,-:;!?"


def word_count(filepath: str) -> dict[str, int]:
    counts = defaultdict(int)

    with open(filepath, "r") as file:
        for line in file:
            for punctuation in PUNCTUATION_CHARS:
                line = line.replace(punctuation, "")
            words = line.split(" ")
            for word in words:
                counts[word.strip().lower()] += 1
    return counts

