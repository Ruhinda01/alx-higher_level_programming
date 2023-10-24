#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        error_msg = "Exception: " + str(e)
        sys.stderr.write(error_msg + "\n")
        return False
