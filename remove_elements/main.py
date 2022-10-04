
def remove_element(value:int,numbers:list[int]) -> list[int]:

    return list(number for number in numbers if number != value)

def main() ->None:

    print(remove_element(2,[1,1,1,2,2,2,3,3,3,4,4,5]))


if __name__ == '__main__':
    main()
