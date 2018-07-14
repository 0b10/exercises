"""
A solution for the Valid Parentheses problem on codewars.
http://www.codewars.com/kata/valid-parentheses/python
"""

'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input
string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses
(e.g. [], {}, <>).
'''

'''
What I learned from this:
    * sometimes a simple for-loop is much simpler than recursion, because;
        * a second method has to be specified, to call the recursive one - with extra arguments;
        * the recursive function has a larger signature;
        * the recursive function has to track its own state - where as Python will use the for-loop construct to iterate
            over an iterable;
    * using a list for this problem would be a waste of memory, and inefficient. This is something to consider for all
        problems - not just this one;
    * Being as exclusive as possible with conditionals can avoid a problems - an else clause with no condition can have
        unintended side effects. For example, with this code, exclusive conditionals don't catch any other character
        other than brackets - which is intended.
'''


def valid_parentheses(string):
    stack_size = 0

    for paren in string:
        if paren == '(':
            stack_size += 1
        elif paren == ')':
            stack_size -= 1
            if stack_size < 0:
                return False

    return True if stack_size == 0 else False

