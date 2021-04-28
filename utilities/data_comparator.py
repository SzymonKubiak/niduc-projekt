import numpy as np


class DataComparator:
    def compare_data_vectors(self, original_data, recieved_data, data_block_size):
        data_packets = len(original_data) // data_block_size
        error_packets = 0
        for i in range(0,data_packets):
            error_found = False
            for j in range(0,data_block_size):
                if(original_data[i*data_block_size+j]!=recieved_data[i*data_block_size+j]):
                    error_found=True
            if(error_found==True):
                error_packets = error_packets + 1

        print("Total data packets sent: ", data_packets)
        print("Correctly transmitted packets: ", data_packets - error_packets)
        print("Not correctly transmitted packets: ", error_packets)
        return