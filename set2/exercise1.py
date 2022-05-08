"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will declare a new list consisting of 6 strings
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # it declared a new list with 6 varables which are all strings

# I think this will print each varable in the list some_words
for word in some_words:
    print(word)
# It printed all the varabls in some_words, one by one

# I think this will print x 6 times over 6 lines
for x in some_words:
    print(x)
# It printed printed all the varabls in some_words, one by one; x only refered to the varable in some_words

# I think this will print all the whole some_word list in one line
print(some_words)
# It printed the whole list including the squre bracket

# I think this will print 'some_words contains more than 3 words'
if len(some_words) > 3:
    print('some_words contains more than 3 words')
# It did print 'some_words contains more than 3 words'

# I think this will print a tuple containing 6 attribute information in regards to the platform
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
# It printed a tuple containing 5 attribute information in regards to the platform [QUESTION]