#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        ben = fct(*args)
    except BaseException as a:
        ben = None
        print("Exception: {}".format(a), file=sys.stderr)
    finally:
        return ben
