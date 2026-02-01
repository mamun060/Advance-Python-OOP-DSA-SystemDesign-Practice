class DuplicateChecker:
    def contains_duplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
duplicate_checker = DuplicateChecker()
print(duplicate_checker.contains_duplicate([1, 2, 3, 1]))