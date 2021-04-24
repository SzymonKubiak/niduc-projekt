import numpy as np
    
class HammingCode:
    def __init__(self):
        self.dataBlockSize = 4 
        self.generationMatrix = np.array([[1,1,0,1],[1,0,1,1],[1,0,0,0],[0,1,1,1],[0,1,0,0,],[0,0,1,0],[0,0,0,1]])
        self.errorSyndromeMatrix=[[0,0,0,1,1,1,1],[0,1,1,0,0,1,1],[1,0,1,0,1,0,1]]
        
    def generateCodes2(self,dataVector):
        dataVector = np.matrix(dataVector).transpose()
        return np.dot(self.generationMatrix,dataVector) %2
        
    def generateCodes(self,dataVector):
        codeVectorsAmount = len(dataVector)  // self.dataBlockSize
        codedVector = []
        for i in range(0, codeVectorsAmount):
            readyCode = []
            utilities = Utilities()
            readyCode.append(utilities.xor([dataVector[4*i],dataVector[4*i+1],dataVector[4*i+3]]))
            readyCode.append(utilities.xor([dataVector[4*i],dataVector[4*i+2],dataVector[4*i+3]]))
            readyCode.append(dataVector[4*i])
            readyCode.append(utilities.xor([dataVector[4*i+1],dataVector[4*i+2],dataVector[4*i+3]]))
            readyCode.append(dataVector[4*i+1])
            readyCode.append(dataVector[4*i+2])
            readyCode.append(dataVector[4*i+3])
            codedVector = codedVector + readyCode
        return codedVector