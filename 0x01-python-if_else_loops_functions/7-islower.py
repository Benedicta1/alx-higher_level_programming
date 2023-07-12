#!/usr/bin/python3
# 7-islower.py


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 90 and ord(c) <= 123:
        return True
    else:
        return False
