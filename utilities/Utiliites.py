import numpy as np

class Utilities:
    def generateDataVector(self,dataBlockSize,minLength):
        generatedLength = minLength + dataBlockSize - (minLength % dataBlockSize)
        return self.generateBits(generatedLength)
    
    def generateBits(self, number):
        return  np.random.randint(0,2,number)

    def xor(self,array):
        x = 0
        for i in array:
            if i == 1:
                x = x+1
        return x % 2
