[Return Home](0-welcome.md)

# <span style="color:yellow">Sets!</span>

A set is another very useful data structure. Like a stack, sets generally have a very fast performance. Usually the performance of a set is O(1) due to a process called hashing. However, unlike stacks, sets do not find their usefulness in keeping things in order. The real strength of a set is its ability to not allow duplicates. Sets are able to keep duplicates out by using something called hashing.

#

# <span style="color:yellow">Hashing</span>

Hashing is a process that is used to add and remove items to and from a set, as well as check for membership in the set. Hashing makes sets perform quickly because it assigns each piece of stored data a value. Then when that piece of data needs to be found, the set can quickly look at the data's location based on the value given by the hash function.

A hash is a mathematic equation that data is run through to put the data in a spot in the set.

A simple example of a set is index(number) = number.

Given the following set, the top being the index and bottom the data held,

| Zero | One | Two | Three | Four |
| ---- | --- | --- | ----- | ---- |
| 1    |     |     | 4     |

<details>
  <summary><span style="color:orange">Why the spaces?</span></summary>
  There are spaces within the set because it is what we call a sparse list. This just means that not every index needs to be filled.

</details>
</br>

look what happens when we plug in another number.

index(2) = 2
Zero| One | Two | Three | Four
--|---|---|---|---
1 | 2 | |4 | |

The data is then added to the second index.

Now take a second to think about what will happen to that same set if we put the number 1 through
our hash function.

 <details>
  <summary><span style="color:orange">What will happen?</span></summary>
  Nothing! because 1 is already stored in our set, it will not be added again. This happens because we have already determined the location of 1 with our hash function, and because it is the same function, the out put is the same. This is how sets stop duplicates from appearing.

index(1) = 1

| Zero | One | Two | Three | Four |
| ---- | --- | --- | ----- | ---- |
| 1    | 2   |     | 4     |      |

#

</details>
<br/>

This way that hashing stops duplicates is how membership is easily tested within a set.

If we want to check and see if 3 is in our set we can plug it into our hash function and see where it should be located.

index(3) = 3

Now we know that 3 should be at index number three (Two)

| Zero | One | Two | Three | Four |
| ---- | --- | --- | ----- | ---- |
| 1    | 2   |     | 4     |      |

We know that index three is empty, so 3 is not in our set.

A set this small is good for demonstration, but not very practical in the real world as there isn't a lot of space for data to be stored.

#

# <span style="color:yellow">Hashing in Python</span>

Python has a built in hash function. This hash function works the same as our simple one, but is better equipped for more complex data, while ours would only work with numbers in range of the size of the set.

```python
print(hash(0))
# 0
print(hash('Bed'))
# -6165277921325111985
print(hash("bed"))
# 490261703700477627
print(hash(25.67))
# 1544914816173178905
print(hash(False))
# 0
```

This example code shows the built in hash function and its output. As you can see this function works with many different data types.

# <span style="color:yellow">Conflicts</span>

You may have seen an issue in the values in the previous code. 0 was output twice. This is an issue because while sets keep out duplicates, the actual value is not duplicate. So what do we do?

There are two common ways of dealing with conflicts like this in sets, Chaining and Open Addressing.

<span style="color:gold">Chaining</span>

With chaining, whenever a duplicate index is found, a list is created at that index to contain the different pieces of data.

For example with the two 0s:
Zero| One | Two | Three | ...
--|---|---|---|---
0 | | 2 | | |

Zero is already stored, so the set becomes this when False is added to the set
Zero| One | Two | Three | ...
--|---|---|---|---
[0, False] | | 2 | | |

<span style="color:gold">Open Addressing</span>

The other common way of dealing with conflicts is called open addressing. With open addressing, when an index is already being used, the data needing to be stored is stored in the next available index.
For example if we wanted to add False, it would look like this
Zero| One | Two | Three | ...
--|---|---|---|---
0 | False | 2 | | |

Now look what happens if more values are already stored in the set like so.
Zero| One | Two | Three | Four |
--|---|---|---|---|
0 | 1 | 2 | 3 | |

Since False should be stored in the zero index, it will need to be stored somewhere else. In this case, there is only one available space, Four, so the data will be stored there.
Zero| One | Two | Three | Four |
--|---|---|---|---|
0 | 1 | 2 | 3 | False |

## <span style="color:yellow">Operations</span>

There are four main operations used with the set data structure.

#

