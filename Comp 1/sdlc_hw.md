#Software Development Life Cycle Homework

You should refer to the **homework policy** for details on how this homework should be submitted.

**Attempt all questions and show all working.**

##Question 1
The diagram below shows an incomplete diagram of the systems development life cycle.

![](https://www.dropbox.com/s/itzcm89732xjqwb/incomplete_cycle.jpg?dl=1)

1. What phase of the systems development life cycle is (a)? (**1 mark**)
*Design*
2. What phase of the systems development life cycle is (b)? (**1 mark**)
*Testing*

##Question 2
Bob has a problem that he needs to solve. The problem is described below.
“There are two jugs – A and B. Jug A has a capacity of three litres. 
←
Jug B has a capacity of five litres. There are no markings on the jugs so it is not possible to see how much is in each jug just by looking at it (unless it is full or empty).

There is a sink with a water  tap and a drain. How can exactly one litre of water be obtained from the tap using the two jugs?”

A well-defined problem consists of a given, a goal, a set of resources, a set of constraints and ownership.


1. Describe the goal of this problem.  (**1 mark**)
*The Goal is to get exactly 1 liter*
2. Describe the set of resources available top Bob when solving this problem.  (**3 mark**)
*3 Litre Jug and a 5 Litre Jug*
*Sink with a tap and a drain*
3. What is meant by ownership of a problem? (**1 mark**)
*It means that "Who does what" basically*

##Question 3
The algorithm, represented as a flowchart in the diagram below and the variable table describe the converting of a **4-bit binary value into denary**.

![](https://www.dropbox.com/s/n87ng9d25x6irrw/flowchart.jpg?dl=1)

|Identifier|Data type|Purpose|
|----------|---------|-------|
|Column|Integer|Stores the place value (column heading)|
|Answer|Integer|Stores the denary value equivalent to the bit pattern entered by the user|
|Bit|Integer|Stores a 0 or 1 entered by the user|

1. Write a program for the above algorithm. Paste your program source code below (**11 marks**)

```python
#space for your source code
answer = 0
column = 8
while column > 1:
    bit = int(input("ENter bit value: "))
    answer =  answer +(column*bit)
    column = column/2
print("Decimal value is: {0}".format(answer))

```

2. Test the program by showing the result of entering the values `1, 1, 0, 1` (in that order).  Provide screen capture(s) for the test described above in the space below. (**3 marks**)

![](http://s25.postimg.org/jzjksxlxr/screen.jpg)

3. What is the largest denary number that could be output by the algorithm represented by the flowchart? (**1 mark**) 
*14*
4. The algorithm represented by the flowchart can convert sixteen different patterns into denary. If the symbol `Column ← 8` is changed to `Column ← 16` how many more bit patterns could be converted into denary? (**1 mark**)
*4 bit patterns could be converted into denary*

##Question 4
When developing a new system, the stages of the systems development life cycle could be followed.

1. At which stage of the systems development life cycle would the flowchart in Figure 4 have been created? (**1 mark**)
*Design*
2. At which stage of the systems development life cycle would the flowchart in Figure 4 be automated using a programming language? (**1 mark**)
*Implementation*



