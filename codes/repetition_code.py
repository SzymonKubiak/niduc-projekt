from codes.error_correcting_code import ErrorCorrectingCode


class RepetitionCode(ErrorCorrectingCode):

    def __init__(self, word_length):
        self.word_length = word_length
        super().__init__()

    def encode(self, data):
        encoded_data = []

        for bit in data:
            encoded_data.extend([bit] * self.word_length)

        return encoded_data

    def decode(self, encoded_data):
        decoded_data = []
        data_iter = iter(encoded_data)

        while True:
            try:
                word = []

                for _ in range(self.word_length):
                    word.append(next(data_iter))

                decoded_word = self._decode_word_by_majority(word)
                decoded_data.append(decoded_word)

            except StopIteration:
                break

        return decoded_data

    def _decode_word_by_majority(self, word):
        return 0 if word.count(0) > word.count(1) else 1
