from codes.cyclic_code import CyclicCode
from codes.hamming_code import HammingCode
from codes.repetition_code import RepetitionCode
from utilities.data_generator import DataGenerator
from utilities.data_comparator import DataComparator

cyclic_code = CyclicCode(4, [1, 0, 1, 1], 0)
hamming_code = HammingCode()
repetitition_code = RepetitionCode(3)
data_generator = DataGenerator()
data_comparator = DataComparator()

data = data_generator.generate_data_vector(hamming_code.data_block_size, 4)
print("Original data: ", data)

encoded_data_hamming = hamming_code.encode(data)
print("Encoded with Hamming code: ", encoded_data_hamming)

decoded_data_hamming = hamming_code.decode(encoded_data_hamming)
print("Decoded with Hamming code: ", decoded_data_hamming)

data_comparator.compare_data_vectors(data, decoded_data_hamming, hamming_code.data_block_size)

encoded_data_repetition = repetitition_code.encode(data)
print("Encoded with Repetition code: ", encoded_data_repetition)

decoded_data_repetition = repetitition_code.decode(encoded_data_repetition)
print("Decoded with Repetition code: ", decoded_data_repetition)

encoded_data_cyclic = cyclic_code.encode(data)
print("Encoded with Cyclic code: ", encoded_data_cyclic)

decoded_data_cyclic = cyclic_code.decode(encoded_data_cyclic)
print("Decoded with Cyclic code: ", decoded_data_cyclic)
