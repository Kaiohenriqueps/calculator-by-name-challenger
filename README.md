# calculator-by-name-challenger
Get a input definition of a variable, calculate expressions by name instead of values.

## Operations
1) def: definition of a variable
2) calc: calculate expression
3) clear: clear all the definitions

## Input formats
1) The input can be a definition of a variable, such as:
```
def foo 3
def bar 7
```

2) The input can be a calculation from an expression, such as:
```
calc foo + bar =
```

## Output formats
When the result hasn´t a definition, the result is a string "unknown", as:
```
def foo 3
def bar 7
calc foo + bar =
foo + bar = unknown
```

When the result has a definition, the result is the name of the variable, as:
```
def foo 3
def bar 7
def programming 10
calc foo + bar =
foo + bar = programming
```