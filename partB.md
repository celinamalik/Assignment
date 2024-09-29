# **Part B - Comparing Run Times**

***

I will now be comparing run times of the various approaches used to create formulas for finding standard deviation.
The code is depicted below, and the final conclusion is shown towards the bottom of this file.

In this file, I began with importing the various formulas defined in Part A. 
I named the file `formulas` for ease, but it is the same file as the Part A file. 
***


```python
from formulas import std_loops, std_builtin, stdnumpy
```

***
Now, I use the `open` function to open the comma-separated values sheet named `data.csv`. However, a `with` function precedes this line,
as it is used for opening files in Python to prevent the system from crashing. The mode is set to `r` to read the data, with returns text.

Next, the three separate columns are created into their corresponding variables, set equivalent to an empty list - this will store the data 
for each column.

I then created a `for` loop for each column in the file. Using `strip` will erase any extra spaces, while `split` will split each column into a list of values separated by commas.

Since the dataset file was set to a mode of `r`, it is vital to convert the values into floats. This is done after using separate `if` statements to append each value to its respective column. Now the columns are finally separated into respective lists, and we can use the standard deviation formulas for each column.
***


```python
with open('data.csv', 'r') as file:
    col1 = []
    col2 = []
    col3 = []

    for col in file:
        col = col.strip()
        nr = col.split(',')
        
        if nr[0].strip():
            col1.append(float(nr[0].strip()))
        if nr[1].strip():
            col2.append(float(nr[1].strip()))
        if nr[2].strip():
            col3.append(float(nr[2].strip()))
```


```python
print('Column 1.')
print('**************************')
print('Loops:', std_loops(col1))
print('Functions:', std_builtin(col1))
print('Numpy:', stdnumpy(col1))
print()
print('Column 2.')
print('**************************')
print('Loops:', std_loops(col2))
print('Functions:', std_builtin(col2))
print('Numpy:', stdnumpy(col2))
print()
print('Column 3.')
print('**************************')
print('Loops:', std_loops(col3))
print('Functions:', std_builtin(col3))
print('Numpy:', stdnumpy(col3))
```

    Column 1.
    **************************
    Loops: 0.2823721097353601
    Functions: 0.2823721097353601
    Numpy: 0.28237210973536014
    
    Column 2.
    **************************
    Loops: 0.28467443283850546
    Functions: 0.2846744328385061
    Numpy: 0.28467443283850596
    
    Column 3.
    **************************
    Loops: 0.2854045269476155
    Functions: 0.28540452694761564
    Numpy: 0.2854045269476156


***

The values of the standard deviation for each column have now been calculated with each approach. 

We must now find the run-time of each approach for each column. The magic function `%timeit` allows us to do this. Below, the run-time of each approach is calculated starting with column 1. The first value in the 3 seperate outputs is the run-time for the loop approach, the second value is the run-time for the built-in approach, and lastly the third is for the NumPy approach. 

***


```python
%timeit std_loops(col1)
print()
%timeit std_builtin(col1)
print()
%timeit stdnumpy(col1)
```

    18.8 μs ± 6.2 μs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
    
    15.4 μs ± 395 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
    
    31.7 μs ± 510 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)



```python
%timeit std_loops(col2)
print()
%timeit std_builtin(col2)
print()
%timeit stdnumpy(col2)
```

    198 μs ± 49.6 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    
    144 μs ± 4.4 μs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
    
    94.3 μs ± 1.44 μs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)



```python
%timeit std_loops(col3)
print()
%timeit std_builtin(col3)
print()
%timeit stdnumpy(col3)
```

    2.21 ms ± 278 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    
    1.5 ms ± 66 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    
    663 μs ± 4.85 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


***

# Analysis of Results

### *Column 1 Analysis:*

The execution time of each function calculating standard deviation for column 1, which contains 100 values between 0 and 1, 
shows clearly which function is the fastest. It is apparent that the function using built-in functions is
the fastest. Although the approach using loops comes close, it is still slower, and the NumPy approach is the slowest.

### *Column 2 Analysis:*

This column contains 1000 values between 0 and 1. Here, the results differ from column 1. The medium-sized dataset leads to 
a general decrease in execution speed for all approaches. The function using NumPy outperforms the other functions significantly,
while the loop function is the slowest. 

### *Column 3 Analysis:*

Column 3 is the largest dataset, with 10 000 values, leading to a significant relative increase in execution time. However, 
NumPy once again is the clear winner out of all three approaches. It is, to a great extent, the fastest way of calculating
the standard deviation for the largest dataset. Once again, the loop function is the slowest.

 ***

## **Final Conclusion:**

The approach for calculating standard deviation using NumPy becomes the most efficient method as the size of the dataset increases.
However, for small datasets, it performs relatively slower. For small datasets, the built-in approach is the most efficient. The approach
using loops is consistently the slowest performing function across all datasets, and is clearly the least efficient method for
calculating standard deviation.
Overall, the approach using NumPy is generally the most efficient - the built-in approach is only faster at the smallest dataset by a negligable amount, and NumPy clearly outperforms it for larger datasets. 

***


```python

```
