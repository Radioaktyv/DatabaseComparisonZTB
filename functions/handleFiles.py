import sqlite3
import shutil
from time import time


def copyfile(src, dst, text):
    shutil.copy(src, dst)
    print(text)
