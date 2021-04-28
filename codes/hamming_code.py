import numpy as np
from codes.error_correcting_code import ErrorCorrectingCode
from codes.utilities.Utilities import Utilities

#Regular Hamming code for example (7,4) can correct single error. But it cannot detect double or more errors, because the code distance is equal to 3
#Hamming code with parity bit can recognise the double errors

class HammingCode(ErrorCorrectingCode):
    def __init__(self):
        self.data_block_size = 4
        self.encoded_packet_size = 7
        self.generation_matrix = np.array([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [
            0, 1, 1, 1], [0, 1, 0, 0, ], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.error_syndrome_matrix = [[1,0,1,0,1,0,1], [0,1,1,0,0,1,1], [0,0,0,1,1,1,1]]

    def encode(self, data_vector):
        code_vectors_amount = len(data_vector) // self.data_block_size
        coded_vector = []
        for i in range(0, code_vectors_amount):
            data_packet = data_vector[self.data_block_size*i:self.data_block_size*(i+1)]
            data_packet = np.matrix(data_packet).transpose()
            coded_packet = np.dot(self.generation_matrix, data_packet) % 2
            coded_packet = coded_packet.transpose()
            coded_packet = np.asarray(coded_packet)[0]
            coded_vector = coded_vector + coded_packet.tolist()
        return coded_vector


    def check_error_position(self, encoded_packet):
        encoded_packet = np.matrix(encoded_packet).transpose()
        error_position_matrix = np.dot(self.error_syndrome_matrix, encoded_packet) % 2
        error_position_matrix = np.asarray(error_position_matrix).transpose()
        error_position_array = error_position_matrix[0]
        error_position = 0
        for i in range(0,3):
            error_position = error_position + error_position_array[i]*pow(2, i)
                
        return error_position

    def correct_single_errors(self, encoded_data_vector):
            code_vectors_amount = len(encoded_data_vector) // self.encoded_packet_size
            corrected_vector = []
            for i in range(0, code_vectors_amount):
                encoded_packet = encoded_data_vector[self.encoded_packet_size*i:self.encoded_packet_size*(i+1)]
                error_position = self.check_error_position(encoded_packet)
                if (error_position != 0):
                    encoded_packet[error_position-1] = (encoded_packet[error_position-1]+1)%2
                corrected_vector = corrected_vector + encoded_packet
            return corrected_vector
    
    def decode(self, encoded_data_vector):
        corrected_vector = self.correct_single_errors(encoded_data_vector)
        corrected_code_vectors_amount = len(corrected_vector) // self.encoded_packet_size
        decoded_vector = []
        for i in range(0,corrected_code_vectors_amount):
            packet_data = [corrected_vector[7*i+2],corrected_vector[7*i+4],corrected_vector[7*i+5],corrected_vector[7*i+6]]
            decoded_vector = decoded_vector + packet_data
        return decoded_vector