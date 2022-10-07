def linear_search(arr: list = None, item: int = None):
    for position, element in enumerate(arr):
        if element == item:
            return position
    return -1


if __name__ == "__main__":

    stringInput = input(
        "Enter the numbers array with comma seperated\nEG: 2,3,4,...\n")
    eleToSearch = input("Enter the number to search: ")

    try:
        stringArray = stringInput.split(",")
        integerArray = list(map(int, stringArray))
        intEle = int(eleToSearch)

    except:
        print("Enter the input in specified format...")

    else:
        output = linear_search(integerArray, intEle)
        print(output) if output >= 0 else print(
            "Specified element is not found")
