import numpy as np
import csv


# Returns five most important sample percentiles
def five_num_summary(data):
    return np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')


error_packets = []

# Get a list of all uncorrectly sent packets from CSV:
with open('../data_constant_noise.csv') as input_csv:
    data = csv.reader(input_csv, delimiter=',')
    error_packets = [int(row[1]) for row in data]


# Get five number summary for the uncorrectly sent packets:
five_percentiles = five_num_summary(error_packets)

print(five_percentiles)

# Save the data to CSV:
with open('five_number_summary.csv', 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(five_percentiles)
