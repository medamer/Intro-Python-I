"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open("Intro-Python-I/src/foo.txt", "r")
foo = f.read()
print(foo)
f.close
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

t = open("Intro-Python-I/src/bar.txt", "w+")
t.write("As I walk through the valley of the shadow of death \nI take a look at my life and realize there's not much left \ncoz I've been blastin and laughin so long, that \neven my mama thinks that my mind is gone")
t.close

t = open("Intro-Python-I/src/bar.txt", "r")
bar = t.read()
print(bar)
t.close