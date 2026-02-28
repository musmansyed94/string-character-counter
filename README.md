\# String Character Frequency



A Python implementation that counts character occurrences in a string and outputs them in the order of first appearance.



\## 📌 Problem Statement

Write a program that counts character occurrences in a string and outputs them in order of first appearance.



\*\*Example\*\* \*\*Input:\*\* `"hello world"`  

\*\*Output:\*\* `h:1, e:1, l:3, o:2, w:1, r:1, d:1`



\## ✅ Solution Overview

The function processes the input string in a single pass and:

\* \*\*Counts\*\* each character’s frequency.

\* \*\*Preserves\*\* order of first appearance.

\* \*\*Ignores\*\* literal space characters (`" "`).

\* \*\*Returns\*\* formatted output as `"char:count"` pairs separated by commas.



The implementation is efficient, readable, and production-ready.



\## ⚙️ Assumptions

| Feature | Assumption |

| :--- | :--- |

| \*\*Case-sensitive\*\* | `'A'` and `'a'` are treated as different characters. |

| \*\*Whitespace\*\* | Only literal spaces (`" "`) are ignored. Other characters (`\\n`, `\\t`) are counted. |

| \*\*Special Characters\*\* | All characters including digits, punctuation, and emojis are supported. |

| \*\*Empty Input\*\* | Returns an empty string (`""`). |

| \*\*Python Version\*\* | Requires Python 3.7+ (dictionaries preserve insertion order). |



\## 🧠 Approach



1\.  \*\*Validate\*\* input type.

2\.  \*\*Handle\*\* empty string edge case.

3\.  \*\*Iterate\*\* through characters:

&nbsp;   \* Skip literal spaces.

&nbsp;   \* Use a dictionary to track frequency.

4\.  \*\*Format\*\* results preserving insertion order.



\## ⏱ Complexity Analysis

\* \*\*Time Complexity:\*\* $O(n)$ — Single pass through the string.

\* \*\*Space Complexity:\*\* $O(k)$ — Where $k$ is the number of unique characters.

This is optimal for the problem.



\## 💻 Implementation



```python

"""

Module: char\_frequency

Counts character occurrences in order of first appearance.

"""



def count\_character\_frequency(text: str) -> str:

&nbsp;   if not isinstance(text, str):

&nbsp;       raise TypeError(f"Expected a string, but got {type(text).\_\_name\_\_}")



&nbsp;   if not text:

&nbsp;       return ""



&nbsp;   frequencies = {}



&nbsp;   for char in text:

&nbsp;       if char == " ":

&nbsp;           continue

&nbsp;       frequencies\[char] = frequencies.get(char, 0) + 1



&nbsp;   return ", ".join(f"{char}:{count}" for char, count in frequencies.items())



\## 🧪 Test Coverage

The solution includes comprehensive unit tests covering:



\### Standard Cases

\* \*\*Normal sentence\*\*: Validates strings with repeated characters and spaces.

\* \*\*Case sensitivity\*\*: Ensures `'A'` and `'a'` are tracked independently.



\### Edge Cases

\* \*\*Empty string\*\*: Returns an empty result without errors.

\* \*\*Only spaces\*\*: Correctly ignores strings consisting only of whitespace.

\* \*\*Special characters \& Emojis\*\*: Validates Unicode and symbol support.

\* \*\*Numbers \& Punctuation\*\*: Confirms non-alphabetic characters are counted.

\* \*\*Appearance ordering\*\*: Verified that 'z' before 'a' remains in that order.

\* \*\*Performance\*\*: Large input test to confirm linear $O(n)$ scaling.



\### Error Handling

\* \*\*Type validation\*\*: Explicitly raises `TypeError` for non-string inputs (ints, lists, None).







---



\## ▶️ Running Tests

To execute the test suite, run the following command in your terminal:



```bash

python -m unittest test\_char\_frequency.py

