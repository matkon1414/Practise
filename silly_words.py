def sillycase(string):
    halfing = len(string) // 2
    first_half = string[:halfing]
    second_half = string[halfing:]
    string = first_half.lower() + second_half.upper()
    return string