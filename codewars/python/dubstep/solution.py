"""
A solution to the Dubstep problem on codewars
http://www.codewars.com/kata/dubstep/python
"""


'''
!! Description !!
Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently,
he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Polycarpus inserts a
certain number of words "WUB" before the first word of the song (the number may be zero), after the last word
(the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy
glues together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot
transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out
what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length
doesn't exceed 200 characters

Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
'''

'''
What I learned from this exercise:
    * filter(func, iterable) is a built-in function that is used to filter an iterable, and returns an iterator of the
        newly created list.
    * func is just a function object, and it's definition may look like: def myFnc(foo):
    * You need to pass func in as a reference type for filter() to call it, and pass in the current iterable item,
        similar to: 'for item in iterable'.
    * That this is also not the most elegant solution, but filter is a very useful function.

'''


def song_decoder(song):
    return ' '.join(list(filter(None, song.split('WUB'))))


def test(song, expected_result):
    assert song_decoder(song) == expected_result


# !! Tests !!
test("AWUBBWUBC", "A B C")
test("AWUBWUBWUBBWUBWUBWUBC", "A B C")
test("WUBAWUBBWUBCWUB", "A B C")
test("TESTWUBWUBTESTWUBWUBTEST", "TEST TEST TEST")
test("WUBTESTWUB", "TEST")
test("WUB", "")
test("WUBWUB", "")
test("TEST", "TEST")