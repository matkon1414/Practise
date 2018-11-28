#skrypt sprawdza czy string jest palindromem

def checkPalindrome(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False