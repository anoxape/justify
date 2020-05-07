#!/usr/bin/env python3
"""Justifies each paragraph of the input text to fill the page width.

When a block of text is justified, each line fills the entire space from left to right, except for the last line of a paragraph.
This is accomplished by adjusting the space between words and characters in each line so that the text fills 100% of the space.
The result is a straight margin on each side of the page.

Each input line is considered a separate paragraph. Words longer than the width would be placed on their own lines.
"""

from typing import Iterable, Iterator, List


def stretcher(line: List[str], add_space: int) -> Iterator[str]:
    """Generator function to stretch the single line using spaces.

    :param line: line to stretch as a list of words
    :param add_space: total number of spaces to add between the words
    :return: stretched line as an iterable of words and spaces
    """
    # check if there are words and space to stretch
    if add_space > 0 and len(line) > 1:
        gaps = len(line) - 1
        space_per_gap, extra_space = divmod(add_space, gaps)

        # first put space_per_gap between the words
        separator = ' ' * space_per_gap
        for i in range(gaps - extra_space):
            yield line[i]
            yield separator

        # then put space_per_gap and spread the extra_space between the last words
        separator = ' ' * (space_per_gap + 1)
        for i in range(gaps - extra_space, gaps):
            yield line[i]
            yield separator

    # emit either the final word or the only one
    yield line[-1]


def justifier(words: Iterable[str], width: int) -> Iterator[str]:
    """Generator function to justify a paragraph to fill the page width.

    :param words: an iterable of words to justify
    :param width: page width in symbols
    :return: justified text as an iterator of justified lines
    """
    if width <= 0:
        raise ValueError('width must be greater than 0')

    # accumulate line keeping count of the available space
    line, space = [], width
    for word in words:
        # space can be negative if the word is longer than the width
        if len(line) > 0 and len(line) + len(word) > space:
            # emit the full line
            yield ''.join(stretcher(line, space))
            line, space = [], width
        # collect word
        line.append(word)
        space -= len(word)

    # emit the last line
    if len(line) > 0:
        yield ''.join(stretcher(line, space))


def justify(text: str, width: int) -> List[str]:
    """Justify a paragraph to fill the page width.

    Splits text by unicode whitespace, calls helper function, then materializes iterator to list.

    :param text: a single paragraph of text to justify
    :param width: page width in symbols
    :return: justified text as a list of justified lines
    """
    return list(justifier(text.split(), width))


def main():
    import argparse, sys

    def positive(string: str) -> int:
        """Parse an argument and check if it is a positive number.

        :param string: argument to parse
        :return: parsed argument as int
        :raises argparse.ArgumentTypeError: if the argument is not a positive number
        """
        value = int(string)
        if value <= 0:
            raise argparse.ArgumentTypeError(f"invalid positive value: '{value}'")
        return value

    # parse arguments
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('file', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                        help='input file (file name or - for stdin, defaults to stdin)')
    parser.add_argument('-w', '--width', dest='width', type=positive, required=True,
                        help='page width (greater than 0)')
    args = parser.parse_args()

    # justify each line of the input file as a separate paragraph and print the result
    with args.file as file:
        for line in file.readlines():
            print('\n'.join(justify(line, args.width)))


if __name__ == '__main__':
    main()
