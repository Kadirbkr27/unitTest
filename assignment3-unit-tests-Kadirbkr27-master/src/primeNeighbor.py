'''
Created by Neda Topuz
Modified by Abdulkadir Bakır
'''

def findPrimeNumber(upperBound):
    if upperBound < 2:
        return False
    for i in range(2, int(upperBound**0.5) + 1):
        if upperBound % i == 0:
            return False
    return True

def primeNeighbor(val):
    if val < 1000:
        for pri in range(int(val), 1, -1):
            if findPrimeNumber(pri):
                print(pri)
                return pri
        return 0 
    else: return 0