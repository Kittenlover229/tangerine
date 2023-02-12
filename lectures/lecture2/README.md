# Lecture 2

## Overview

<!--Addendum to lecture 1:-->
* Compound operators
* Modular arithmetic

<!--Sequences-->
* Lists
* `zip` and `enumerate`
* Sequence Minimum and Maximum

<!--Some Algorithms, Abstracting Them As Function-->
* Linear Search
* Loop Binary Search
* Recursive Binary Search

<!--Drawing-->
* Simple Drawings With Turtle
* Koch Snowflake

<!--Addendum-->
* Two techniques for 2D lists: lists of lists and linearization
* Sliding Window Technique
* Slicing
* `split`ing strings into lists
* Comparing strings (Lexocographically)

## Contents

### Intro

* Sound check
* Welcome everyone for coming to the second lecture, I'm very glad everyone present made it today.
* Without any further ado let's talk about something important.

### Compound Operators

* During our last lecture we used several builtin arithmetic operations (`+`, `-`, `*`, `/` and `**`)
* First I would like to make you aware that all of them are available as function. I remind you that functions are the specific commands that we request the language to execute. 
* It is often needed that we use arithmetic on a specific variable, if you recall our example of a counting program. Let's look at it again.

```py
x = 0
while x > 0:
    y = x
    while y > 0:
        y = y - 1
        print(y)
    x = x - 1 
```

* The expression `a = a - 1` occurs twice in this small snippet of code and you gonna see it a lot. If we also think about, say, the while loop counting up.

```py
x = 0
while x < 10:
    x = x + 1
```

* Arithmetic operations on a variable that involve the variable itself occur very often and there is a handy notation you may use, I've heared it called compound assignment. The aforementioned program can be rewritten like this.

```py
x = 0
while x < 10:
    x += 1
```

* This works for all the arithmetic operations we've discussed and will discuss in the future. Sadly, this doesn't work for functions.

### Lists

* Working with individual variables in fun and all but usually you are processing sets of data. Take minecraft, it operates a lot of blocks at the same time, do you really think each of those is its own variable?

* To handle this lists were invented. A list is, as the name implies, a list.

* It can be indexed. That's to say you can get the Nth element of the list. That's called indexing. Check it out.

```py
x = [1, 2, 3]
print(x[1])
```

* The simplest list is an empty one. You can also construct the list using the `list()` function.

* And we are seing a 2. I wonder why that it.

* It is like this for many reasons, mainly convinience and historic ones. Zero is absolutely a valid integer and ther is no nnanguage C there were no lists, there was raw memory and you had something that was point to a "blob of integers" or "blob of floats". When you wanted to get a specific element you would count how many integers or floats respectively it was from the start. The first integer in a sequence was of course 0 integers or floats away from the start so its index was zero.

```
My lovely integer storage:

start of integers in memory
|
v
+-----------+-----------+-----------+
| integer 1 | integer 2 | integer 3 |
+-----------+-----------+-----------+
```

* This is a programming tradition and is seen in most of the modern languages and I would like you to remember that they are indexed from 0. Just keep it in mind when coding. 

* What is the simplest thing we can do with a list? Print it out of course.
```py
ls = [5, 6, 3, 5, 3, 3]

for i in range(len(ls)):
    print(ls[i])
```

* Now ranges starting at 0 probably makes even more sense. We are also using the `len` function to get the length of our lit. Can someone guess what it is in this example? No surprises there.

* But we can simplify this even further, you see, lists are iterable objects.Try and unpack this statement. Well, an object is a "thing". It has a type and some functions we can use on it. 

* What is an iterable? It's just something you can iterate through, meaning you can use a `for` loop just fine. 

* Usually these objects are also homogeneous. A list is homogeneous if it consists of elements of the same types (notice the plural, we will talk about that later). A list all elements of each are 

* We are, in fact, already familiar with one other homogeneous iterable object. That's the range. Let's verify that it is indeed an iterable homogenenous object.

* Lists are also mutable, that means you can change. Common operations include `append` for adding a single element to the list, `pop` for removing an element at a certain index (and retrieving it),`clear` for removing all the elements of a list, `extend` for attaching a list as a tail of some other list. `remove` for removing

* You may also freely nest lists as far as you want.

```py
one_deep_list = [1, 2, 3, 4, 5, 6]
two_deep_list = [[1, 2], [3, 4], [5, 6]]
three_deep_list = [[[1], [2]], [[3], [4]], [[5], [6]]]
```

* As you might have already noticed indexing a specific element of the list looks very similar to creating a list. That might lead to notation abuse like this.

```py
[[[[0][0]][0]][0]]
```

* Specific list elements can also be assigned to. All of this combined makes for a great tool for processing large chunks of data with the same algorithm. From our previous lecture we might recall our maximum algorithm, let us try and implement the opposite of that, a minimum algorithm that operates on a list. 

```py
lovely_lovely_list = [3, 488, 5, 6]

max_item_so_far = None
for list_item in lovely_lovely_list:
    if max_item_so_far > list_item:
        max_item_so_far = list_item

print(max_item_so_far)
```

* There is a new keyword "None", but it just means that there is no value was found just yet. This is a concious choice.

* Spend some time exploring the algorithm. Verify that it works.

* Now, let's change our task a bit, find the maximum element of a list and spit out it's index. For that purpose there is a helper function `enumerate`. It
goes through of all the elements of a list with their indices.

```py
lovely_lovely_list = [3, 488, 5, 6]

max_item_so_far = None
max_index_so_far = None
for index, item in enumerate(lovely_lovely_list):
    if max_item_so_far > item:
        max_item_so_far = item
        max_index_so_far = index

print(max_index_so_far)
```
* Great! Verify that it works. We can use that example to revise some terminology. An index is whatever the value some object is inside the list, indices start from zero. An object inside the list is called an element. Getting an element from a list is called indexing. 

* Now, another common thing is finding an object to satisfy a certain criterion and that we did. More common is filtering, so let's have a look an example.
