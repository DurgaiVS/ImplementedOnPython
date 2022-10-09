def binary_search(arr: list = None, item: int = None, start: int = None, end: int = None):
    start = 0
    end = arr.__len__() - 1
    while True:
        if start - end == 0:
            return start if item == arr[start] else -1
        mid = (start + end + 1) // 2
        if item > arr[mid]:
            start = mid + 1
        elif item < arr[mid]:
            end = mid - 1
        elif item == arr[mid]:
            return mid


if __name__ == "__main__":

    stringInput = input(
        "Enter the sorted numbers array with comma seperated value\nEG: 2,3,4,...\n")
    eleToSearch = input("Enter the number to search: ")

    try:
        stringArray = stringInput.split(",")
        integerArray = list(map(int, stringArray))
        intEle = int(eleToSearch)

    except:
        print("Enter the input in specified format...")

    else:
        output = binary_search(integerArray, intEle)
        print(output)  # if output >= 0 else print("Specified element is not found")
