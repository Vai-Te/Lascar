from pyfiglet import Figlet
from random import choice, seed
from string import ascii_letters as letters,\
    digits, punctuation

seed(38)
baitolagem = letters + digits + punctuation
viadagem = Figlet(font="Slant")

converter = lambda code: "".join(choice(baitolagem)
                         for _ in range(len(code)))


if __name__ == "__main__":
    print(viadagem.renderText("Python to Malbolge"))

    python_code = input("Insira o codigo em python:")
    malbolge_code = converter(python_code)
    print("\nResultado em Malbolge language:\n", malbolge_code)