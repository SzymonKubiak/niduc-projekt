from codes.error_correcting_code import ErrorCorrectingCode


class RepetitionCode(ErrorCorrectingCode):

    def __init__(self, word_size, block_size):
        self.word_size = word_size
        self.data_block_size = block_size

    def encode(self, data_vector):
        encoded_data = []

        for bit in data_vector:
            encoded_data.extend([bit] * self.word_size)

        return encoded_data

    def decode(self, encoded_data):
        decoded_data = []
        data_iter = iter(encoded_data)

        for i in range(0, len(encoded_data), self.word_size):
            word = encoded_data[i:i + self.word_size]
            decoded_word = self._decode_word_by_majority(word)
            decoded_data.append(decoded_word)

        return decoded_data

    def _decode_word_by_majority(self, word):
        return 0 if word.count(0) > word.count(1) else 1
