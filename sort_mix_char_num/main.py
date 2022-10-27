

def sort(arr:list) -> list:
    arr.sort(key=lambda x: x[3:])
    return arr


def main() -> None:
    arr = ['BBD256','KFT442','ACF621','SST120']

    print(sort(arr))


if __name__ == '__main__':
    main()
