class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_bak = nums1.copy()
        num1_ptr = 0
        num2_ptr = 0
        count = 0
        while num1_ptr<m and num2_ptr<n:
            if nums1_bak[num1_ptr] < nums2[num2_ptr]:
                nums1[count] = nums1_bak[num1_ptr]
                count += 1
                num1_ptr += 1
            else:
                nums1[count] = nums2[num2_ptr]
                count += 1
                num2_ptr += 1
        
        while (num1_ptr<m):
            nums1[count] = nums1_bak[num1_ptr]
            count += 1
            num1_ptr += 1
        
        while (num2_ptr<n):
            nums1[count] = nums2[num2_ptr]
            count += 1
            num2_ptr += 1
