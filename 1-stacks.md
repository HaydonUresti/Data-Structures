[Return Home](0-welcome.md)

# <span style="color:yellow">Stacks!</span>

Stacks are a very useful and common data structure! You may not realize it, but you likely interact with stacks on a daily basis.

A couple of very common examples of stacks include the arrow buttons in a web browser, or the use of control + z and control + y on many computer applications. What are the purposes of these? What do they have in common?
Think about it for a moment and click the tab below and compare what you came up with!

<details>
  <summary><span style="color:orange">Stack Example</span></summary>
  Both the control + z/control + y and the arrow buttons help navigate you to a previous spot, whether that be a web location or an action taken. 
  
  This ability to go back is a key strength of stacks.
</details>
<br/>

## <span style="color:yellow">How Do They Work?</span>

Stacks work in a similarly to regular lists. Both stacks and lists are made to contain data. Data can be both added and removed from the data structures.
The difference between stacks and lists comes in the way information is removed and added.

In a list, data can be added or removed from anywhere.

If we were to create a list of [a,b,c], we could add each letter in whatever order we'd like. All we need to know is the index of the location that we want. It is the same for removing data.

In a stack, we can only add and remove data from the very last index. For example, adding data would look something like this: <br/>
![example of adding to a stack.  [a]  --> [a,b]  --> [a,b,c]...](images/stack_ex.jpg)

Removing would be opposite of that and look like this:

![example of popping a stack.   [a,b,c] --> [a,b] --> [a] --> [ ]](images/stack_pop_ex.jpg)

Adding and removing data in this way makes the stack a very fast data structure. With each of its main operations having an O(1) performance as there is no need for iteration as only the last item is the one used at a given time. </br>
The other strength to only working with the last item, is that it stays in an order. This order is why it is used to do things like keep track of histories like the the examples given earlier.

## <span style="color:yellow">Operations</span>

There are four main operations used with the stack data structure, and each has a performance of O(1).

#

#1 push(value) </br>
&emsp; push() is the operation that adds a value to the end of a stack. The syntax for a push operation in Python is <span style="color:gold">stack.append(value)</span>.

#

#2 pop() </br>
&emsp; pop() is the operation that removes the last value from the stack. The Python syntax for a pop() operation is <span style="color:gold">stack.pop()</span>.

<details>
  <summary><span style="color:orange">A helpful tip with for the pop operation</span></summary>
 Use the syntax <span style="color:gold">var = stack.pop()</span> to save the last value to a variable while deleting it from the stack at the same time.
</details>

#

#3 size() </br>
&emsp; The size() operation will return the size of the stack. The Python syntax for size() is <span style="color:gold">length = len(stack)</span>.

#

#4 empty() </br>
&emsp; The empty() operation is used to check if the stack is empty or not. The Python syntax for empty() is <span style="color:gold">if len(stack) = 0: </span>.

#

## <span style="color:yellow">Examples</span>

### <span style="color:gold">Example: </span> </br>

The following example makes use of a stack to keep track of a history of items needed by someone. A stack is ideal for the situation as it will help its user know what item he is on next, even if another item is added in the process of checking things off.

</br>
Miguel is at a flee market. As he walks around he came across an item he realy wanted. It was a golden rubber duck that he just had to add to his collection. The man at the booth said he would only trade it for a rare comic book held by another one of the vendors. Miguel then approached the comic book owner to be told they would only trade for another item in the market. This trend continued for Miguel for 4 more vendors, whose items include a guitar, a car a spoon, and a fossil. </br>
As the list became more complicated, Miguel decided to make a program and use a stack to keep track of the items still needs. </br>
Write code to show what this might look like.

```python
#create an emty list/stack
items = []

#append the items to the stack in the order Miguel needs them
items.append('rubber duck')
items.append('comic book')
items.append('guitar')
items.append('car')
items.append('spoon')
items.append('fossil')
```

Miguel was able to get and trade the fossil, the spoon, and the car successfully. In his rush to get the items, Miguel forgot how many more he needs. </br>
Write the code Miguel would use to remove the items he has gotten from the his stack. Use a loop to do so and print out each deleted item. After the items are removed, check the list for how many more items Miguel needs.

```python
#remove the items Miguel has already gotten
for i in range(3):
    item = items.pop()
    print(item)

#check how many items are left
print(len(items))
```

Miguel then goes to get the guitar he needs, but as the owner hands it to him it is dropped and breaks. Miguel talks to he vendor wanting the guitar and is told that an antique camera will work as a trade instead. The vendor with the camera then wants a ceiling fan in exchange for the camera. </br>
Write code to add the new needed items to Miguel's stack

```python
#add the newly needed items to the stack
items.append('camera')
items.append('fan')
```

Miguel gets the ceiling fan and successfully trades all the needed items to get the golden rubber duck. </br>
Write the code to continue removing items from Miguel's stack, then check and make sure there is nothing left in the stack. If the stack is empty, print how many more items are needed.

```python
#remove the rest of the items from the stack
items.pop()
items.pop()
items.pop()
items.pop()
items.pop()

#check to see how many items are left in the stack
if len(items) == 0:
    print('There are no more items to get.')
else:
    print(f'{len(items)} items are still  needed')
```

While this example might seem strange, it does showcase many basic operations of a stack.

#

## <span style="color:gold">Problem to solve</span>

Now you try!

In this example you are going to be acting as the control + z/control + y for the inputs of a user. In this scenario, the item added may be a string of words (I ate an apple), a single word (apple), or a single letter (a) depending on the time taken for the user to input data. Assume that all the input given is exactly as the user would want it printed out. If the input is control + z or control + y use the proper operations on the stack. You may find the use of the list operator .clear() to be useful.

Input: I am so excited for this weekend! </br>
Input: Icant wait </br>
Input: control + z </br>
Input: I can't wait to go </br>
Input: to the lake! </br>
Input: I haven't been there in years.</br>
Input: I used to go there </br>
Input: control + z</br>
Input: control + z</br>
Input: I have't been there in over a decade.</br>
Input: My favorite thing to do ate the lake is </br>
Input: Going</br>
Input: out on my families boat. </br>
Input: I hope the water will be good for boating. </br>
Input: control + z </br>
Input: control + z</br>
Input: out on my family's boat </br>
Input: control + z</br>
Input: control + z</br>
Input: control + z</br>
Input: control + y</br>
Input: going boating with my family. </br>

Finally, print the final complete message the user writes.

<details>
  <summary><span style="color:orange">Hint</span></summary>
 Find a way to keep track of the popped value. Also think about how control + z and control + y relate.  
</details>
<br/>

<details>
  <summary><span style="color:orange">Expected output</span></summary>
 ['I am so excited for this weekend!', "I can't wait to go", 'to the lake!', "I haven't been there in over a decade.", 'My favorite thing to do at the lake is ', 'going boating with my family.']

Note that either an error or nothing will occur if control + y were to be input again.

</details>
<br/>

[Possible solution to example 2](code_examples/stack_problem_to_solve.py)

[Next Tutorial](2-sets.md)
