# def quickSort(arr, start = None, end = None):
#   isChanged = False
#   if start == None and end == None:
#     start = 0
#     end = len(arr) - 1
#   length = len(arr[start:(end+1)])
#   i = start
#   pivot = arr[end]
#   j = end-2

#   # else:
#   #   length = len(arr[start:(end+1)])
#   #   i = start
#   #   pivot = arr[end]
#   #   j = end-1

#   # print(i, j, length, pivot)

#   while i <= j:
#     if arr[i] > pivot:
#       isChanged = True
#       print(arr[i], i, pivot)
#       while j >= i:
#         if arr[j] < pivot:
#           print(arr[j],j)
#           arr[i], arr[j] = arr[j], arr[i]
#           break
#         j-=1
#       continue
#     i+=1

#   # print(arr)

#   if isChanged: arr[i], arr[length-1] = pivot, arr[i]

#   beforePivot = i-1
#   afterPivot = i+1
#   # endIndex = length-1

#   print(f'{arr=}, {beforePivot=}, {afterPivot=}, {i=}, {j=}, {start=}, {end=}')

#   if beforePivot > start: quickSort(arr, start, beforePivot)
  # if end > afterPivot: quickSort(arr, afterPivot, end)

from math import floor

def quickSort(arr, start = None, end = None):
  if not start:
    start = 0
    end = arr.__len__() - 1
  i = start
  j = i
  subI = 0
  subJ = 0
  while subJ < end or subI < end:
    if not arr[subI] > arr[end]:
      subI += 1
      continue
    if not arr[subJ] < arr[end]:
      subJ += 1
      continue
    arr[subI], arr[subJ] = arr[subJ], arr[subI]
    subI += 1
    subJ += 1

  arr[end], arr[subI] = arr[subI], arr[end]

  print(f"{arr = }, {start = }, {end = }, {subI = }, {subJ = }")

  if start > subI - 1:
    quickSort(arr, start, subI - 1)
  if subI > end - 1:
    quickSort(arr, subI + 1, end)
  



if __name__ == "__main__":

  stringInput = input("Enter the numbers to be sorted with comma seperated\nEG: 2,3,4,...\n")

  try:
    stringArray = stringInput.split(",")
    integerArray = list(map(int, stringArray))

  except:
    print("Enter the input in specified format...")
  
  else:
    output = quickSort(integerArray)
    # print(output)