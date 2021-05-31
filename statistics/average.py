import numpy as np
import csv


def read_from_csv(file_name):
    csv_array = []
    with open( file_name+ '.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_array.append(list(map(int, row)))
    return csv_array

def write_array_to_csv(array,file_name):
    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in array:
            writer.writerow(row)

# used for one-dimensional variable
# returns list = [average, std deviation]
def average_and_deviation(array, valuable_column_index):
    valuable_column_array = []
    for row in array:
        valuable_column_array.append(row[valuable_column_index])
    return [np.mean(valuable_column_array), np.std(valuable_column_array)]


# used for two-dimensional variable
# returns list of lists = [average, std deviation]
def multiple_average_and_deviation(array, valuable_column_index, interval):
    output_array = []
    for dataset in range(len(array)//interval):
        partial_stats = [dataset]
        partial_stats.extend(average_and_deviation(array[dataset*interval:dataset*interval+interval-1], valuable_column_index))
        output_array.append(partial_stats)
    return output_array


constant_noise = read_from_csv("data_constant_noise")
constant_noise_stats = []
constant_noise_stats.append(average_and_deviation(constant_noise, 1))
write_array_to_csv(constant_noise_stats,"constant_noise_stats")



variable_noise = read_from_csv("data_variable_noise")
variable_noise_stats = []
variable_noise_stats= multiple_average_and_deviation(variable_noise, 2, 50)
write_array_to_csv(variable_noise_stats,"variable_noise_stats")







