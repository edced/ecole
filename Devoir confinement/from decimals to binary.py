# Python program to convert decimal to binary 

# Function to convert Decimal number 
# to Binary number 
def decimalToBinary(n): 
    return bin(n).replace("0b", "")
player = input

# Driver code 
if __name__ == '__main__': 
    print(decimalToBinary(1)) 
    print(decimalToBinary(18)) 
    print(decimalToBinary(7)) 


#source https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/