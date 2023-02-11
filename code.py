import csv
def readCSV():
    file = open(r'C:\Users\blitz\OneDrive\Desktop\projectss\tasks\lab1\source.csv' , 'r')
    file1 = open(r'C:\Users\blitz\OneDrive\Desktop\projectss\tasks\lab1\source2.csv' , 'w', newline="")
    csvreader = csv.reader(file)
    csvwriter = csv.writer(file1)
    csvwriter.writerow((["year","region","value"]))
    next(csvreader, None)
    for rows in csvreader:
        print((rows[0] + "-01-01", rows[1], rows[2]))
        csvwriter.writerow((rows[0] + "-01-01", rows[1], rows[2]))
    

readCSV()