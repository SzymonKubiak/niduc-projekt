import matplotlib.pyplot as plt
import numpy as np
import csv


# Returns five most important sample percentiles
def five_num_summary(data):
    return np.percentile(data, [0, 25, 50, 75, 100], interpolation='midpoint')


def getCharts(file_name):

    error_packets = []
    # Get a list of all uncorrectly sent packets from CSV:
    with open(f"crc_test_results/{file_name}.csv") as input_csv:
        data = csv.reader(input_csv, delimiter=',')
        error_packets = [int(row[1]) for row in data]

    fig, ax1 = plt.subplots()

    # Creating plot
    ax1.boxplot(error_packets, vert=False)

    ax1.set_xlabel("Liczba błędnie zdekodowanych pakietów")
    # plt.show()
    plt.savefig(f"statistics/crc_stats/{file_name}_boxplot.png")

    fig, ax1 = plt.subplots()

    ax1.hist(error_packets, bins='auto')
    ax1.set_xlabel("Liczba błędnie zdekodowanych pakietów")
    ax1.set_ylabel("Liczba wystąpień w próbie")

    # plt.show()
    plt.savefig(f"statistics/crc_stats/{file_name}_hist.png")

    # Get five number summary for the uncorrectly sent packets:
    five_percentiles = five_num_summary(error_packets)

    # Save the data to CSV:
    with open(f"statistics/crc_stats/{file_name}_fns.csv", 'w', newline='') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(five_percentiles)


getCharts("crc_test_4")
getCharts("crc_test_5")
getCharts("crc_test_6")
getCharts("crc_test_7")
getCharts("crc_test_8")
getCharts("crc_test_9")
