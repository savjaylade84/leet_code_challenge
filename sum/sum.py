

def sum(numbers:list[int],target:int=0) -> list[int]:
    return list((numbers.index(left),numbers.index(right)) for left in numbers for right in numbers if (left + right) == target and  (left != right))


def main() ->None:
    num = [1,2,3,4,5,6]
    target = 9

    print(sum(num,target))


if __name__ == '__main__':
    main()
