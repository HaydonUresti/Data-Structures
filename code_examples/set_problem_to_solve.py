# The lists we are working with
list1 = [1,16,1,14,66,32,46,35,62,66,
26,53,36,42,79,54,26,35,53,24,
57, 46,23,68,42,47,55,6,7,7,9,4,2,
46,1,4,6,2,8,9,3,35,21,66,23,63,25,
74,11,73,14, 85, 34, 68, 93, 2, 56,
25,21,6,21,53,7,6, 88, 32, 21, 3, 
5, 1, 41, 36,23, 52, 35, 56, 13, 
5, 1, 5, 62, 22,62, 7,2, 52, 52,
5, 13, 5, 1, 2,3,7, 93,3, 6, 2, 13,
52, 46, 62,1, 12, 35, 34,51, 53, 1,
5, 11, 18, 91, 19,13, 31, 38,
31, 83,10, 99]


list2 = [1, 5, 24, 52, 62, 5, 6, 23, 
2, 6, 87, 25, 24, 6,24,24, 62, 6, 2,
1, 6, 8, 8, 98, 35, 32,62, 13, 45, 2,
6, 13, 13, 24,25, 16, 62, 62, 62,
73, 23, 25, 34, 7, 46, 45, 63, 73, 
76, 4, 6, 2, 8, 9, 3, 35, 21, 66, 23, 63, 
25,74, 13, 73, 14, 85, 34, 68, 93, 2,
56, 25, 21, 6, 21, 53, 7, 6, 88, 32, 21,
3, 5, 1, 41, 36, 23, 52, 53, 56,
13, 5, 1, 5, 62, 22,62, 7,2, 52, 
52, 5, 77]



def find_unique_numbers(list_1, list_2):
    """A funtion that finds unique numbers that 
    are also not palindromic of any number in 
    either of the two lists.
    Parameters:
        list1: a list of integers 
        list2: a list of integers
    Returns:
        Returns a list of the numbers from the two lists that 
        are unique and not palindromic.
    """
   #Create a set from the parameter lists to remove duplicate numbers
    set_a = set(list1) | set(list2)

    #Create an empty set to add values to
    set_b = set()

    #A for loop going through all the numbers, reversing each one, and 
    #adding it to the new set
    for i in set_a:
        set_b.add(int(str(i)[::-1]))

    #returning the difference of the sets as a list    
    return list(set_b.difference(set_a))


print(find_unique_numbers(list1, list2))

#Output: [64, 65, 97, 67, 37, 39, 43, 75, 78, 15, 81, 86, 89, 58, 61]
