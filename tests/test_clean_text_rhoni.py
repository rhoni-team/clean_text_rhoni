"""Tests for main clean_text_rhoni module
"""

from clean_text_rhoni.clean_text_rhoni import clean_text, clean_text_snake_case


def __load_text(input_file):
    """Load text from a text file
    """
    with open(input_file, "r") as file:
        text = file.read()
    return text

raw_text = __load_text(input_file="tests/cortazar_axolotl.txt")


def test_clean_text():
    """Unit test for complete_clean_text
    """
    expected_text = __load_text(input_file="tests/expected_clean_text.txt")
    
    result_text = clean_text(text=raw_text)

    assert expected_text == result_text


def test_clean_text_snake_case():
    """Unit test for clean_text_snake_case
    """
    expected_text = __load_text(input_file="tests/expected_snake_case.txt")
    
    result_text = clean_text_snake_case(text=raw_text)

    assert expected_text == result_text
