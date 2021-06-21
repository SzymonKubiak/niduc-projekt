import csv
import matplotlib.pyplot as plt

error_packets = []

# Get a list of all uncorrectly sent packets from CSV:
with open('data_constant_noise.csv') as input_csv:
    data = csv.reader(input_csv, delimiter=',')
    error_packets = [int(row[1]) for row in data]

fig, ax1 = plt.subplots()

ax1.hist(error_packets, bins='auto')
ax1.set_xlabel("Liczba błędnie zdekodowanych pakietów")
ax1.set_ylabel("Liczba wystąpień w próbie")

plt.show()
