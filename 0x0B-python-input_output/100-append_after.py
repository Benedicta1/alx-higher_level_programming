#!/usr/bin/python3
"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific
    string."""


    with open(filename, 'r+', encoding='utf-8') as curr_file:
        lines = curr_file.readlines()
        curr_file.seek(0)
        for b, line in enumerate(lines):

            if search_string in line:
                lines[b] = line + new_string
        curr_file.writelines(lines)
