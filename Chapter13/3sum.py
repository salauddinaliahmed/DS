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



if __name__ == '__main__':
    # print(threesum([-1, 0, 1, 2, -1, 4]))
    print(new_same_sum([1,2,3,1,2,3], 2))