import sqlite3
from ReallySimpleDB import manager

def connect():
    return sqlite3.connect("Reviews/database.sqlite")


def createCursor(con):
    return con.cursor()
