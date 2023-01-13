'''
Created on 29/04/2015
Author: Bruno
This code is a only exemple who to do a basic CRUD in Python 2.7 with MongoDB 2.6.
'''

from pymongo import *


class MongoDB_Python:
    def __init__(self):
        # Initialize the connection on the data base.
        self.conn = MongoClient('localhost', 27017)
        self.db = self.conn.TestDB  # Data Base name:  TestDB
        self.cursor = self.db.collection  # Collection name: collection

    def create(self, query={}):
        # Insert a new register.
        self.cursor.insert(query)

    def read(self, query={}):
        # Read all the register.
        for value in self.cursor.find(query):
            print(value)

    def update(self, query_1={}, query_2={}):
        # Change the first item on the list.
        self.cursor.update(query_1, query_2)

    def delete(self):
        # Delete all the elements on the list.
        for i in self.cursor.find():
            self.cursor.remove(i)


if __name__ == '__main__':
    mongo = MongoDB_Python()

    for x in range(3):
        reg = {'_id': x, 'x': x, 'list': ['first', 'second', 'third', 'fourth', 'fifth']}
        mongo.create(reg)

    print('Read before update.')
    mongo.read()

    mongo.update({'x': 0, 'list': 'first'}, {'$set': {'list.$': 'primeiro'}})

    # Add a new element on the list.
    mongo.update({'x': 1}, {"$addToSet": {'list': {'$each': ['fifth', 'sixth', 'seventh']}}})

    # Remove one element on the list.
    mongo.update({'x': 2}, {'$pull': {'list': 'fifth'}})

    print('Read after update.')
    mongo.read()

    mongo.delete()