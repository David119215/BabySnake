#!/usr/bin/env python3

# Remember this is a one line comment

""" 
Also, this is a block ("multiline") comment.

Basically, everything between the three quotation marks is
ignored by Python.

Notice the comment on the fist line.  It is special.
It started with a #! - we call this a "shebang."  It lets
Python know this is a special coment.

https://en.wikipedia.org/wiki/Shebang_(Unix) 

"""

import os  # This line lets us use the "print" function provided to us by Python

# This is a function.  A block of code that can be REUSED
def new_function():
    print("  Running new_function()")
    print("  Doing lots of stuff....")
    print("  \"Returning\" from new_function()")
    print("\\")
    print("  BABYSNAKE!!!!!")


# main() is a special function that is always run first
def main():
    print(" Running main")
    print(" About to \"call\" new_function()")
    new_function()
    print(" Finished running new_function()")

    print(" Let's \"call\" new_function() again!")
    new_function()
    print(" Finished running new_function()")
    print(" \"Returning\" from main()")

    x = 2
    y = f(x)
    print(" f(x) where x == 2 returned ", y)

def f(var):
    return var*var

# This is code that will "call" main()
if __name__ == "__main__":
    print("About to \"call\" main()")  # Notice the slash before the quotation mark.  WHY??????
    main()
    print("Finished running main()")
