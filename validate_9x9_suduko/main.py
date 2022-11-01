

import random

def validate_suduko(arr:list[list]) -> bool:

    for x in arr:
        temp = list(set(item for item in x))
        if len(temp) < len(arr[0]):
            return False
    for y in range(0,len(arr[0])):
        temp = list()
        for z in range(0,len(arr[0])):
            temp.append(arr[z][y])
        temp = list(set(item for item in temp))
        if len(temp) < len(arr[0]):
            return False
            
    return True


    
def main() -> None:
    _min,_max = (0,9)
    x,y = (1,9)
    index = 1 
    while True:

         arr = [
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)],
             [random.randint(x,y) for _ in range(_min,_max)]
         ]
         
         answer:bool = validate_suduko(arr)
         print(f'\r{arr[0]}<|      \r\n{arr[1]} |\r\n{arr[2]} |\r\n{arr[3]} |\r\n{arr[4]} |\r\n{arr[5]} |\r\n{arr[6]} |\r\n{arr[7]} |\r\n{arr[8]}<|\r')
         print(f'\rtotal generated suduko: {index}  \r',end='')
         index += 1
         if answer:
             break
    

if __name__ == '__main__':
    main()
