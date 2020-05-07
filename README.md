justify
=======

Justifies each paragraph of the input text to fill the page width.

When a block of text is justified, each line fills the entire space from left to right, except for the last line of a paragraph.
This is accomplished by adjusting the space between words and characters in each line so that the text fills 100% of the space.
The result is a straight margin on each side of the page.

Each input line is considered a separate paragraph. Words longer than the width would be placed on their own lines.

# Requirements:

* python >= 3.7

# Installation

Just clone the repository with `justify.py`.

# Usage

```
$ ./justify.py -h
usage: justify.py [-h] -w WIDTH [file]

Justifies each paragraph of the input text to fill the page width.

positional arguments:
  file                  input file (file name or - for stdin, defaults to stdin)

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        page width (greater than 0)
```

# Example

```
$ ./justify.py -w 20 <<< \
> "This is a sample text but a complicated problem to be solved,\
> so we are adding more text to see that it actually works."
This  is  a   sample
text      but      a
complicated  problem
to be  solved,so  we
are adding more text
to   see   that   it
actually      works.
```

# Test

1. Run `pip install -r dev_requirements.txt` to install dependencies
2. Run `pytest`
