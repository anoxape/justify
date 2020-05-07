import pytest

from justify import justify


# Width must be greater than 0
def test_zero_width():
    with pytest.raises(ValueError):
        justify('', 0)


# Empty paragraph should result in an empty list
def test_empty_paragraph():
    assert justify('', 1) == []


# Word longer than the width should be placed on its own line
def test_long_word():
    paragraph = 'Hello, world!'
    assert justify(paragraph, 1) == [
        'Hello,',
        'world!'
    ]


# Two words should be kept as one line if the width is just enough
def test_one_line():
    paragraph = 'Hello, world!'
    assert justify(paragraph, len(paragraph)) == [
        'Hello, world!'
    ]


# Two words should be put on two lines if the width is not enough for both
def test_two_lines():
    paragraph = 'Hello, world!'
    assert justify(paragraph, len(paragraph) - 1) == [
        'Hello,',
        'world!'
    ]


# Example from the problem statement
def test_example():
    paragraph = 'This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works.'
    width = 20
    assert justify(paragraph, width) == [
        "This  is  a   sample",
        "text      but      a",
        "complicated  problem",
        "to be solved, so  we",
        "are adding more text",
        "to   see   that   it",
        "actually      works.",
    ]
