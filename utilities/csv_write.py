import csv

def write_array_to_csv(array,file_name):
    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in array:
            writer.writerow(row)

