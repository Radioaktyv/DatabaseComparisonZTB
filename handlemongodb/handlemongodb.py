from cred import mongodbpass
from pymongo import MongoClient
from models.review import Review
import string
from random import randint, choice


def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str


def getnewReview():
    review = Review(get_random_string(10), get_random_string(14), get_random_string(5), randint(0,5), randint(0,5), randint(0,5), randint(1000000000,2000000000),
                    get_random_string(15),
                    get_random_string(1000))
    return review.__dict__


def connectToMongo():
    client = MongoClient(mongodbpass)
    db = client["DatabaseComparisonZTB"]
    collection = db["Reviews"]
    print("Successful connection")
    return collection


def deleteRecords(collection, iteration):
    for i in range(iteration):
        collection.delete_one({"Id": None})
    print("Delete successful \namount or records:", iteration)


def readRecords(collection, iteration):
    for i in range(iteration):
        id = randint(1, 500000)
        document = collection.find({"Id": id})
    print("Read successful \namount or records:", iteration)


def createRecords(collection, iteration):
    for i in range(iteration):
        document = getnewReview()
        collection.insert_one(document)
    print("Successful create \namount or records:", iteration)


def updateRecords(collection, iteration):
    for i in range(iteration):
        id = randint(1, 500000)
        score = randint(0, 5)
        collection.update_one({"Id": id}, {"$set": {"Score": score}})
    print("Successful Update \namount or records:", iteration)

