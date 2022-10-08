

def palindrome(input:str) -> bool:
    temp = [char for char in input]
    temp2 = ''
    print(temp)

    if temp[0] == '-':
        return False

    temp.reverse()

    for char in temp:
        temp2 = temp2 + char
    print(temp2)

    if temp2 == input:
        return True

    return False


def main() -> None:
    num = input('Enter a Number: ')

    print(f'is palindrome: {palindrome(num)}')

if __name__ == '__main__':
    main()
