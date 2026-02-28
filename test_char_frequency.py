import unittest
from char_frequency import count_character_frequency

class TestCountCharacterFrequency(unittest.TestCase):
    
    # --- Original Tests ---
    
    def test_example_case(self):
        """Standard sentence with repeated letters and spaces."""
        result = count_character_frequency("hello world")
        self.assertEqual(result, "h:1, e:1, l:3, o:2, w:1, r:1, d:1")
        print("Passed: Standard example case.")
        
    def test_empty_string(self):
        """The smallest possible valid input."""
        self.assertEqual(count_character_frequency(""), "")
        print("Passed: Empty string case.")
        
    def test_case_sensitivity(self):
        """Verifies that 'A' and 'a' are unique keys."""
        self.assertEqual(count_character_frequency("AaA"), "A:2, a:1")
        print("Passed: Case sensitivity case.")

    # --- New Edge Cases ---

    def test_all_spaces(self):
        """Edge Case: String containing only ignored characters."""
        self.assertEqual(count_character_frequency("   "), "")
        print("Passed: String with only spaces.")

    def test_special_characters_and_emojis(self):
        """Edge Case: Non-alphanumeric characters and Unicode symbols."""
        # Note: Depending on your Python version/OS, emojis are 1-2 chars, 
        # but Python 3 handles them as single Unicode characters.
        self.assertEqual(count_character_frequency("!@#! 🔥🔥"), "!:2, @:1, #:1, 🔥:2")
        print("Passed: Special characters and emojis.")

    def test_numbers_and_punctuation(self):
        """Edge Case: Mixing digits and syntax."""
        self.assertEqual(count_character_frequency("1221..."), "1:2, 2:2, .:3")
        print("Passed: Numbers and punctuation.")

    def test_first_appearance_order(self):
        """Edge Case: Verifies the dictionary correctly follows appearance order."""
        # 'z' is last in alphabet but first in string.
        # 'a' is first in alphabet but last in string.
        self.assertEqual(count_character_frequency("zebra"), "z:1, e:1, b:1, r:1, a:1")
        print("Passed: First appearance ordering.")

    def test_long_string(self):
        """Edge Case: Large input to ensure efficiency."""
        long_str = "a" * 1000 + "b" * 500
        self.assertEqual(count_character_frequency(long_str), "a:1000, b:500")
        print("Passed: Long string performance.")

    # --- Error Handling ---

    def test_type_error_handling(self):
        """Verifies that the program rejects non-string types."""
        inputs = [123, None, ["a", "b"], {"key": "val"}, 4.5]
        for i in inputs:
            with self.assertRaises(TypeError):
                count_character_frequency(i)
        print(f"Passed: Validated {len(inputs)} non-string types for TypeError.")

if __name__ == '__main__':
    print("--- Starting Comprehensive Edge Case Tests ---\n")
    unittest.main()