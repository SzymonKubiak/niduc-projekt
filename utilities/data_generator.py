import numpy as np


class DataGenerator:
    def generate_data_vector(self, data_block_size, min_length):
        generated_length = min_length + \
            data_block_size - (min_length % data_block_size)
        return list(self._generate_bits(generated_length))

    def _generate_bits(self, number):
        return np.random.randint(0, 2, number)
