# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
    
# solution = Solution()
# print(solution.hasDuplicate([1,2,3,1]))  

class SolutionTwo:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


solutionTwo = SolutionTwo()
print(solutionTwo.hasDuplicate([1,2,3,4]))
