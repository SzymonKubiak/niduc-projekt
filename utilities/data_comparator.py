import numpy as np


class DataComparator:
    def compare_data_vectors(self, original_data, recieved_data, data_block_size, encoded_packet_size):
        data_packets = len(original_data) // data_block_size
        error_packets = 0
        for i in range(0, data_packets):
            error_found = False
            for j in range(0, data_block_size):
                if(original_data[i*data_block_size+j] != recieved_data[i*data_block_size+j]):
                    error_found = True
            if(error_found == True):
                error_packets = error_packets + 1

        error_bits = 0
        for i in range(0, len(recieved_data)):
            if original_data[i] != recieved_data[i]:
                error_bits = error_bits + 1
        print("----------STATISTICS----------")
        print(f'{"Total packages":20}{data_packets:10d}')
        print(f'{"Correct packages":20}{data_packets - error_packets:10d}')
        print(f'{"Error packages":20}{error_packets:10d}')
        print(f'{"Error package ratio":20}{round(error_packets*100/data_packets):9d}%')
        print(f'{"Total bits":20}{len(recieved_data):10d}')
        print(f'{"Correct bits":20}{len(recieved_data) - error_bits:10d}')
        print(f'{"Error bits":20}{error_bits:10d}')
        print(f'{"Error bit ratio":20}{round(error_bits*100/len(recieved_data)):9d}%')
        print(
            f'{"Code redundancy":20}{round(encoded_packet_size*100/data_block_size):9d}%')
        print("------------------------------")

        return

    def statistics(self, original_data, recieved_data, data_block_size):
        data_packets = len(original_data) // data_block_size

        error_packets = 0
        for i in range(0, data_packets):
            error_found = False
            for j in range(0, data_block_size):
                if(original_data[i*data_block_size+j] != recieved_data[i*data_block_size+j]):
                    error_found = True
            if(error_found == True):
                error_packets = error_packets + 1

        error_bits = 0
        for i in range(0, len(recieved_data)):
            if original_data[i] != recieved_data[i]:
                error_bits = error_bits + 1

        return [data_packets, error_packets]
