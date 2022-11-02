def add_binary(numl:str,numr:str) -> str:
    templ:int = int(numl)
    tempr:int = int(numr)
    
    result = bin(templ + tempr)
    return str(result)


def main() -> None:
    test_a,test_b = ('11','1')
    print(add_binary(test_a,test_b))
    test_a,test_b = ('1010','1011')
    print(add_binary(test_a,test_b))

if __name__ == '__main__':
    main()
