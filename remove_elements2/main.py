

def remove_elements(num:list[int],val) -> int:
    print(f'list:{num},target:{val}')
    num = [item for item in num if item != val]
    print(num)
    return len(f'result:{num}')

def main() -> None:
    num = [1,2,3,4,4,5,6]
    val = 4

    print(remove_elements(num,val))

if __name__ == '__main__':
    main()
