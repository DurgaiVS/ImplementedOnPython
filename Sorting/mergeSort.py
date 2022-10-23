def mergeSort(arr):
    length = len(arr)
    if length == 2:
        arr[0], arr[1] = (arr[1], arr[0]) if arr[1] < arr[0] else (
            arr[0], arr[1])

    elif length == 1:
        pass

    else:
        mid = length//2
        firstHalf = mergeSort(arr[:mid])
        secondHalf = mergeSort(arr[mid:])
        lenFir = len(firstHalf)
        lenSec = len(secondHalf)
        arr = []

        (i, j) = (0, 0)
        for _ in range(length):
            if firstHalf[0] <= secondHalf[0]:
                arr.append(firstHalf[0])
                firstHalf.remove(firstHalf[0])
                # i+=1
                if len(firstHalf) == 0:
                    arr = arr + secondHalf
                    break

            else:
                arr.append(secondHalf[0])
                secondHalf.remove(secondHalf[0])
                # 0+=1
                if len(secondHalf) == 0:
                    arr = arr + firstHalf
                    break

    return arr


if __name__ == "__main__":

    stringInput = input(
        "Enter the numbers to be sorted with comma seperated\nEG: 2,3,4,...\n")

    try:
        # stringArray = stringInput.split(",")
        # converting string input to an array of integer
        integerArray = list(map(int, stringInput.split(",")))

    except:
        print("Enter the input in specified format...")

    else:
        output = mergeSort(integerArray)
        print(output)
