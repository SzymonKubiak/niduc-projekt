from codes.hammming_code import HammingCode
from codes.repetition_code import RepetitionCode
from utilities.data_generator import DataGenerator

hamming_code = HammingCode()
repetitition_code = RepetitionCode(3)
data_generator = DataGenerator()

data = data_generator.generate_data_vector(hamming_code.data_block_size, 5)
print("Original data: ", data)

encoded_data_hamming = hamming_code.encode(data)
print("Encoded with Hamming code: ", encoded_data_hamming)

encoded_data_repetition = repetitition_code.encode(data)
print("Encoded with Repetition code: ", encoded_data_repetition)

decoded_data_repetition = repetitition_code.decode(encoded_data_repetition)
print("Decoded with Repetition code: ", decoded_data_repetition)
