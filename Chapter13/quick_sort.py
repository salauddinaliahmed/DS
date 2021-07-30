"""
Quick Sort:
- Uses a concept called partitioning, which is to take a random value in the array (called the pivot), then we make sure 
  that every number that is less than the pivot ends at the left side of the pivot and 
  every number at that is greater than the pivot is on the right side.

This uses a combination of recursion and looping.

"""
from math import pi
import random

def quicksort(arr):
  # Randomly select pivot (Pivot is an index).
  arr_size = len(arr)-1
  # pivot = random.randint(0, arr_size)
  pivot = 5
  print(f"The pivot is: {pivot} and it holds the value: {arr[pivot]}")

  left_pointer = 0
  right_pointer = arr_size-1

  result = pivot_compare(arr, pivot, left_pointer, right_pointer)
  return result


def pivot_compare(arr, pivot, left_pointer, right_pointer):
  arr_size = len(arr)-1

  while left_pointer <= arr_size:
  # Move to right unless you encounter a value greater than or equal to the pivot.
    if arr[pivot] <= arr[left_pointer] :
      break
    left_pointer += 1

  # Everything to the right of the pivot, should be greater than the pivot
  while right_pointer >= 0:
    if arr[right_pointer] < arr[pivot]:
      break
    right_pointer -= 1


  # Check if left pointer has gone beyond right pointer.
  if left_pointer >= right_pointer:
    # Swap the pivot
    arr[pivot], arr[left_pointer] = arr[left_pointer], arr[pivot]
    return arr

  else:
    arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
    return pivot_compare(arr, pivot, left_pointer, right_pointer)

if __name__ == '__main__':
  arr = [0, 5, 2, 1, 6, 3]
  print(f"Old array: {arr}")
  print(quicksort(arr))
