def convert_int_to_roman (integer:int):

    conversion = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

    result = ""

    for num, roman in conversion.items():
      while integer >= num:
        integer = integer - num
        result = roman + result
    return result
        
if __name__=="__main__":
    integer = 585
    romain_number = convert_int_to_roman(integer)
    print(romain_number)
    
    
    