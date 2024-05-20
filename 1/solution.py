from leetCode.dataStructures.redBlackTree import RedBlackTree

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        rbt= RedBlackTree()
        for i in range(0,len(nums)):
            rbt.insert(nums[i], i)

        for i,val in enumerate(nums):
            node = rbt.root
            while node is not None:
                s = val + node.val
                if s == target and i != node.arg2:
                    return[i, node.arg2]
                elif s < target:
                    node = node.right
                else:
                    node = node.left

# Test Cases
s = Solution()
assert s.twoSum([2,7,11,15], 9) == [0,1]
assert s.twoSum([3,2,4], 6) == [1,2]
assert s.twoSum([3,3], 6) == [1,0]