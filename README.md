# clean_text_rhoni

Package designed to perform various text cleaning and manipulation operations on input strings. It provides methods to transform and modify text in a consistent way.

## Installation

```bash
$ pip install clean_text_rhoni
```

## Usage

This package has 2 main functions to clean a text from special characters, extra spaces, tildes, and transform it to lowercase.

```bash
from clean_text_rhoni.clean_text_rhoni import clean_text, clean_text_snake_case

sample_text = "%ábdc    efghí   %$ñ"

# clean_text()
# run a complete cleaning over a text

cleaned_text = clean_text(sample_text)
print(cleaned_text) # 'abdc efghi n'

# clean_text_snake_case()
# run a complete cleaning over a text and return the result in snake_case style

snake_case_cleaned_text = clean_text_snake_case(sample_text)
print(snake_case_cleaned_text) # abdc_efghi_n

```

You can also access the base class CleanText and use its methods separately:

```bash
from clean_text_rhoni.clean_text_rhoni import CleanText

# create a class instance
instance_clean_text = CleanText()

instance_clean_text.remove_accents("áéíóú") #'aeiou'

instance_clean_text.replace_underscores_by_spaces("hello_world") #'hello world'

# To inspect all the class methods do:
dir(CleanText())

```


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`clean_text_rhoni` was created by rhoni. It is licensed under the terms of the MIT license.

## Credits

`clean_text_rhoni` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
