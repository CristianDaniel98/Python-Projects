if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = int(len(nums)-1)
    print(length)
    count = len(nums)
    check = 0
    c = -1

    for i in range(length):
        if nums[i] == nums[i+1]:
            nums.pop(nums[i])
            length = int(len(nums)-1)
            count -= 1

    print(nums)
