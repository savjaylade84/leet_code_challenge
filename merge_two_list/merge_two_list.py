

def merge_two_list(left:list[int],right:list[int]) -> list[int]:
    temp:list[int] = []
    temp.extend(right)
    temp.extend(left)
    return list(number for number in set(number for number in temp))

def main() ->None:
    right = [1,2,3,4,5,6]
    left = [1,2,3,7,8,9]

    print(merge_two_list(left,right))

if __name__ == '__main__':
    main()
