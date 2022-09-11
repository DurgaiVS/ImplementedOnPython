def insertionSort(arr):
  
  outputArr = []

  for [key, value] in enumerate(arr):

    if key == 0: 
      outputArr.append(value)
      continue

    for i in range(key, 0, -1):

      if value >= outputArr[i-1]:
        outputArr.insert(i, value)
        break

      elif i-1 == 0:
        outputArr.insert(0, value)
        break

  return outputArr




if __name__ == "__main__":

  stringInput = input("Enter the numbers to be sorted with comma seperated\nEG: 2,3,4,...\n")

  try:
    stringArray = stringInput.split(",")
    integerArray = list(map(int, stringArray))

  except:
    print("Enter the input in specified format...")
  
  else:
    output = insertionSort(integerArray)
    print(output)


  