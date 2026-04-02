# **AI_ASSIGNMENT-4**
---
## **Constraint Satisfaction Problems (CSP) Assignment**

This repository contains implementations of fundamental Constraint Satisfaction Problems (CSP) using Python.
All problems are solved using the Backtracking algorithm while enforcing the required constraints at every step.

---

## **Name:** MUPPALLA LIKITH

## **Roll No:** SE24UCSE062

---

## **Problem 1: Australia Map Coloring**

### **Description**

The Australia map coloring problem considers each state as a variable: WA, NT, SA, Q, NSW, V, and T.

Each state is assigned a color from a domain consisting of Red, Green, and Blue.

### **Constraint**

No two adjacent states can have the same color.

### **Approach**

* Represent states and their adjacency using a graph structure
* Apply backtracking to assign colors
* Validate constraints before each assignment

### **Output**

A valid coloring of all states such that no neighboring states share the same color.

---

## **Problem 2: Telangana Map Coloring**

### **Description**

This problem extends the map coloring concept to the districts of Telangana, where each district is treated as a variable.

### **Constraint**

Adjacent districts must not have the same color.

### **Approach**

* Model districts as variables
* Define adjacency relationships between districts
* Use backtracking to assign colors while satisfying constraints

### **Output**

A valid color assignment for all districts with no adjacency conflicts.

---

## **Problem 3: Sudoku Solver (CSP)**

### **Description**

Sudoku is modeled as a CSP where each cell in the grid is treated as a variable with a domain of values from 1 to 9.

### **Constraints**

* Each row must contain unique numbers from 1 to 9
* Each column must contain unique numbers from 1 to 9
* Each 3×3 subgrid must contain unique numbers

### **Approach**

* Represent the Sudoku grid as a set of variables
* Use backtracking to fill empty cells
* Check all constraints (row, column, and subgrid) before assignment

### **Output**

A completely solved Sudoku grid that satisfies all constraints.

---

## **Problem 4: Cryptarithmetic Puzzle (TWO + TWO = FOUR)**

### **Description**

Each letter represents a unique digit, forming a valid arithmetic equation.

### **Constraints**

* Each letter maps to a distinct digit
* Leading digits cannot be zero
* The equation TWO + TWO = FOUR must hold true

### **Approach**

* Generate permutations of digits
* Assign digits to letters
* Validate the arithmetic equation and constraints

### **Output**

A valid mapping of letters to digits such that the equation TWO + TWO = FOUR is satisfied.

---

## **Concepts Used**

* Constraint Satisfaction Problems (CSP)
* Backtracking Algorithm
* Constraint Propagation
* Search Space Exploration

---

## **Conclusion**

This assignment demonstrates the application of CSP techniques in solving real-world problems such as map coloring, Sudoku, and cryptarithmetic puzzles.
Backtracking efficiently explores possible solutions while ensuring that all constraints are consistently satisfied.
