import matplotlib.pyplot as plt
import csv

error_packets = []

# Get a list of all uncorrectly sent packets from CSV:
with open('../data_constant_noise.csv') as input_csv:
    data = csv.reader(input_csv, delimiter=',')
    error_packets = [int(row[1]) for row in data]

fig = plt.figure(figsize=(10, 7))

# Creating plot
plt.boxplot(error_packets)

plt.title("Wykres pudełkowy błędnie przesłanych pakietów")


# show plot
plt.show()
