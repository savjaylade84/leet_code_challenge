
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
    _min,_max = (1,9)
    index = 1 
    while True:

         arr = [
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)],
             [random.randint(_min,_max) for _ in range(_min,_max)]
         ]
         print(f'————————————————————————————————————')
         print(f'total generated suduko: {index}')
         for item in arr:
             print(item)
         print(f'valid suduko? {validate_suduko(arr)}')
         print('————————————————————————————————————')
         index += 1
         if validate_suduko(arr):
             break
    

if __name__ == '__main__':
    main()
