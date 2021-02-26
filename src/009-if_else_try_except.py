#  imports as needed

def some_func():
    # If / Elif / Else conditionals - executing code based on one or more
        # conditions being evaluated as True or False; the "elif" and "else"
        # clauses are optional
    x = 5

    if x > 5: # if the "x > 5" expression is evaluated as True, the code
        # indented under the "if" clause gets executed, otherwise the execution
        # jumps to the "elif" clause...
        print("x is greater than 5")
    elif x == 5: # ...if the "x == 5" expression is evaluated as True, the code
        # indented under the "elif" clause gets executed, otherwise the execution
        # jumps to the "else" clause
        print("x IS 5")
    else: # this covers all situations not covered by the "if" and "elif" clauses;
        # the "else" clause, if present, is always the last clause in the code block
        print("x is NOT greater than 5" )

    # result of the above "if" block
    x IS 5

        # While / While Else loops - a while loop executes as long as an
        # user-specified condition is evaluated as True; the "else" clause is optional
    x = 1

    while x <= 10:
        print(x)
        x += 1
    else:
        print("Out of the while loop. x is now greater than 10")

    # result of the above "while" block
    # 1 2 3 4 5 6 7 8 9 10
    # Out of the while loop. x is now greater than 10

    # Try / Except / Else / Finally - handling an exception when it occurs
    # and telling Python to keep executing the rest of the lines of code in the program
    try:
        print(4/0)
        # in the "try" clause you insert the code that you think might
        # generate an exception at some point
    except ZeroDivisionError:
        print("Division Error!")
        # specifying what exception types Python should expect as a consequence
        # of running the code inside the "try" block and how to handle them
    else:
        print("No exceptions raised by the try block!")
        # executed if the code inside the "try" block raises NO exceptions
    finally:
        print("I don't care if an exception was raised or not!")
        # executed whether the code inside the "try" block raises an exception or not

def main():
    some_func()

if __name__ == '__main__':
    main()
