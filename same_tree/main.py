

def same_tree(arr1:list,arr2:list) -> bool:
    for ia,ib in zip(arr1,arr2):
        if ia != ib:
            return False

    return True

def main() -> None:
    arra,arrb = [1,2,3],[1,2,3]
    print(same_tree(arra,arrb))
    
    arra,arrb = [1,2],[1,None,3]
    print(same_tree(arra,arrb))
    
    arra,arrb = [1,2,1],[1,1,3]
    print(same_tree(arra,arrb))

if __name__ == '__main__':
    main()
