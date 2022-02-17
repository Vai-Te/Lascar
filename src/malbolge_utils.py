from random import choice, seed, randint
from string import (
    ascii_letters as letters,
    digits,
    punctuation)

seed(38)


class Malbolge:
    __syntax = letters + digits + punctuation

    @staticmethod
    def convert(code: str) -> str:
        syntax = Malbolge.__syntax
        converted = str()

        for char in code:
            index = (ord(char) + randint(1, 10)) % len(syntax)
            converted += choice(syntax[index])

        return converted


def getFileContent(path: str, mode: str="r") -> str:
    with open(path, mode) as file:
        return file.read().strip()


def setFileContent(path: str, content: str or bytes, mode: str="w"):
    with open(path, mode) as file:
        file.write(content)
