from __future__ import print_function

import sys

from .application import unwrap_raw


def main():
    if sys.stdin.isatty():
        result = unwrap_raw(sys.argv[1])
    else:
        result = unwrap_raw(sys.stdin.read())
    print(result)
