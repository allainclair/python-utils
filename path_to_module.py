"""Transform a Python string path -> module path to stdout
e.g. my/path/to/the/file.py -> my.path.to.the.file
"""
from sys import argv


def main() -> None:
    path = argv[1]
    strings = path.split("/")
    module_name = strings[-1].removesuffix(".py")
    print(".".join(strings[:-1] + [module_name]))


if __name__ == "__main__":
    main()
