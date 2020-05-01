def binToDec(binNum):
    decNum = 0
    power = 0
    while binNum > 0:
        decNum += 2 ** power * (binNum % 10)
        binNum //= 10
        power += 1
    return decNum
print (str(binToDec(1110))) #change le nombre dans la parenthese
        