

def fizzbuzz(n:int) -> list:

    temp:list = []

    for num in range(1,n):

        if num % 3 == 0 and num % 5 == 0:
            temp.append('fizzbuzz')
        elif num % 3 == 0:
            temp.append('fizz')
        elif num % 5 == 0:
            temp.append('buzz')
        else:
            temp.append(f'{num}')

    return temp

def main() -> None:
    print('[')
    for item in fizzbuzz(20):
        print(f"    '{item}'")
    print(']')

if __name__ == '__main__':
    main()
