# class Solution(object):
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    array = nums1 + nums2
    merged_array = sorted(array)
    length = len(merged_array)
    if (length % 2) != 0:
        middle_index = length // 2
        return merged_array[middle_index]
    else:
        upper_middle_index = length // 2
        lower_middle_index = length // 2 - 1

        middle1 = merged_array[upper_middle_index]
        middle2 = merged_array[lower_middle_index]

        return (middle1 + middle2) / 2
    
res = findMedianSortedArrays([1,2],[3,4,5])
print(res)