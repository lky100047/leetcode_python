class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        array = arr.copy()
        ptr_array = 0
        ptr_arr = 0
        while(ptr_arr < len(array)):
            if array[ptr_array] == 0:
                arr[ptr_arr] = 0
                ptr_arr += 1
                if ptr_arr>= len(array):
                    break
                arr[ptr_arr] = 0
                ptr_arr += 1
                ptr_array += 1
            else:
                arr[ptr_arr] = array[ptr_array]
                ptr_arr += 1
                ptr_array += 1
            
