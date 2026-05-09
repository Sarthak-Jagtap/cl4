#!/usr/bin/python3

import sys

for line in sys.stdin:

    line = line.strip()

    fields = line.split(",")

    student = fields[0]

    marks = fields[1]

    print(f"{student}\t{marks}")
