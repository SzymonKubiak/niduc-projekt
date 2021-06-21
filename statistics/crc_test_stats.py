from os import error
import matplotlib.pyplot as plt
import numpy as np
import csv
from statistics import mean

# Returns five most important sample percentiles


def five_num_summary(data):
    return np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')


def getCharts(file_name, title):

    error_packets = []
    # Get a list of all uncorrectly sent packets from CSV:
    with open(f"crc_test_results/{file_name}.csv") as input_csv:
        data = csv.reader(input_csv, delimiter=',')
        error_packets = [int(row[1]) for row in data]

    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.set_title(title)

    # Creating plot
    ax1.hist(error_packets, bins='auto')
    ax1.set_ylabel("Liczba wystąpień w próbie")

    ax2.boxplot(error_packets, vert=False)
    ax2.set_xlabel("Liczba błędnie zdekodowanych pakietów")

    plt.savefig(f"statistics/crc_stats/{file_name}_chart.png")

    # Get five number summary for the uncorrectly sent packets:
    five_percentiles = five_num_summary(error_packets)

    # Save the data to CSV:
    with open(f"statistics/crc_stats/{file_name}_fns.csv", 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(five_percentiles)

    with open(f"statistics/crc_stats/{file_name}_avg.csv", 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow([np.average(error_packets)])


getCharts("crc_test_4", "4-bitowy dzielnik CRC")
getCharts("crc_test_5", "5-bitowy dzielnik CRC")
getCharts("crc_test_6", "6-bitowy dzielnik CRC")
getCharts("crc_test_7", "7-bitowy dzielnik CRC")
getCharts("crc_test_8", "8-bitowy dzielnik CRC")
getCharts("crc_test_9", "9-bitowy dzielnik CRC")
