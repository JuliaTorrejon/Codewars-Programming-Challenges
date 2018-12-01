def sum_array(arr):
    if arr is None or len(arr) <= 1:
         return 0
    else:
         return sum(sorted(arr)[1:-1])
         
# Notes: There is a sorted() built-in function that builds a new sorted list from an iterable.
