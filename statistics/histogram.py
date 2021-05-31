import csv
import matplotlib.pyplot as plt

error_packets = []

# Get a list of all uncorrectly sent packets from CSV:
with open('../data_constant_noise.csv') as input_csv:
    data = csv.reader(input_csv, delimiter=',')
    error_packets = [int(row[1]) for row in data]


plt.hist(error_packets, bins='auto')
plt.title("Histogram błędnie przesłanych pakietów")

plt.show()
