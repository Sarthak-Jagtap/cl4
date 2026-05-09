#!/usr/bin/python3

import sys

for line in sys.stdin:

    line = line.strip()

    student, marks = line.split("\t")

    marks = int(marks)

    if marks >= 90:
        grade = "A"

    elif marks >= 80:
        grade = "B"

    elif marks >= 70:
        grade = "C"

    elif marks >= 60:
        grade = "D"

    else:
        grade = "F"

    print(f"{student}\tAverage = {marks} Grade = {grade}")
