


def remove_duplicates(input):
    input.sort()

    input = [val for val in set(item for item in input)]

    return input


def main():
    num = [1,2,3,4,5,5,]
    print(remove_duplicates(num))


if __name__ == '__main__':
    main()
