class QuickSort:
  def __init__(self, array) -> None:
    self.array = array
    self.count = 0

  def partition(self, left, right) -> int:
    self.count += 1
    return 6

  def _do_quick_sort(self, left, right):
    self.count += 1
    # Wrong condition
    if right - left >= 0:
      return
    
    pivot = self.partition(left, right)

    # Parition and sort left side of the pivot
    self._do_quick_sort(left, pivot-1)

    # Parition and sort right side of the pivot
    self._do_quick_sort(pivot+1, right)
  

  def quick_sort(self):
    self._do_quick_sort(0, len(self.array)-1)
    return self.array


if __name__ == '__main__':
  arr = [0,5,2,1,6,3]
  print(f"Array before sorting: {arr}")
  qs = QuickSort(arr)
  print(f"Array after quick sort: {qs.quick_sort()}")
  print("\n")
  print(f"Total steps taken for an array of size {len(arr)} is {qs.count}")
