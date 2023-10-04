#!/usr/bin/python3


for li in range(122, 96, -1):
    if li % 2 == 0:
        new = li
    else:
        new = li - 32
    print("{}".format(chr(new)), end="")
