# Lecture 2

## Overview

<!--Addendum to lecture 1:-->
* Compound operators
* Modular arithmetic

<!--Sequences-->
* Lists
* Sequence Minimum and Maximum
* Sliding Window Technique
* Slicing

<!--Function-->
* Functions in their mathematical sense
* Functions as units of execution
* Mathematical Induction and Recursion
* Loops and Recursion (Curry–Howard correspondence)
* Recursive Maximum & Recursive Minimum
* Functions & Lists, pass by value and pass by reference

<!--Some Algorithms, Abstracting Them As Function-->
* Linear Search
* Loop Binary Search
* Recursive Binary Search

<!--Drawing-->
* Simple Drawings With Turtle
* Koch Snowflake

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

* And we are seing a 2. I wonder why that it.

* It is like this for many reasons, mainly convinience and historic ones. Zero is absolutely a valid integer and ther is no need to disregard it when working with lists, but I prefer another point of view.

* In the eldrich programming language C there were no lists, there was raw memory and you had something that was point to a "blob of integers" or "blob of floats". When you wanted to get a specific element you would count how many integers or floats respectively it was from the start. The first integer in a sequence was of course 0 integers or floats away from the start so its index was zero.

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
    print[i]
```

* Now ranges starting at 0 probably makes even more sense. We are also using the `len` function to get the length of our lit. Can someone guess what it is in this example? No surprises there.

* But we can simplify this even further, you see, lists are iterable objects.Try and unpack this statement. Well, an object is a "thing". It has a type and some functions we can use on it. 

* What is an iterable? It's just something you can iterate through, meaning you can use a `for` loop just fine. 

* Usually these objects are also homgeneous. A list is homogeneous if it consists of elements of the same types (notice the plural, we will talk about that later). A list all elements of each are 

* We are, in fact, already familiar with one other homogeneous iterable object. That's the range. Let's go through it.

## Misc

* Lists can be heterogenous: elements of a list can be of different types and this is suboptimal
