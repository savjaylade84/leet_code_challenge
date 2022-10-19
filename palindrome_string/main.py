

def palindrome(p:str) -> bool:
    temp = [item for item in p]
    temp.reverse()
    result = ''
    for item in temp:
        result = result + item
    if result == p:
        return True
    return False


if __name__ == '__main__':
    p = input('Enter a word:')
    print(f'Is "{p}" a palindrome? {palindrome(p)}')
