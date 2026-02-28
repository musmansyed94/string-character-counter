"""
Module: char_frequency
Counts character occurrences in order of first appearance.

Assumptions:
- Case-sensitive: 'A' and 'a' are treated as different characters.
- Spaces are ignored; all other characters (digits, punctuation, emojis, etc.) are counted.
- Output format: "char:count" pairs separated by commas, in order of first appearance.
- Empty input returns an empty string.
"""

def count_character_frequency(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, but got {type(text).__name__}")

    if not text:
        return ""

    frequencies = {}

    for char in text:
        if char == " ":  # Only ignore literal spaces, as per your original logic
            continue
        frequencies[char] = frequencies.get(char, 0) + 1

    return ", ".join(f"{char}:{count}" for char, count in frequencies.items())