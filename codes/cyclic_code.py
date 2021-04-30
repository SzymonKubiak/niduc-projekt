class CyclicCode:

    def __init__(self, block_size, generator_polynomial, initial_filler):
        self.check_sum_len = len(generator_polynomial) - 1
        # Maximum packet length can be 2 ^ (check sum length) - check sum length - 1
        self.data_block_size = block_size
        # generator polynomial - with 4 bit data packet it can be 11 or 13 (in decimal)
        self.generator_polynomial = generator_polynomial
        self.initial_filler = initial_filler

        self.encoded_packet_size = block_size + self.check_sum_len

    def bitwise_xor(self, x, y):
        return int(x != y)

    # Calculates the checksum
    def get_remainder(self, data_vector):
        data_copy = data_vector.copy()
        while 1 in data_copy[:self.data_block_size]:
            cur_shift = data_copy.index(1)
            for i in range(len(self.generator_polynomial)):
                data_copy[cur_shift + i] = self.bitwise_xor(
                    self.generator_polynomial[i], data_copy[cur_shift + i])
        return data_copy[self.data_block_size:]

    def encode(self, data_vector):
        encoded_data = []
        # encode each data block separately
        for i in range(0, len(data_vector), self.data_block_size):
            encoded_block = self.encode_block(
                data_vector[i:i+self.data_block_size])
            encoded_data.extend(encoded_block)

        return encoded_data

    def decode(self, data_vector):
        decoded_data = []
        # decode each data block separately
        for i in range(0, len(data_vector), self.encoded_packet_size):
            decoded_block = self.decode_block(
                data_vector[i:i+self.encoded_packet_size])
            decoded_data.extend(decoded_block)

        return decoded_data

    def encode_block(self, data_vector):
        # Encoded data is firsty padded with "0" or "1"
        padding_length = len(self.generator_polynomial) - 1
        initial_padding = padding_length * [self.initial_filler]
        padded_data_vector = data_vector + initial_padding
        # The encoded data is original data appended with the remainder
        return data_vector + self.get_remainder(padded_data_vector)

    def decode_block(self, encoded_block):
        error_remainder = self.get_remainder(encoded_block)
        decoded_block = self.correct_errors(encoded_block, error_remainder)

        return decoded_block

    def correct_errors(self, encoded_block, error_remainder):
        error_list = self.get_error_list()

        if (error_remainder != [0] * self.check_sum_len):
            wrong_bit = encoded_block[error_list.index(error_remainder)]
            encoded_block[error_list.index(
                error_remainder)] = 0 if wrong_bit == 1 else 1

        return encoded_block[:self.data_block_size]

    # Builds error correction list for calcuating the position of a signle-bit error
    def get_error_list(self):
        error_list = []
        for i in range(self.encoded_packet_size):
            error_data = [0] * self.encoded_packet_size
            error_data[i] = 1
            error_remainder = self.get_remainder(error_data)
            error_list.append(error_remainder)

        return error_list
