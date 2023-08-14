"""
Main module.
It imports the CleanText class with base functions to clean and normalize text,
and derived functions that combines cleaning processes. 
"""
from .clean_text import CleanText


def complete_clean_text(text):
    """
    Perform a complete text cleaning process on the input text.

    This function utilizes the `CleanText` utility class to perform a series of text cleaning operations,
    including:
    1. Trimming leading and trailing spaces.
    2. Removing multiple spaces and replacing them with a single space.
    3. Converting the text to lowercase.
    4. Removing accents from vowels.
    5. Removing special characters.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text after applying all cleaning operations.
    Example: "   Hola Sofía!,   cómo estás?   " will be converted to "hola sofia como estas".
    """
    clean_text_utils = CleanText()
    text = clean_text_utils.trim_leading_spaces(text)
    text = clean_text_utils.replace_multiple_spaces(text)
    text = clean_text_utils.to_lowercase(text)
    text = clean_text_utils.remove_accents(text)
    text = clean_text_utils.remove_special_characters(text)
    return text

def normalize_text(text):
    """
    Normalize an input text in a way that can be easily processed.

    This function utilizes the `CleanText` utility class to perform a series of text cleaning operations,
    including:
    1. Trimming leading and trailing spaces.
    2. Removing multiple spaces and replacing them with a single space.
    3. Converting the text to lowercase.
    4. Removing accents from vowels.
    5. Removing special characters.
    6. Replacing spaces by underscores

    Args:
        text (str): The input text to be normalized.

    Returns:
        str: The normalized text after applying all cleaning operations.

    Example: "   Hola Sofía!,   cómo estás?   " will be converted to "hola_sofia_como_estas".
    """
    text = complete_clean_text(text=text)
    clean_text_utils = CleanText()
    text = clean_text_utils.replace_spaces_by_underscores(text)
    return text
