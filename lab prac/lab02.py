import re

matcher = input("Enter any expression for check: ")
intConst = re.match(r"^[+-]?[0-9]+$",matcher)
floatConst =  re.match(r"[+-]?([0-9]+[\.])+[0-9]+",matcher)
charConst = re.match(r"\b[a-zA-Z]\b",matcher)
identifierConst = re.search(r"(?!.*[\_]{2})[\_]{1}[_a-zA-Z0-9]+",matcher)
stringConst = re.match(r"^(?!.*[0-9])[ .a-zA-Z0-9]+$",matcher)

if identifierConst:
    print("identifier")
if intConst:
    print("int")
if floatConst:
    print("float")
if stringConst:
    print("string")
if charConst:
    print("char")
