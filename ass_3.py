# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 20:13:42 2023

@author: Dell
"""

"""
Given an integer array of size n, find all elements that appear 
more than ⌊ n/3 ⌋ times
"""
def majority_elements(nums):
    n = len(nums)
    threshold = n // 3

    # Use a dictionary to count occurrences of each element
    count_dict = {}

    # Count occurrences
    for i in nums:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    # Find elements that appear more than n/3 times
    result = [i for i, count in count_dict.items() if count > threshold]

    return result
                
nums=[1,1,1,1,2,3,3,3]
print(majority_elements(nums))
    
    
        

            
        
    
        
        
            