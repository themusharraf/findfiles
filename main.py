import sys
from pathlib import Path


def findfile():
    name = sys.argv[1]
    basedir = Path(__file__).resolve().parent.parent

    py_files = basedir.glob(f'*/*{name}')
    return [file for file in py_files]


print(*findfile())
