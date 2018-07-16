"""
An improved solution for the Tribonacci Sequence problem on codewars.
http://www.codewars.com/kata/tribonacci-sequence/python

All credit for this improved solution goes to the people found here:
http://www.codewars.com/kata/reviews/556deca37c58da83c00002dd/groups/5579b2b333b6657427000035
"""

'''
Well [sic] met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of
the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers
trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this
sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the
common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2
places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature
array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array
and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math
enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]
'''

'''
What I learned from this:
    * When looping over a data structure, with a 'moving window' - of sorts, slicing can be that window, and referencing
        index items directly can be messy. x[-3:] before x[-3] + x[-2] + x[-1]
    * That expressions, like range(), can effectively replace conditionals. It's easy to place this code within
        conditionals, so that the loop only executes under certain conditions, but range has it's own conditions to
        determine if the loop executes - that is 'n'. It won't execute is n <= the starting index. Essentially,
        for-loops have their own conditional evaluation that can be leveraged, in the context with the rest of the
        logic.
    * That explicit statements can also replace conditionals: a = a[:n] replaced a condition testing to see whether
        the function should return if it's < 3. Essentially here it just slices the list, and the for-loop won't
        execute due to another (related) factor - the size of 'n'.
'''


def tribonacci(signature, n):
    tmp_sig = signature[:n]  # This handles cases where n < 3. It will return 'n' elements. The for-loop wont execute.

    for i in range(3, n):  # This won't execute if n < 3
        tmp_sig.append(sum(tmp_sig[-3:]))  # Slice the last three items, sum, and append it. Repeat.

    return tmp_sig
