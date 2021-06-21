import matplotlib.pyplot as plt
import csv

error_packets = []

# Get a list of all uncorrectly sent packets from CSV:
with open('data_constant_noise.csv') as input_csv:
    data = csv.reader(input_csv, delimiter=',')
    error_packets = [int(row[1]) for row in data]

fig, ax1 = plt.subplots()

# Creating plot
ax1.boxplot(error_packets, vert=False)

ax1.set_xlabel("Liczba błędnie zdekodowanych pakietów")


# show plot
plt.show()
