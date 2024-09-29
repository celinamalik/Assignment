#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:13:59 2024

@author: celinamalik
"""
#PART A

#This file contains the Python code used to create each function. 

from math import sqrt
#This line imports the square root function into the file.

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    N = len(x)
    #The variable N is the length of the sequence, needed to compute the mean.
    
    mean = 0
    #To sum a sequence of numbers, we must use a base value.
    #Zero is a neutral element, so it ensures a correct starting point.
    
    for i in range(N):
        mean = mean + x[i]
    mean = mean/N
    #This for loop calculates the mean for step 1. For every value in the sequence, it is
    #summed to find the total mean, and then divided by the length of the sequence.
    
    meansq = 0
    for i in range(N):
        meansq = meansq + x[i]**2
    meansq = meansq/N
    #Step 2 is finding the mean of squares. This for loop uses the same approach as in
    #step 1, except it squares each value in the sequence before summing it.
    
    var = meansq - mean**2
    #Step 3 is finding the variance, by subtracting the mean squared from the mean of squares.
    
    return sqrt(var)
    #Finally, we return the square root of the variance, which is the standard deviation.


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    N = len(x)
    
    mean = sum(x)/N
    #In this approach, the mean is found by simply taking the sum of every value in 
    #the sequence with the sum function and dividing it by the length.
    
    meansq = sum(x**2 for x in x)/N
    #Here the mean of squares is found. A for loop is used, as every value in the sequence
    #must be squared before we can take its sum. Integrating a for loop ensures that this
    #takes place. It is also divided by the length of the sequence.
    
    var = meansq - mean**2
    #The variance is found in the same way as for the previous function.
    #And finally, we return the square root of the variance, once again.
    return sqrt(var)

import numpy as np

def stdnumpy(x):
    return np.std(x)
#Here, the creation of this formula is very straightforward. We must import numpy
#to ensure that we can use its functions. Then, we simply use the numpy standard
#deviation formula as what we return for the function. 

num_lst = [1, 2, 3, 4, 5]
#Finally, we test the functions on this list to make sure they all return the same
#values. We can thereby proceed to finding the standard deviation of the dataset columns.

print('Standard deviation loops:', std_loops(num_lst))
print('Standard deviation functions:', std_builtin(num_lst))
print('Standard deviation numpy:', stdnumpy(num_lst))
