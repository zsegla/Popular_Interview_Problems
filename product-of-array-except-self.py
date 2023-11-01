# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]
        for i in range(1, len(nums)):
            products.append(nums[i-1]*products[-1])
            
        right_product = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= right_product
            right_product *= nums[i]
            
        return products
            # res = [1] * len(nums)
#             prefix = 1
#             for i in range(len(nums)):
#                 res[i] *= prefix
#                 prefix *= nums[i]
                
#             postfix = 1
#             for i in range(len(nums)-1, -1, -1):
#                 res[i] *= postfix
#                 postfix *= nums[i]
                
#             return res
#  this one is the most efficient way
