#Find the position of a number in a string


def binary_search(item, lst):
    low = 0;
    high = len(lst) -1
    
    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        
        if guess == item:
            return mid
        
        if guess > item:
            high = mid + 1
        else:
            low = mid - 1
    return None



def main():
    my_list = [1,3,6,7,12,15]

    print(binary_search(3, my_list))

if __name__ == "__main__":
    main()