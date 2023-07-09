# A function that takes a list and target parameter
# Multiple variables : middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list,element):
    middle = 0
    start = 0
    steps = 0
    end = len(list)
    while start < end:
        print("Steps",steps,":",str(list[start:end+1]))
        steps = steps + 1
        middle = (start + end ) // 2
        if list[middle] == element:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1
    
my_list = list(map(int,input().split()))
target = int(input())
binary_search(my_list,target)

        
