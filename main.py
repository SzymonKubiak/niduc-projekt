from utilities.csv_write import * 
from codes.cyclic_code import CyclicCode
from codes.hamming_code import HammingCode
from codes.repetition_code import RepetitionCode
from utilities.bsc_channel import BinarySymmetricChannel
from utilities.data_generator import DataGenerator
from utilities.data_comparator import DataComparator



hamming_code = HammingCode()
cyclic_code = CyclicCode(4, [1, 0, 1, 1], 0)
repetition_code = RepetitionCode(1,4)
data_generator = DataGenerator()
data_comparator = DataComparator()

#####################################################
# Output CSV file will include such values as:      #
# Number of sent packages                           #
# Number of uncorrectly sent packages               #
# Noise percentage in BSC                           #
#####################################################




def test_code(code_object, number_of_bits, noise_generator, data_generator, data_comparator):

    # raw data vector generation
    data = data_generator.generate_data_vector(code_object.data_block_size, number_of_bits)

    # encoding raw data
    encoded_data = code_object.encode(data)

    # put through noisy channel
    recieved_data = noise_generator.transmit_data(encoded_data)

    # decode recieved data
    decoded_data = code_object.decode(recieved_data)

    # function returns total number of sent packages, and number of unsuccesfully sent packages
    return data_comparator.statistics(data, decoded_data, code_object.data_block_size)







noise_promiles_range = 500
number_of_repetitions = 50
number_of_data_bits = 399


## function uses promiles, because iterating over float is impossible
## Here is tested coding with variable noise channel

#####################################################
# Output CSV file will include such values as:      #
# Noise percentage in BSC                           #
# Number of sent packages                           #
# Number of uncorrectly sent packages               #
#####################################################

csv_array_for_variable_noise = []
for noise_promiles in range (noise_promiles_range):
    bsc_channel = BinarySymmetricChannel(noise_promiles / 1000)
    for repetition in range (number_of_repetitions):
        stats = test_code(repetition_code, number_of_data_bits, bsc_channel,data_generator, data_comparator)
        total_sent_packages = stats[0]
        uncorrectly_sent_packages = stats[1]
        csv_array_for_variable_noise.append([noise_promiles, total_sent_packages, uncorrectly_sent_packages])

write_array_to_csv(csv_array_for_variable_noise, "data_variable_noise_repetition1")

# csv_array_for_variable_noise = []
# for noise_promiles in range (noise_promiles_range):
#     bsc_channel = BinarySymmetricChannel(noise_promiles / 1000)
#     for repetition in range (number_of_repetitions):
#         stats = test_code(cyclic_code, number_of_data_bits, bsc_channel, data_generator, data_comparator)
#         total_sent_packages = stats[0]
#         uncorrectly_sent_packages = stats[1]
#         csv_array_for_variable_noise.append([noise_promiles, total_sent_packages, uncorrectly_sent_packages])

# write_array_to_csv(csv_array_for_variable_noise, "data_variable_noise_cyclic")


## second testing - Here we are testing codes with constant noise 

#####################################################
# Output CSV file will include such values as:      #
# Number of sent packages                           #
# Number of uncorrectly sent packages               #
#####################################################

# number_of_repetitions = 1000
# csv_array_for_constant_noise = []
# bsc_channel = BinarySymmetricChannel(0.1)
# for repetition in range (number_of_repetitions):
#     stats = test_code(hamming_code, number_of_data_bits, bsc_channel,data_generator, data_comparator)
#     total_sent_packages = stats[0]
#     uncorrectly_sent_packages = stats[1]
#     csv_array_for_constant_noise.append([ total_sent_packages, uncorrectly_sent_packages])

# write_array_to_csv(csv_array_for_constant_noise, "data_constant_noise")

