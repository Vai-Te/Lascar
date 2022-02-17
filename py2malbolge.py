#!/usr/bin/python3

from math import *
from pyfiglet import Figlet
from argparse import ArgumentParser
from src.malbolge_utils import *


def getArgs():
    parser = ArgumentParser(description="Python to Malbolge converter",
                            epilog="Copyright (c) 2002-2013 Canindé, Amsterdam.\nAll Rights Reserved.")

    parser.add_argument('-t', '--text', type=str,
                        help='text to convert')
    parser.add_argument('-f', '--file', type=str,
                        help='file content to convert')
    parser.add_argument('-o', '--output', type=str,
                        help='file to output the result')

    return parser.parse_args()


def main():
    args = getArgs()
    figlet = Figlet(font="acrobatic")
    print(figlet.renderText("Py2Malbolge"))

    if args.file and args.text:
        raise Exception("Can't use both at the same time")

    if file := args.file:
        print("Getting content from file:", file)
        python_code = getFileContent(file)

    elif text := args.text:
        python_code = text
        
    else:
        python_code = input("Enter python code: ")

    malbolge_code = Malbolge.convert(python_code)
    if output := args.output:
        setFileContent(output, malbolge_code)
        print("Malbolge code written to file:", output)

    else:
        print("\nResult in Malbolge language: \n", malbolge_code)


if __name__ == "__main__":
    main()
