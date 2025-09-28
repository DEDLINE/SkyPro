class StringUtils:

    def __init__(self):
        pass

    def reverse_string(self, s: str):

        return s[::-1]

    def capitalize_string(self, s: str):

        return s.capitalize()

    def is_palindrome(self, s: str):

        s = s.lower().replace(" ", "")
        return s == s[::-1]

    def count_vowels(self, s: str):

        vowels = "aeiouауоыиэяюё"
        count = 0
        for char in s.lower():
            if char in vowels:
                count += 1
        return count

    def find_substring(self, main_string: str, sub_string: str):

        return main_string.lower().count(sub_string.lower())
