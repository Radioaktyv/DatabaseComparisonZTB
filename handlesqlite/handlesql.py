import sqlite3
from models.review import Review
from random import choice, randint
import string


def connect(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    return cursor, conn


def get_random_string(length):
    letters = string.ascii_uppercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str


def getnewReview():
    review = Review(get_random_string(10), get_random_string(14), get_random_string(5), randint(0,5), randint(0,5), randint(0,5), randint(1000000000,2000000000),
                    get_random_string(15),
                    get_random_string(1000))
    return review


def createRecordSQL(cursor, iteration):
    # Insert data
    for i in range(iteration):
        newReview = getnewReview()
        values = (str(newReview.ProductId), str(newReview.UserId), str(newReview.ProfileName),
                  int(newReview.HelpfulnessNumerator), int(newReview.HelpfulnessDenominator), int(newReview.Score),
                  int(newReview.Time),
                  str(newReview.Summary), str(newReview.Text))
        cursor.execute(
            "INSERT INTO Reviews (ProductId, UserId, Profilename, HelpfulnessNumerator, HelpfulnessDenominator, Score, Time,Summary, Text) VALUES (?, ?, ?, ?, ?, ?, ?,?,?)",
            values)


def readRecordSQL(cursor, iteration):
    for i in range(iteration):
        rId = randint(0, 550000)
        cursor.execute("SELECT * FROM Reviews WHERE Id=?", (rId,))


def updateRecordSQL(cursor, iteration):
    for i in range(iteration):
        rId = randint(1, 550000)
        rStr = get_random_string(30)
        print("random ID:" + str(rId) + "\n")
        cursor.execute("UPDATE Reviews SET Text = ? WHERE Id = ?", (rStr, rId,))


def deleteRecordSQL(cursor, iteration):
    for i in range(iteration):
        rId = randint(1, 550000)
        print("random ID:" + str(rId) + "\n")
        cursor.execute("DELETE FROM Reviews WHERE Id = ?", (rId,))

def commitChanges(conn):
    conn.commit()

def closeConnection(conn):
    conn.close()
