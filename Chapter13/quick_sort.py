class QuickSort:
  def __init__(self, array) -> None:
    self.array = array
    self.count = 0

  def partition(self, left, right) -> int:
    self.count += 1
    pivot = right
    right = right-1

    while True:

      while self.array[left] < self.array[pivot]:
        left += 1
      
      while self.array[right] > self.array[pivot]:
        right -= 1

      if left >= right:
        break
      
      else:
        self.array[left], self.array[right] = self.array[right], self.array[left]

        # Once you've swapped left and right pointers, we move the left pointer by 1. Since the value is already found to be less than the the pivot.
        # Thus stopping the right pointer.
        left += 1

    self.array[left], self.array[pivot] = self.array[pivot], self.array[left]
    return left

  def _do_quick_sort(self, left, right):
    self.count += 1
    if right - left <= 0:
      return
    
    pivot = self.partition(left, right)

    # Parition and sort left side of the pivot
    self._do_quick_sort(left, pivot-1)

    # Parition and sort right side of the pivot
    self._do_quick_sort(pivot+1, right)
  

  def quick_sort(self):
    self._do_quick_sort(0, len(self.array)-1)
    return self.array

  def _quick_select(self, k, left, right):
    self.count += 1
    if right - left <= 0:
      return self.array[left]

    pivot = self.partition(left, right)

    if k < pivot:
      return self._quick_select(k, left, pivot-1)
    
    elif k > pivot:
      return self._quick_select(k, pivot+1, right)
    
    else:
      return self.array[pivot]

  def quickselect(self, kth_element):
    return self._quick_select(kth_element, 0, len(self.array)-1)



if __name__ == '__main__':
  # arr = [0,5,2,1,6,3]
  # print(f"Array before sorting: {arr}")
  # qs = QuickSort(arr)
  # print(f"Array after quick sort: {qs.quick_sort()}")
  # print("\n")
  # print(f"Total steps taken for an array of size {len(arr)} is {qs.count}")

  qselect = [0, 50, 20, 10, 60, 30]
  qsec = QuickSort(qselect)
  ith_val = 2
  print(f"Quick Select, {ith_val+1}nd value: {qsec.quickselect(ith_val)}")
  print(f"Total steps taken for an array of size {len(qselect)} is {qsec.count}")