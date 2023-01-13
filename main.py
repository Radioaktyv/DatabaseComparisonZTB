import sqlite3
import shutil
from time import time


def copyfile(src, dst, text):
    shutil.copy(src, dst)
    print(text)


copyfile("Reviews/database.sqlite", "Backup/database.sqlite", "Backup created.")



copyfile("Backup/database.sqlite", "Reviews/database.sqlite", "Backup restored.")
