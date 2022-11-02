

def plus_one(arr:list) -> list:
    arr[len(arr) - 1] += 1
    return arr


def main() -> None:
    arr = [1,2,3]
    print(plus_one(arr))
    arr = [1,2,3,4]
    print(plus_one(arr))

if __name__ == '__main__':
    main()
