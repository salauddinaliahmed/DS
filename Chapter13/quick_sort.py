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


def contains_duplicates(arr):
  for _ in range(len(arr)-1):
    if arr[_] == arr[_+1]:
      return True
  return False

# Question 1:
def question1_product(arr):
  *_, a, b, c = arr
  return a*b*c

# Question 2:
def question2_missing(arr):
  for _ in range(len(arr)-1):
    if arr[_+1] - arr[_] > 1:
      print(f'{(len(arr) * (len(arr)+1)) / 2 - sum(arr)}')
      return arr[_] + 1

  # Print
  

def q3_greatest_number(arr):
  def _first():
    """I am O(N^2)"""
    greatest_value = 0
    for i in arr:
      greatest_value = True
      for j in arr[1:]:
        if j>i:
          greatest_value = False
    
      if greatest_value:
        return i
    
  def _second():
    """I am O(NlogN)"""
    sorted_arr = QuickSort(arr)
    return sorted_arr.quick_sort()[-1]


  def _third():
    """I am O(N)"""
    previous_greatest = 0
    for _ in arr:
      if _ > previous_greatest:
        previous_greatest = _
    
    return previous_greatest

  return _first(), _second(), _third()


if __name__ == '__main__':
  # arr = [0,5,2,1,6,3]
  # print(f"Array before sorting: {arr}")
  # qs = QuickSort(arr)
  # print(f"Array after quick sort: {qs.quick_sort()}")
  # print("\n")
  # print(f"Total steps taken for an array of size {len(arr)} is {qs.count}")

  # qselect = [0, 50, 20, 10, 60, 30]
  # qsec = QuickSort(qselect)
  # ith_val = 2
  # print(f"Quick Select, {ith_val+1}nd value: {qsec.quickselect(ith_val)}")
  # print(f"Total steps taken for an array of size {len(qselect)} is {qsec.count}")
  arr2 = [5, 2, 4, 6, 1, 2, 2 ]
  arr2 = [0, 1, 2, 4, 5]
  qs = QuickSort(arr2)
  sorted_arr = qs.quick_sort()
  print(f"Contains duplicates: {contains_duplicates(sorted_arr)}")
  print(f"Answer to question 1 Chapter 13: {question1_product(sorted_arr)}")
  print(f"Answer to question 2 Chapter 13: {question2_missing(sorted_arr)}")

  print(f"Third question: {q3_greatest_number([1, 4, 6, 2, 3])}")
