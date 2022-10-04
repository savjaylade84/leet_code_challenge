

def thousand(num:int)-> str:

    if(num < 4 and num > 0):
        if(num == 3):
            return 'MMM'
        elif(num == 2):
            return 'MM'
        elif(num == 1):
            return 'M'
    
    return ''

def hundred(num:int)-> str:

    if(num < 10 and num > 0):
        if(num == 9):
            return 'CM'
        if(num == 8):
            return 'DCCC'
        if(num == 7):
            return 'DCC'
        if(num == 6):
            return 'DC'
        if(num == 5):
            return 'D'
        if(num == 4):
            return 'CD'
        if(num == 3):
            return 'CCC'
        if(num == 2):
            return 'CC'
        if(num == 1):
            return 'C'
    return ""


def ten(num:int)-> str:

     if(num < 10 and num > 0):
         if(num == 9):
             return 'XC'
         if(num == 8):
             return 'LXXX'
         if(num == 7):
             return 'LXX'
         if(num == 6):
             return 'LX'
         if(num == 5):
             return 'L'
         if(num == 4):
             return 'XL'
         if(num == 3):
             return 'XXX'
         if(num == 2):
             return 'XX'
         if(num == 1):
             return 'X'
     return ""


def one(num:int)-> str:

     if(num < 10 and num > 0):
         if(num == 9):
             return 'IX'
         if(num == 8):
             return 'VIII'
         if(num == 7):
             return 'VII'
         if(num == 6):
             return 'VI'
         if(num == 5):
             return 'V'
         if(num == 4):
             return 'IV'
         if(num == 3):
             return 'III'
         if(num == 2):
             return 'II'
         if(num == 1):
             return 'I'
     return ""

def integer_to_roman(__number:int = 0) -> str:

    temp:list = [int(num) for num in str(__number)]

    answer:str = ''

    if(len(temp) == 4):
        answer = answer +  thousand(temp[0]) + hundred(temp[1]) + ten(temp[2]) + one(temp[3])

    if(len(temp) == 3):
        answer = answer + hundred(temp[0]) + ten(temp[1]) + one(temp[2])

    if(len(temp) == 2):
        answer = answer +   ten(temp[0]) + one(temp[1])

    if(len(temp) == 1):
        answer = answer +   one(temp[0])

    return answer



def main() -> None:

    while True:
        __input = int(input('[ Enter Number ]: '))
        __roman = integer_to_roman(__input)
        print(f'[ Roman Numeral  ]: {__roman}')

        answer = input('[ Do You To Exit (Y) yes / (N) no]: ')
        if(answer == 'Y' or answer == 'y'):
            break
    
    pass



if __name__ == '__main__':
    main()
