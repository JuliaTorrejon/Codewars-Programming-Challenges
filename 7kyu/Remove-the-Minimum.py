def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a
    
# Notes: [:] is the array slice syntax for every element in the array. The remove() method searches for the given element in the list and removes the first matching element.
