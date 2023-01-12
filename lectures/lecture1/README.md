# Lecture 1

## Contents

### Part 1: Meta

* Sound check
* Hello, thanks everyone for coming
* This course is rather advanced in places, but I will do my best to keep it real and practical since it's our goal anywway
* Let's do a vibe check. How familiar is everyone with computing in general
* Programming is
    * Computer Science - all the theoretical stuffwwhich covers all of how computers work (or should work in theory for that matter)
    * Programming Practise - useful tips and tricks to use in your program and general practices
    * Data Structures & Algorithms - solutions to common well-known and thoroughly researched problems
    * Mathematics - no surprises here hopefully
    * Group Work - coordinating a team of developers
    * Soft Skills - talking to other developers and communicating your thoughts clearly
* What are we doing today? Basic language overview, some basic operations on data.
* What is python? A universal prorgramming language, it can do pretty much anything. It is used in statistical analysis, machine learning, AI, data storage, web servers, discord bots, robotics, game development (e.g. the among us game server is made in Python). A swiss knife so to say.
* Simplest program: an empty program
* Simplest program 2: just a print expression, no function calls yet
* Simplest program 3: printing a Hello world
* Using the interpreter for interactive development is basically like having a dialogue with the computer. You prompt questions, it answers you.
* The `help` command. "Object" is a fancy way of saying "thing".
* Official documentation [here](./links.md)

### Part 2: Stupid Programming

* Python as a scientific calculator (+, -, *, /, **)
* Python has long arithmetic
* Storing a variable
* Type is akin to the mathematical concept of a set member. Take the `int` type, in mathematics it's represented with a Z and contains all the possible whole numbers, integers. Here type is also that. Take number `5`, it's a whole number and is of type `int`.
* You can use the `type` function to get the type of an expression
* Logical expressions with (==, <, >, <=, >=)
* Booleans are simple, it's a value that is either true or false, they have some laws related to that but we wwill talk about that later
* You can store a computed value in something called a variable, that will allow you to access it later
* Imprecision when storing fractional numbers, the float type
* Strings! Bits of text, put in quotes, very lovely and useful.
* Your usual operations also work on strings, you can multiply them like this

```py
"Hi " + " mark"

"0" * 5 #   = "00000"
0 * 5 #     = 0
```

* Notice that when multiplying something of type "str" we get a "str"
* And yet when multiplying an "int" we get an "int"
* Types don't represent just the values, they also represent possible operations with your data
* Zen of python, philosophy of the language, `import this`
* Typecasting is the act of changing one type into another

```py
0 * 5       # 0
str(0) * 5  # "00000"
y = 3.14
type(y)     # float
y = int(y)
type(y)     # 3
```

* Operations can fail, this is called exceptions, but I prefer the word
explosion. For example when converting a string without text into an integer you will have trouble. That will abort the execution of your program.
* But `int` wouldn't round a fraction. It truncates it, basically reducing it to it's integer part. For rounding there are functions `ceil` and `floor`.
* This is great and all but we want our programs to be interactive. For that you may use the `input` function, let's have a look. It allows us to read a string from the user, lovely, isn't it?
* Now we would love to make a program that says hello to us, but how? Well, there is some input and some output, we are going to input our name and have a response of "Hello, name!", where the name is our actual name, no surprises there. Let's write it out using our current knowledge.
* Important bit relating to the python zen: don't reuse variables. If you used the variable `name` don't reuse it to store the `surname`, that will make your programs difficult to read and believe me, your code is written once, but read many more times and not just by you. Let's modify our example to include the last name.
* You can do simple programs since this is enough, let's make a program to compute a quadratic equation with two guaranteed roots and express it like a chain of blocks
* Now let's do the program live, I don't have the code for it prepared

### Part 3: But what if...

* Sometimes a program needs to behave more intelligently, for example we know that if out discriminant is less than zero we can't really compute the roots. What do we do? We use booleans and ifs, let's rewrite out example to account for this. 
* You may notice that while developing the program I run it several times on simple examples to see how it works and see if it behaves well enough. This may seem difficult at first, but this is the best way to find what your errors are. 
* This process is called debugging, removing bugs basically. Bugs in the context of computer programming refers to errors and unintended behaviour.
* Great! Now it works and handles some specific conditions, good job us

### Part 4: Loop de loop

* Now let's move a little away from mathematics into something more specific.


# Misc

Where do I find documentation?
