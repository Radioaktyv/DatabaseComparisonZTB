import pandas as pd
import matplotlib.pyplot as plt


def generate_arrays():
    mongo = pd.read_csv("../MongoDb.csv")
    mcreate = []
    mread = []
    mupdate = []
    mdelete = []
    sql = pd.read_csv("../SQLite.csv")
    screate = []
    sread = []
    supdate = []
    sdelete = []
    ABCD = ((0, 5, 10, 15), (1, 6, 11, 16), (2, 7, 12, 17), (3, 8, 13, 18), (4, 9, 14, 19))
    for a, b, c, d in ABCD:
        mcreate.append(mongo.values[a])
        mread.append(mongo.values[b])
        mupdate.append(mongo.values[c])
        mdelete.append(mongo.values[d])
        screate.append(sql.values[a])
        sread.append(sql.values[b])
        supdate.append(sql.values[c])
        sdelete.append(sql.values[d])
    # print(mcreate)
    return (mcreate, mread, mupdate, mdelete), (screate, sread, supdate, sdelete)


def generate_plot(mongo, sql):
    miter = []
    mtime = []
    siter = []
    stime = []
    for i in range(4):
        for j in range(5):
            miter.append(float(mongo[i][j][0]))
            mtime.append(float(mongo[i][j][1]))
            siter.append(float(sql[i][j][0]))
            stime.append(float(sql[i][j][1]))

        plt.plot(miter, mtime)
        # mongo
        plt.xlabel("Iterations")
        plt.ylabel("Time (s)")
        plt.xscale("log")
        plt.title("MongoDb " + str(mongo[i][j][2]))
        mname = "MongoDb" + str(mongo[i][j][2]) + ".png"
        plt.savefig(mname)
        plt.clf()
        # sql
        plt.plot(siter, stime)
        plt.xlabel("Iterations")
        plt.ylabel("Time (s)")
        plt.xscale("log")
        plt.title("SQLite " +str(sql[i][j][2]))
        mname = "SQLite" + str(sql[i][j][2]) + ".png"
        plt.savefig(mname)
        plt.clf()
        miter = []
        mtime = []
        siter = []
        stime = []


mongo, sql = generate_arrays()
generate_plot(mongo, sql)
