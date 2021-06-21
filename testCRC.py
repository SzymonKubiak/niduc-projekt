import csv
from codes.cyclic_code import CyclicCode
from utilities.bsc_channel import BinarySymmetricChannel
from utilities.data_generator import DataGenerator
from utilities.data_comparator import DataComparator

bsc_channel = BinarySymmetricChannel(0.1)
data_generator = DataGenerator()
data_comparator = DataComparator()
number_of_data_bits = 999
number_of_repetitions = 100


def test_code(code_object):
    # raw data vector generation
    data = data_generator.generate_data_vector(
        code_object.data_block_size, number_of_data_bits)

    # encoding raw data
    encoded_data = code_object.encode(data)

    # put through noisy channel
    recieved_data = bsc_channel.transmit_data(encoded_data)

    # decode recieved data
    decoded_data = code_object.decode(recieved_data)

    # function returns total number of sent packages, and number of unsuccesfully sent packages
    return data_comparator.statistics(data, decoded_data, code_object.data_block_size)


def write_array_to_csv(array, file_name):
    with open(f"crc_test_results/{file_name}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for row in array:
            writer.writerow(row)


def repeatTests(number_of_repetitions, code_object, file_name):

    csv_array = []

    for repetition in range(number_of_repetitions):
        stats = test_code(code_object)
        total_sent_packages = stats[0]
        uncorrectly_sent_packages = stats[1]
        csv_array.append(
            [total_sent_packages, uncorrectly_sent_packages])
    write_array_to_csv(csv_array, file_name)

# Testing codes with constant noise = 0.1

#####################################################
# Output CSV file:                                  #
# Number of sent packages                           #
# Number of uncorrectly sent packages               #
#####################################################


# Add leading 1 to every code:

# 0x5 = 101
cyclic_code = CyclicCode(4, [1, 0, 1, 1], 0)
repeatTests(number_of_repetitions, cyclic_code, "crc_test_4")

# 0x9 = 1001
cyclic_code = CyclicCode(11, [1, 0, 0, 1, 1], 0)
repeatTests(number_of_repetitions, cyclic_code, "crc_test_5")

# 0x12 = 10010
cyclic_code = CyclicCode(26, [1, 0, 0, 1, 0, 1], 0)
repeatTests(number_of_repetitions, cyclic_code, "crc_test_6")

# 0x21 = 100001
cyclic_code = CyclicCode(57, [1, 0, 0, 0, 0, 1, 1], 0)
repeatTests(number_of_repetitions, cyclic_code, "crc_test_7")

# 0x48 = 1001000
cyclic_code = CyclicCode(120, [1, 0, 0, 1, 0, 0, 0, 1], 0)
repeatTests(number_of_repetitions, cyclic_code, "crc_test_8")

# # 0xa6 = 10100110
cyclic_code = CyclicCode(247, [1, 0, 1, 0, 0, 1, 1, 0, 1], 0)
repeatTests(number_of_repetitions, cyclic_code, "crc_test_9")
