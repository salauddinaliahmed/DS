def threesum(arr):
    arr.sort()
    sorted_arr = arr

    output = []
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        l = i+1
        r = len(arr)-1

        while l < r:
            currentsum = arr[i] + arr[l] + arr[r]

            if currentsum == 0:
                output.append([arr[i], arr[l], arr[r]])
            
                # Because its a sorted list.
                while l < r and arr[l] == arr[l+1]:
                    l += 1
                while l < r and arr[r] == arr[r-1]:
                    r -= 1

                l += 1
                r -= 1

            elif currentsum < 0:
                l += 1
            
            else:
                r -= 1

    return output


def new_same_sum(nums, k):
    # h = {}
    # for i, j in enumerate(nums):
    #     if j in h:
    #         h[j].append(i)
    #     else:
    #         h[j] = [i]
        
    # # indexes of 2+ nos.
    # result = False
    # for v in h.values():
    #     if len(v) > 1:
    #         t = 0
    #         while t < len(v)-1:
    #             if abs(v[t]-v[t+1]) <= k:
    #                 return True
    #             t += 1
                
    # return False
    h = {}
    for i, j in enumerate(nums):
        if j in h and abs(i-h[j]) <= k:
            return True
        h[j] = i
    return False

# Taken from leetcode for debugging.
def addTwoNumbers(l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        s = ''
        curr = self
        while curr:
            s += f'->{curr.val}'
            curr = curr.next
        return s

if __name__ == '__main__':
    # print(threesum([-1, 0, 1, 2, -1, 4]))
    l1 = ListNode(9, next=ListNode(9, next=ListNode(9)))
    l2 = ListNode(1, next=ListNode(0, next=ListNode(0)))

    print(addTwoNumbers(l1,l2))