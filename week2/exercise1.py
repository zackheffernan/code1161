"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

# I think this will look for the string 'word' in the list 'some_words' and then print it.
for word in some_words:
    print(word)  #it did it 

# I think this will search for the string 'x' in the list 'some_words' and then print it, but sicne 'x' does not exist in the list, it will print nothing.
for x in some_words:
    print(x)  #it didn't print x

#I think this will print the the list 'some_words'
print(some_words) #it did

#if the list contains more than 3 words, print the statement 'some_words contains more than three words'
if len(some_words) > 3:
    print('some_words contains more than 3 words')  #it did

#i think this will return information about the user's computer
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #it did

usefulFunction()
