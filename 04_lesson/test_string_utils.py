import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_reverse_string(string_utils):
    assert string_utils.reverse_string("hello") == "olleh"
    assert string_utils.reverse_string("world") == "dlrow"
    assert string_utils.reverse_string("") == ""
    assert string_utils.reverse_string("a") == "a"
    assert string_utils.reverse_string("12345") == "54321"
    assert string_utils.reverse_string(" hello ") == " olleh "


def test_capitalize_string(string_utils):
    assert string_utils.capitalize_string("hello") == "Hello"
    assert string_utils.capitalize_string("world") == "World"
    assert string_utils.capitalize_string("") == ""
    assert string_utils.capitalize_string("a") == "A"
    assert string_utils.capitalize_string("123") == "123"
    assert string_utils.capitalize_string(" hello") == " hello"


def test_is_palindrome(string_utils):
    assert string_utils.is_palindrome("racecar") is True
    assert string_utils.is_palindrome("Hello") is False
    assert string_utils.is_palindrome("A man a plan a canal Panama") is True
    assert string_utils.is_palindrome("") is True
    assert string_utils.is_palindrome("a") is True
    assert string_utils.is_palindrome("121") is True


def test_count_vowels(string_utils):
    assert string_utils.count_vowels("hello") == 2
    assert string_utils.count_vowels("world") == 1
    assert string_utils.count_vowels("Python") == 1
    assert string_utils.count_vowels("aeiouауоыиэяюё") == 14
    assert string_utils.count_vowels("123") == 0


def test_find_substring(string_utils):
    assert string_utils.find_substring("hello world", "o") == 2
    assert string_utils.find_substring("hello world", "wor") == 1
    assert string_utils.find_substring("hello world", "a") == 0
    assert string_utils.find_substring("ababab", "aba") == 2
    assert string_utils.find_substring("HELLO", "hello") == 1
