import numpy as np
from codes.error_correcting_code import ErrorCorrectingCode
from codes.utilities.Utilities import Utilities


class HammingCode(ErrorCorrectingCode):
    def __init__(self):
        self.data_block_size = 4
        self.generation_matrix = np.array([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [
            0, 1, 1, 1], [0, 1, 0, 0, ], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.error_syndrome_matrix = [[0, 0, 0, 1, 1, 1, 1], [
            0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]]

    def encode2(self, data_vector):
        data_vector = np.matrix(data_vector).transpose()
        return np.dot(self.generation_matrix, data_vector) % 2

    def encode(self, data_vector):
        code_vectors_amount = len(data_vector) // self.data_block_size
        coded_vector = []
        for i in range(0, code_vectors_amount):
            ready_code = []
            utilities = Utilities()
            ready_code.append(utilities.xor(
                [data_vector[4*i], data_vector[4*i+1], data_vector[4*i+3]]))
            ready_code.append(utilities.xor(
                [data_vector[4*i], data_vector[4*i+2], data_vector[4*i+3]]))
            ready_code.append(data_vector[4*i])
            ready_code.append(utilities.xor(
                [data_vector[4*i+1], data_vector[4*i+2], data_vector[4*i+3]]))
            ready_code.append(data_vector[4*i+1])
            ready_code.append(data_vector[4*i+2])
            ready_code.append(data_vector[4*i+3])
            coded_vector = coded_vector + ready_code
        return coded_vector
