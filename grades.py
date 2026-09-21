import csv

columns = ["Test1", "Test2", "Test3", "Test4", "Final"]

def read_table(path = "grades.csv"):
    with open(path, encode = "utf-8", newline = "") as f:
        return list(csv.DictReader(f, skipoptionalspace=True))
    