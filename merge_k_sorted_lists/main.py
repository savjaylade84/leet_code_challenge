

def merge_k_sorted_lists(numbers:list[list[int]]) -> list[int]:
    temp:list[int] = []
    for rows in numbers:
        temp.extend([column for column in rows])
    temp.sort()
    return temp

    
def main() ->None:

    grid:list[list[int]] = [
        [1,3,4],
        [1,2,4],
        [2,3],
    ]

    print(merge_k_sorted_lists(grid))


if __name__ == '__main__':
    main()

