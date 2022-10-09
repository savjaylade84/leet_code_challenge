

def narcissitic_number(num):
    if num <= 9:
        return False

    temp = str(num)
    temp = [i for i in temp]
    #print(temp)
    #print(len(temp))
    temp = sum([int(i) ** len(temp) for i in temp])
    #print(temp)
    #print('#'*40)
    if temp == num:
        return True

    return False


def main():
    line_num = 1
    for i in range(0,1000000000):
        if narcissitic_number(i):
            print(f'{line_num}: {i} => {narcissitic_number(i)}')
            line_num = line_num + 1



if __name__ == '__main__':
    main()
