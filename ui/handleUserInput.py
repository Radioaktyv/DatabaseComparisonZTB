from ui.UserInputs import UserInputs
from handlesqlite.handlesql import *
from handlemongodb.handlemongodb import *

def handleUserInput(userInput: UserInputs):
    iterations = userInput.records_amount
    selected_db = userInput.selected_database
    selected_crud_method = userInput.crud_method

    if selected_db == 'MongoDb':
        collection = connectToMongo()
        if selected_crud_method == "CREATE":
            createRecords(collection, iterations)
        elif selected_crud_method == "READ":
            readRecords(collection, iterations)
        elif selected_crud_method == "UPDATE":
            updateRecords(collection, iterations)
        else:
            deleteRecords(collection, iterations)
    else:
        cursor, conn = connect('./handlesqlite/database.sqlite')
        if selected_crud_method == "CREATE":
            createRecordSQL(cursor, iterations)
        elif selected_crud_method == "READ":
            readRecordSQL(cursor, iterations)
        elif selected_crud_method == "UPDATE":
            updateRecordSQL(cursor, iterations)
        else:
            deleteRecordSQL(cursor, iterations)
        commitChanges(conn)
        closeConnection(conn)