#1 add(value) </br>
&emsp; The add() operation adds a given value from the set. The syntax for an add operation in Python is <span style="color:gold">set.add(value)</span>. An O(1) operation.

#

#2 remove(value) </br>
&emsp; The remove() operation removes the given value form the set. The Python syntax for a remove() operation is <span style="color:gold">set.remove(value)</span>. An O(1) operation.

#

#3 member(value) </br>
&emsp; The member() operation checks if the given value is contained in the set. The Python syntax for member() is <span style="color:gold">if value in set: </span>. An O(1) operation.

#

#4 size() </br>
&emsp; The size() gives the amount of items contained in the set. The Python syntax for size() is <span style="color:gold"> length = len(set) </span>. An O(1) operation.

#

#5 create() </br>
&emsp; The create operation is used to create an empty set. The Python syntax for create() is <span style="color:gold"> set = set() </span>. An O(1) operation.

<details>
  <summary><span style="color:orange">Tip</span></summary>
  You can also create a pre-populated set from an existing list by using the list as an argument within set() like so <span style="color:gold"> set = set(list) </span> An O(n) operation.

</details>

#

<span style="color:orange">The mathematic operations: Intersection, Union, and Difference</span>

#6 Intersection </br>
&emsp; Intersection returns the values that two different sets contain. The Python syntax for Intersection is <span style="color:gold"> x = intersection(set1, set2)</span> or <span style="color:gold">x = set1 & set2</span>.

#

#7 Union </br>
&emsp; Union combines two sets into one. The Python syntax for Union is <span style="color:gold"> x = union(set1, set2)</span> or <span style="color:gold">x = set1 | set2</span>.

#

#8 Difference </br>
&emsp; Difference is the opposite of intersection returns the values contained the given set that do not appear in the argued set. The Python syntax for difference is <span style="color:gold"> x = set1.difference(set2)</span> or <span style="color:gold">x = set1 - set2</span>.

#

## <span style="color:yellow">Examples</span>

## <span style="color:gold">Example Problem</span>

Take a look at the following lists.

```python
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
31, 83,10]

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
52, 5]
```

Imagine you are tasked with writing a program to merge these lists
while removing the duplicate values. After which, you are to create a
list of the duplicate values. While writing code using loops could make
make this complicated, sets make it extremely easy as sets excel at dealing with duplicate values!

We can accomplish our first task with the following code.

```python
new_list = list(set(list1) | set(list2))
print(f'This is the list with duplicate values removed: {new_list}')

#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19, 21, 22, 23, 24, 25, 26, 31, 32, 34, 35, 36, 38, 41, 42, 45, 46, 47, 51, 52, 53, 54, 55, 56, 57, 62, 63, 66, 68, 73, 74, 76, 79, 83, 85, 87, 88, 91, 93, 98]
```

Now we need to create a separate list that contains only those duplicate values.
This is also simple using sets.

```python
duplicate_list = list(set(list1) & set(list2))
print(f'This is the list containing all the duplicate values: {duplicate_list}')
#Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 16, 21, 22, 23, 24, 25, 32, 34, 35,
#36, 41, 46, 52, 53, 56, 62, 63, 66, 68, 73, 74, 85, 88, 93]
```

[See the solution all together here](code_examples/set_example_problem.py)

As you can see, sets are a very useful tool to use when working with duplicates!

#

## <span style="color:gold">Problem to solve</span>

Now you try!

Using the original two lists from above write a function that will find the numbers that are
unique and are not contained in the list as a palindromic number (mirror number Ex. 13 & 31) of another number contained in either of the lists.

Example: If the given lists are [1, 13, 20, 24, 68, 77] and [1, 31, 20, 42, 67, 99], your program
will return [20, 67, 68] &emsp; (Note that 77 and 99 are palindromic numbers of themselves).

Start your program with the following code

```python
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
    pass
```

<details>
  <summary><span style="color:orange">Tips</span></summary>
    <span style="color:gold">int(str(i)[::-1]) </span> is a simple way of reversing the order of a number

</details>

<details>
  <summary><span style="color:orange">Expected Output and Solution</span></summary>
    [64, 65, 97, 67, 37, 39, 43, 75, 78, 15, 81, 86, 89, 58, 61]
    </br>

[Possible Solution](code_examples/set_problem_to_solve.py)

</details>

</br>

[Previous Tutorial](1-stacks.md)

[Next Tutorial](3-trees.md)
