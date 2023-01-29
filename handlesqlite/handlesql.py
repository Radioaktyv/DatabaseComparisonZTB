import sqlite3
from ReallySimpleDB import manager
from sqlalchemy import create_engine

# Connect to the SQLite database
engine = create_engine('sqlite:///database.sqlite')


def connect():
    return sqlite3.connect("Reviews/database.sqlite")


def createCursor(con):
    return con.cursor()
