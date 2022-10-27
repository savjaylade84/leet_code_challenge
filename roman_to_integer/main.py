


def thousands(thousand:str) -> int:
    if thousand == 'M':
        return 1000
    return 0

def hundreds(hundred:str) -> int:
    if hundred == 'C':
        return 100
    if hundred == 'D':
        return 500
    return 0

def tens(ten:str)-> int:
    if ten == 'X':
        return 10
    if ten == 'L':
        return 50
    return 0

def ones(one:str)-> int:

    if one == 'I':
        return 1
    if one == 'V':
        return 5
    return 0


def roman_integer(roman:str) -> int:
    temp = [char for char in roman]
    
    _sum:int = 0
    prev:str = ''

    for item in temp:
        #print(f'{item} -> ',end='')
        if ones(item) > 0:
            if item == 'V' and prev  == 'I':
                _sum = _sum + 3
            else:
                _sum = _sum + ones(item)
           # print(f'{ones(item)} -> ',end='')

        if tens(item) > 0:
            if item == 'L' and prev  == 'C':
                _sum = _sum + 30
            elif item == 'X' and prev == 'I':
                _sum = _sum + 8
            else:
                _sum = _sum + tens(item)
           # print(f'{tens(item)} -> ',end='')

        if hundreds(item) > 0:
            if item == 'D' and prev  == 'C':
                _sum = _sum + 300
            elif item == 'C' and prev == 'X':
                _sum = _sum + 80
            else:
                _sum = _sum + hundreds(item)
           # print(f'{hundreds(item)} -> ',end='')

        if thousands(item) > 0:
            if item == 'M' and prev == 'C':
                _sum = _sum + 800
            else:
                _sum = _sum + thousands(item)
           # print(f'{thousands(item)} -> ',end='')
        #print(':'+f'{_sum}'+':'+prev + ':')
        prev = item
            
    return _sum

def main() -> None:


    arr = ['III','IV','IX','LVIII','MCMXCIV']

    for item in arr:
        print(f'{item} -> {roman_integer(item)}')



if __name__ == '__main__':
    main()


