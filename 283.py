class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)

#Via this method, we require no shifting