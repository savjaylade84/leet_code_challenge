

''' 
        sorted sum problem in hackerrank

        problem:

        f(n) = 1*s + 2*s +3*s...n*s
        f(1) + f(2) + f(3) ... f(n)

'''


def sorted_sum(arr) -> int:
    temp:list[int] = []
    temp_list:[list[int]] = []
    index:int = 0
    total:int = 0
    f_num:int = 0


    arr.sort()
    arr.reverse()

    ''' 
        create like this
        [4]
        [3,4]
        [2,3,4]
        [1,2,3,4]
        final look
        [[4],[3,4],[2,3,4],[1,2,3,4]]
    '''
    while index < len(arr):
        index_:int = 0
        while index_ <= index:
            temp.append(arr[index_])
            index_ = index_ + 1
        temp.sort()
        print(temp)
        temp_list.append(temp)
        temp = []
        index = index + 1
    print(temp_list)

    ''' 
        loop every list in list then
        loop again for each item
        then multiply  value to its
        index + 1. add all the results in
        each list.look like this

        [1*4] = 4
        [1*3,2*4] = 11
        [1*2,2*3,3*4] = 20
        [1*1,2*2,3*3,4*4] = 30
        [[1*4],[1*3,2*4],[1*2,2*3,3*4],[1*1,2*2,3*3,4*4]] = 
        [4,11,20,30]
    '''
    temp = []
    for row in temp_list:
        index = 0
        total = 0
        for num in row:
            print('->',(index * num))
            total = total + ((index + 1) * num)
            index = index + 1
        temp.append(total)
        print(temp)

    ''' 
        sum all the items
        [4,11,20,30] = 65
    '''
    total = 0
    for num in temp:
        total = total + num
        
    return total

def main() -> None:
    test:list[int] = [9,5,8]

    print('Result:',sorted_sum(test))


if __name__ == '__main__':
    main()
