#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        error_msg = "Exception: " + str(e)
        sys.stderr.write(error_msg + "\n")
        return None
