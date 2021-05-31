import csv 
def read_from_csv(filename):
    csv_array = []
    with open( filename+ '.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_array.append(list(map(int, row)))
    return csv_array