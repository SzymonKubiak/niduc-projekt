import numpy as np


class Utilities:

    def xor(self, array):
        x = 0
        for i in array:
            if i == 1:
                x = x+1
        return x % 2
