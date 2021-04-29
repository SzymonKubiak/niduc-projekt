import numpy as np


class BinarySymmetricChannel():
    def __init__(self, error_probability):
        # Probability of an error occurring for each sent bit
        self.error_probability = error_probability

    def transmit_data(self, data_vector):
        for i in range(len(data_vector)):
            bit = data_vector[i]
            if np.random.ranf() <= self.error_probability:
                data_vector[i] = 0 if bit == 1 else 1

        return data_vector
