import csv


def getCSVData(fileName):
    # create an empty list to store rows
    rows = []
    # open the csv file
    datafile = open(fileName, "r")

    # create s csv reader from csv file
    reader = csv.reader("dataFile")

    # skip the header
    next(reader)

    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
